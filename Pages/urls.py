from django.urls import path
from .views import Landing_Page,Register_view,login_view,logout_view,Home_page,create_test_classroom,Test_Codes_view,Student_Response_view,Students_Response_API
urlpatterns = [
    path('',Landing_Page,name='Landing_Page'),
    path('Register/',Register_view,name='Register_view'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('Home/',Home_page,name='Home_page'),
    path('Home/Create_Test_Classroom/',create_test_classroom,name='create_test_classroom'),
    path('Home/Test_Codes/',Test_Codes_view,name='Test_Codes'),
    path('Home/Student_Response_view/',Student_Response_view,name='Student_Response_view'),
    path('api/Student_Response/',Students_Response_API,name='Students_Response_API'),
]
