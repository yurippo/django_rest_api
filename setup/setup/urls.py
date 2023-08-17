from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewset, CoursesViewset, RegistrationViewset, ListsRegistrationSudent, ListRegisteredStudent
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewset, basename='Students')
router.register('courses', CoursesViewset, basename='Courses')
router.register ('registrations', RegistrationViewset, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('students/<int:pk>/registrations/', ListsRegistrationSudent.as_view()),
    path('courses/<int:pk>/registrations/', ListRegisteredStudent.as_view())
]








#that's the idea of the API through some different addresses/URLS we wanna make available
# some different functionalities
# we wanna base on the address and the method of the requisition I want to create a student
# I wanna delete a student
#in models.py I want to create a model business rules and integrate it with the database
#I want that in the moment that I receive requests I return a Json file and to help us o that
#there's a tool called Django Rest Framework to do all that how we create the URls and main routes
# of our application  


# os ViewSets permitem definir as intera��es da sua API e permitir que a estrutura REST construa os URLs dinamicamente com um objeto roteador

# A utiliza��o de Viewset pode evitar repetir a l�gica das views
# Certo! N�o ser� necess�rio incluir a l�gica para um CRUD, analisando as estruturas do REST para cada recurso.

#Viewsets incluem a��es como criar, listar, atualizar ou deletar
#Certo! Os Viewsets incluem essas a��es ou opera��es por padr�o

#Porem Um Viewset � a fonte �nica e definitiva de informa��es sobre seus dados
#Um modelo sim � a fonte �nica e definitiva de informa��es sobre seus dados e n�o um Viewset

# Criamos as classes AlunosViewSet e CursosViewSet para usufruir das principais ;

# Realizamos uma requisi��o GET retornando um Json;

# Instalamos o Django Rest Framework.

# Vamos executar requisi��es dos tipos PUT, PATH, DELETE e criar um novo modelo de matr�cula, para vincular um aluno ou aluna em um curso!
