# Projeto_UGTSIC_SESAP

Esse repositório contém um sistema de cadastro de currículos desenvolvido com Django.

## Visão Geral

O projeto é um sistema web simples para o cadastro de currículos, permitindo aos usuários:

- Cadastrar novos currículos 
- Visualizar currículos já cadastrados

## Tecnologias Utilizadas

- Backend: Python 3.13, Django
- Frontend: HTML, CSS, Semantic UI, Materialize.

## Pré-requisitos

Certifique-se que você tenha instalado no seu dispositivo:

- Python 3.12 ou superior
- Django instalado
- Git lab
- Qualquer IDE que suporte Python, Git e Django de sua preferência. Para o projeto o usado o Visual Studio Code.

## Instalação

No terminal digite os seguintes comandos:

- git clone https://github.com/gabifpp0/Projeto_UGTSIC_SESAP.git
- py -m pip install django

## Rodando a aplicação

No terminal digite os seguintes comandos:

- cd Projeto_UGTSIC_SESAP
- ativar o venv: venv\Scripts\activate
- cd projcadastroCV
- py manage.py migrate
- py manage.py runserver
- Entrar na url que será fornecida pelo django

## Admin

Para acessar o admin do django vai ser preciso criar um super user. No terminal digite os seguintes comandos:

- py manage.py createsuperuser. Escolha um nome de usuário e senha
- Após a URL coloque /admin 
- Entre com as credenciais cadastradas