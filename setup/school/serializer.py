from rest_framework import serializers

from school.models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= ['id','name','rg','cpf','birth_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= '__all__'






# Para manter os dados armazenados no banco de dados, criamos um modelo e executamos a migração.

# Sabendo disso, para entregar os dados armazenados no banco de dados no formato Json por exemplo ou receber um Json para salvar no banco de dados, o que devemos fazer?

# Devemos criar uma classe com a responsabilidade de serializar os dados.
# Os dados de saída devem ser serializados em um formato específico, e os dados de entrada serão desserializados para processamento.

# Criamos o modelo de aluno e de curso;

# Configuramos o Django Admin para criar, editar, listar e deletar alunos, alunas ou cursos;

# Criamos a classe responsável para serializar os dados.

#Vamos entender o que são viewsets, configurar nossa url e realizar requisições GET e POST!

# Criamos o serializer que permite que dados sejam convertidos para a forma Python nativa, de modo que o RM do Python entenda, e que sejam facilmente renderizados em JSON, XML, ou outros tipos.

# No nosso caso, vamos manter o padrão JSON. Porém, quem será responsável por receber esses dados e selecionar a serialização utilizada? Visto que recebemos dados em JSON e queremos transformá-los em Python nativo para que o nosso programa entenda?

# Arquivo views.py
# Precisamos de um responsável por essa atividade. Temos o serializador, mas não temos quem diga qual serializer iremos utilizar. Quem fará isso será o nosso arquivo views.py.

# Com ele aberto, teremos acesso ao método que criamos anteriormente para visualizar apenas um aluno.