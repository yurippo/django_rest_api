from django.http import JsonResponse #we're using from django.http import JsonResponse #because we're building an API that will return a Json not render a html page

from rest_framework import viewsets, generics

from school.models import Student, Course, Registration

from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationSerializer, ListStudentsRegisteredSerializer

from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated


class StudentsViewset(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewset(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewset(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListsRegistrationSudent(generics.ListAPIView):
    """Listing student registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListRegisteredStudent(generics.ListAPIView):
     """Listing students registered in one course"""
     def get_queryset(self):
         queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
         return queryset
     serializer_class = ListStudentsRegisteredSerializer
     authentication_classes = [BasicAuthentication]
     permission_classes = [IsAuthenticated]





#old code just returning a JSON instead of viewset
# def students(request):
#     if request.method == 'GET':
#         student = {'id':1, 'name':'Yuri'}
#         return JsonResponse(student) #in this part we're not returning a rendered page but a Json we created



#  Criamos uma API, utilizando Django REST Framework. Desenvolvemos recursos de alunos para disponibilizar e aprendemos a trabalhar com as a��es principais do CRUD. 
# Realizamos esse processo para cursos e para matr�culas, vinculando os dois modelos.

# N�s criamos os modelos, os serializamos, preparamos nossos viewsets e registramos URLs para atender �s nossas requisi��es. 
# Tamb�m configuramos mais detalhes sobre alunos e cursos, de modo que podemos consultar todas as matr�culas de uma pessoa e todas as matr�culas em um determinado curso.

# Para finalizar, inclu�mos uma autentica��o b�sica. Mesmo executando o projeto localmente, n�o queremos que qualquer aplica��o tenha acesso � API.

# Ainda h� muito conte�do para estudar sobre APIs, valida��es e testes. Clicando no link do Django REST Framework no topo da p�gina da nossa API,
#  podemos abrir a documenta��o e consultar mais informa��es sobre desenvolvimento de API com essa ferramenta.
