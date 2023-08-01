from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self): #so I can represent the object on a String format
        return self.name
    

class Course(models.Model):
    LEVEL = (
        ('B','Basic'),
        ('I', 'Intermediate'),
        ('A','Advanced')
    )
    code_course = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False,default='B')


    def __str__(self): #so I can represent the object on a String format
        return self.description
    
    #Now we're going to migrate it to the database in settings.py I'll add school