from rest_framework import serializers
from .models import Student_Response,Create_Test_ClassRoom

from rest_framework import serializers
from .models import Student_Response, Create_Test_ClassRoom
from rest_framework import serializers
from .models import Student_Response, Create_Test_ClassRoom

class StudentResponseSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=200)
    Enrolment_no = serializers.CharField(max_length=200)
    RiskScore = serializers.CharField(max_length=200)
    # For input, accept a list of URLs.
    Image_URL = serializers.ListField(
        child=serializers.CharField(max_length=200),
        allow_empty=True
    )
    # Use write_only so it's only used during creation
    Access_Token = serializers.CharField(max_length=200, write_only=True)
    
    def create(self, validated_data):
        # Extract the access token and remove it from validated_data
        access_token = validated_data.pop('Access_Token')
        try:
            # Look up the Test_ClassRoom using the provided access token
            test_classroom = Create_Test_ClassRoom.objects.get(Access_Token=access_token)
        except Create_Test_ClassRoom.DoesNotExist:
            raise serializers.ValidationError("Test classroom not found for the given access token.")
        
        # Process the list of image URLs into a comma-separated string
        image_urls = validated_data.pop('Image_URL', [])
        image_urls_str = ",".join(image_urls) if image_urls else ""
        
        # Create the Student_Response instance
        student_response = Student_Response.objects.create(
            Test_ClassRoom=test_classroom,
            Image_URL=image_urls_str,
            **validated_data
        )
        return student_response

    def to_representation(self, instance):
        """
        Override the default output so that Image_URL is returned as a list of URLs.
        """
        return {
            "Name": instance.Name,
            "Enrolment_no": instance.Enrolment_no,
            "RiskScore": instance.RiskScore,
            "Image_URL": instance.Image_URL.split(",") if instance.Image_URL else []
        }
