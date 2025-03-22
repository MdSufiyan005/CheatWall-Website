from django.shortcuts import render,redirect
import json
import base64
from .forms import CustomUserForm,CustomAuthenticationForm,CustomTestClassroom,CustomAccessForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Create_Test_ClassRoom,Test_Codes,Student_Response
import random
import string
from .serializers import StudentResponseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



def Landing_Page(request):
    return render(request,'Landing_page.html')

def Register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Home_page')
    else:
        form = CustomUserForm()
    return render(request,'Register.html',{'form':form})

@login_required
def Home_page(request):
    return render(request,'Home.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
               login(request,user) 
               return redirect('Home_page')
            else:
                form.add_error(None,"Invalid username or password")
    else:
        form = CustomAuthenticationForm()

    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('Landing_Page')

# Create view for the test classroom

def generate_unique_access_token():
    length = random.choice([4, 5])
    characters = string.ascii_uppercase + string.digits
    token = ''.join(random.choices(characters, k=length))
    # Ensure the generated token is unique
    while Create_Test_ClassRoom.objects.filter(Access_Token=token).exists():
        length = random.choice([4, 5])
        token = ''.join(random.choices(characters, k=length))
    return token

def encode_json(data):
    # Convert the data to JSON string
    json_data = json.dumps(data,default=str)
    # Encode to bytes and then to Base64
    encoded_bytes = base64.urlsafe_b64encode(json_data.encode('utf-8'))
    # Convert bytes to string
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

@login_required
def create_test_classroom(request):
    if request.method == 'POST':
        form = CustomTestClassroom(request.POST)
        if form.is_valid():
            # Create an instance without saving immediately
            test_classroom = form.save(commit=False)
            # Generate and assign the unique access token
            test_classroom.Access_Token = generate_unique_access_token()
            # Now save the instance with all details
            test_classroom.save()
            content = Create_Test_ClassRoom.objects.get(Access_Token=test_classroom.Access_Token)
            content = {
                'App_Name': content.App_Name,
                'Access_Token': content.Access_Token,
                'Start_Time': content.Start_Time,
                'End_Time': content.End_Time,
                'Discription': content.Discription
            }
            encoded_data = encode_json(content)
            model_test_code = Test_Codes(Test_code=encoded_data,Test_classroom=test_classroom)
            model_test_code.save()
            
            return render(request, 'success.html', {'encoded_data': encoded_data})  # Update to your desired redirect
    else:
        form = CustomTestClassroom()
        
    return render(request, 'Create_class.html', {'form': form})

@login_required
def Test_Codes_view(request):
    tests = Test_Codes.objects.select_related('Test_classroom').all()
    return render(request, 'Test_Codes.html', {'tests': tests})


@login_required
def Student_Response_view(request):
    if request.method == 'POST':
        form = CustomAccessForm(request.POST)
        if form.is_valid():
            access_token = form.cleaned_data.get('Access_Token')
            try:
                test_room = Create_Test_ClassRoom.objects.get(Access_Token=access_token)
            except Create_Test_ClassRoom.DoesNotExist:
                form.add_error('Access_Token', 'Access Token not found.')
                return render(request, 'Dashboard_Temp.html', {'form': form})
            
            # Retrieve student responses related to this test classroom
            content_stu = Student_Response.objects.filter(Test_ClassRoom=test_room)
            
            # Attach an image_list attribute to each response
            for response in content_stu:
                response.image_list = response.Image_URL.split(',') if response.Image_URL else []
            
            # Build a list of image lists for all responses
            row_images = [response.image_list for response in content_stu]
            # JSON-encode the row_images so that it becomes valid JSON in the template
            row_images_json = json.dumps(row_images)
            return render(request, 'Dashboard.html', {
                'form': form,
                'content_stu': content_stu,
                'row_images': row_images_json
            })
    else:
        form = CustomAccessForm()
    return render(request, 'Dashboard_Temp.html', {'form': form})


#  This is the restfull api for the Procting detials

@api_view(['POST'])
def Students_Response_API(request):
    if request.method == 'POST':
        serializer = StudentResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


