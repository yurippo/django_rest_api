from django.contrib import admin

from school.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id','name','rg','cpf','birth_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student,Students)

class Courses(admin.ModelAdmin):
    list_display = ('id','code_course','description')
    list_display_link = ('id','code_course')
    search_fields = ('code_course',)

admin.site.register(Course,Courses)

class Registrations(admin.ModelAdmin):
    list_display= ('id','student','course')
    list_display_links= ('id',)

admin.site.register(Registration,Registrations)


# WARNINGS:
# school.Course: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
#         HINT: Configure the DEFAULT_AUTO_FIELD setting or the AchoolConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
# school.Student: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
#         HINT: Configure the DEFAULT_AUTO_FIELD setting or the AchoolConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
# Username (leave blank to use 'yuri'): yuri
# Email address: yuri@yurippo.com
# Password: 
# Password (again): 
# Superuser created successfully.
# (venv) yuri@mintBox:~/django_rest_api/setup$ 
