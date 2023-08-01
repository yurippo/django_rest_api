# Hello, World!

# Django Rest API

# Neste Projeto, vamos aprofundar nosso conhecimento utilizando o Django, criando um API junto a biblioteca do Django Rest Framework.

# instalando o Django Rest API	Vamos aprender o que é uma API, JSON e realizar uma requisição GET
# Modelos, Admin e Serializers	Vamos criar 2 modelos, vincular o Django Admin e serializar os modelos
# Viewset e requisições GET e POST	Vamos entender na prática o que é o viewset e realizar requisições GET e POST
# Atualizando e deletando recursos	Vamos atualizar e deletar os recursos e criar um novo modelo
# ListAPIView e Autenticação	Vamos utilizar o ListAPIView e adicionar autenticação na API

# Preparando ambiente

# é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

# Python 3.7.4
# Django 3.0.7
# O Django pode ser instalado através do comando:
# pip install Django==3.0.7

# Para otimizar o tempo do curso, criamos esta atividade descrevendo o passo a passo para criação de um projeto Django. Os passos são:

# Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:

# python3 -m venv ./venv

# Ative seu ambiente virtual com o seguinte comando (MAC e Linux):

# source venv/bin/activate

# Em caso de Windows, utilize o comando:

# venv\Scripts\activate.bat

# Instale o Django nesse ambiente virtualizado:

# pip install django

# Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:

# django-admin startproject setup 

# Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

# LANGUAGE_CODE = 'pt-br'
# TIME_ZONE = 'America/Sao_Paulo'

# vamos utilizar o Postman que é uma ferramenta que tem como objetivo testar serviços da API. Para instalar, faça o download do Postman.




