# ⚽ Sistema de Futebol - Django Fullstack

Projeto desenvolvido como parte de um processo seletivo para vaga de desenvolvedor **Fullstack Django**.

---

## 📌 Funcionalidades

✔ Sistema de login e logout
✔ Proteção de rotas (apenas usuários autenticados acessam o sistema)
✔ CRUD completo de Times
✔ Mensagens de feedback (sucesso/erro)
✔ Confirmação de exclusão
✔ Interface web com templates
✔ API REST com Django Rest Framework

---

## 🧱 Tecnologias utilizadas

* Python
* Django
* Django Rest Framework
* SQLite
* HTML + CSS

---

## 📁 Estrutura do projeto

```
futebol_project/
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── urls.py
│   ├── templates/
│   │   └── times/
│   │       ├── lista.html
│   │       ├── form.html
│   │       └── confirm_delete.html
│
├── futebol_project/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acessar a pasta

```
cd futebol_project
```

### 3. Criar ambiente virtual

```
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```
venv\Scripts\activate
```

### 5. Instalar dependências

```
pip install django djangorestframework
```

### 6. Rodar migrações

```
python manage.py migrate
```

### 7. Criar superusuário

```
python manage.py createsuperuser
```

### 8. Rodar o servidor

```
python manage.py runserver
```

---

## 🌐 Acessos

* Sistema web: http://127.0.0.1:8000/login/
* Admin: http://127.0.0.1:8000/admin/
* API:

  * /api/times/
  * /api/jogadores/
  * /api/partidas/

---

## 🔐 Segurança

* Autenticação obrigatória nas rotas
* CSRF Token nos formulários
* Exclusão via POST (boa prática)

---

## 📌 Critérios atendidos

✔ Proteção de rotas
✔ Validação de formulários
✔ Tratamento de erros
✔ Serialização com ModelSerializer
✔ Status HTTP corretos
✔ Estrutura de rotas REST
✔ Mensagens de feedback
✔ Templates com herança (`base.html`)
✔ Navegação funcional
✔ Organização do código
✔ Versionamento com Git
✔ Documentação com README

---

## 👨‍💻 Autor

Desenvolvido por **Daphne Carvalho**
