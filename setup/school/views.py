from django.http import JsonResponse #we're using from django.http import JsonResponse #because we're building an API that will return a Json not render a html page

from rest_framework import viewsets

from school.models import Student, Course, Registration

from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer


class StudentsViewset(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewset(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewset(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

 








# def students(request):
#     if request.method == 'GET':
#         student = {'id':1, 'name':'Yuri'}
#         return JsonResponse(student) #in this part we're not returning a rendered page but a Json we created
