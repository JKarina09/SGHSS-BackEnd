
# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este projeto é um back-end para gerenciamento de pacientes, consultas e profissionais de saúde, desenvolvido como parte da disciplina de Projeto Multidisciplinar. O sistema é voltado à clínica fictícia **VidaPlus** e implementado com Django REST Framework.

# Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- Django REST Framework
- JWT (Autenticação via djangorestframework-simplejwt)
- SQLite3
- Git

## Como rodar o projeto localmente

1. Clone este repositório:
```bash
git clone https://github.com/JKarina09/SGHSS-BackEnd.git
cd SGHSS-BackEnd
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

##  Autenticação

As rotas protegidas utilizam **JWT**.
Para obter um token, faça um POST para:

```
/api/login/
```

Com:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Use o token recebido como `Authorization: Bearer <token>` nas demais rotas protegidas.

##  Endpoints principais

- POST `/api/pacientes/`
- GET `/api/pacientes/`
- POST `/api/consultas/`
- GET `/api/consultas/`
- POST `/api/login/`
- POST `/api/token/refresh/`

> Documentação completa dos endpoints no relatório final.

##  Testes

Os testes foram realizados via **Postman**, com autenticação JWT e cobertura de todas as rotas principais (cadastro, listagem, atualização e exclusão).

---
