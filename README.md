# BiblioteKa

<div>
	<img align="center" alt="Django" height="30" width="60" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg">
	<img align="center" alt="PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
	<img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>


## Index

* [Introdução](#introdução)
* [Base URL](#base--url)
* [Como Rodar os testes](#como--rodar--os--testes)
* [Endpoints](#endpoints)
* [Account](#account)
* [Login](#login)
* [Book](#book)
* [Copy](#copy)
* [Loans](#loans)
* [Gender](#gender)
* [Publishing_company](#publishing_company)


---
<br />

# Introdução
O sistema BiblioteKa é um software desenvolvido no quinto módulo do curso de Desenvolvimento Web Full Stack da Kenzie Academy Brasil. A aplicação gerencia atividades de uma biblioteca. Sendo assim, nosso objetivo é criar uma API para manipular os conteúdos e as regras de negócio.

O banco de dados do sistema é composto por tabelas fundamentais com diferentes responsabilidades, sendo elas:

<ul>
	<li> Usuários: Contamos com 3 principais tipos de usuários: estudante, colaborador da biblioteca (staff) e admin. Os usuários do tipo estudante são aqueles que podem emprestar livros da biblioteca e devem devolvê-los dentro do prazo, eles têm acesso limitado. Os usuários do tipo colaborador da biblioteca são aqueles que trabalham na biblioteca, eles podem adicionar ou remover livros, cópias e agendamentos. Além disso, eles podem gerenciar usuários não staff. Os usuários do tipo admin são aqueles que têm acesso total ao sistema de biblioteca, a grande diferença entre ele e staff é a permissão de gerenciar e criar usuários do tipo staff.</li>
	<li>Livros: Usada para armazenar informações sobre os livros da biblioteca, como título, autor, capa, número de páginas e gênero.</li>
	<li>Gêneros: A tabela de gênero está diretamente relacionada com a tabela de livros, oferecendo uma vasta gama de possibilidades na hora de cadastrar um novo livro no sistema.</li>
	<li>Cópias: Ela é usada para armazenar informações sobre as cópias dos livros da biblioteca. Isso é importante porque permite que os usuários da biblioteca saibam quantas cópias de um livro estão disponíveis para empréstimo e quantas cópias já foram emprestadas.</li>
	<li>Agendamentos: Usada para armazenar informações sobre os agendamentos dos usuários da biblioteca em relação às cópias. No momento do agendamento é gerada uma data em que um usuário levou a cópia e uma data em que a cópia deve ser devolvida. Esse prazo final foi estabelecido como 3 dias úteis depois da data do agendamento. Além disso, o sistema da Biblioteka conta com uma automação que revisa todos os agendamentos uma vez ao dia. Essa automação verifica se os livros foram devolvidos dentro do prazo e define o campo de atraso como verdadeiro caso o agendamento tenha passado do tempo limite</li>
	<li></li>
</ul>

**[⬆ Back to Index](#index)**

---
<br />

# Como Rodar os testes: 

**[⬆ Back to Index](#index)**

---
<br />

# Base url

```
https://doc-biblioteka.onrender.com/
```

**[⬆ Back to Index](#index)**

---
<br />

# Endpoints

### Account
Tipos de usuários:
<ul>
    <li>Estudante</li>
    <li>Colaborador da biblioteca (staff).</li>
    <li>Admin</li>
</ul>


<h4 align ='center'> Listagem de usuários </h4>

```
api/accounts/
```

###### GET - Apenas staff e admin podem listar todos os usuários

Não é necessario corpo de requisição:

`status 200`

Resposta do servidor: 
```json
[
	{
		"id": 1,
		"cpf": "00000000000",
		"username": "user",
		"email": "user@mail.com",
		"is_staff": false,
		"address": "rua 01, numero 000",
		"created_at": "2023-07-10",
		"permission_loan": true,
		"loans": []
	},
	{
		"id": 2,
		"cpf": "00000000002",
		"username": "user2",
		"email": "user2@mail.com",
		"is_staff": false,
		"address": "rua 01, numero 000",
		"created_at": "2023-07-10",
		"permission_loan": true,
		"loans": []
	}
]
```

<h4 align ='center'> Criar usuário </h4>


###### POST - Qualquer pessoa pode criar uma conta. Apenas Admin deve ter permissão para criar staff.

```
api/accounts/
```

Corpo de requisição:
```json
{
	"username": "user",
	"password": "1234",
	"cpf": "00000000000",
	"email": "user@mail.com",
	"address": "rua 01, numero 000"
}
```

Resposta do servidor: 

`status 201`

```json
{
	"id": 1,
	"cpf": "00000000000",
	"username": "user",
	"email": "user@mail.com",
	"is_staff": false,
	"address": "rua 01, numero 000",
	"created_at": "2023-07-10",
	"permission_loan": true,
	"loans": []
}
```


<h4 align ='center'> Consultar usuário </h4>

```
api/accounts/<int:pk>/
```

###### GET -  staff, admin e o próprio usuário


Não é necessario corpo de requisição:

`status 200`

Resposta do servidor: 
```json
{
	"id": 1,
	"cpf": "00000000000",
	"username": "user",
	"email": "user@mail.com",
	"is_staff": false,
	"address": "rua 01, numero 000",
	"created_at": "2023-07-10",
	"permission_loan": true,
	"loans": []
}
```

<h4 align ='center'> Editar usuário </h4>

```
api/accounts/<int:pk>/
```

###### PATCH - staff, admin e o próprio usuário



<h4 align ='center'> Deletar  usuário </h4>

```
api/accounts/<int:pk>/
```
###### DELETE -staff, admin e o próprio usuário

**[⬆ Back to Index](#index)**

---
<br />

### Login

---
<br />

```
api/accounts/login/
```



###### POST - 
Corpo de requisição:
```json
{
	"username": "user",
	"password": "1234"
}
```

status 200
Resposta do servidor: 
```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTYzMTk5NSwiaWF0IjoxNjg5MDI3MTk1LCJqdGkiOiJkMjM5NGJlZjdjOGQ0N2UyOTVhNmJiYTAzZjA5ZmNmMiIsInVzZXJfaWQiOjF9.EgkpxrRVwtBcVRDMnGFD02MTr7ONA7DkO9efdjHOoSg",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDgxMTk1LCJpYXQiOjE2ODkwMjcxOTUsImp0aSI6ImEzNjhlNTE1ZTZkODRiOGVhYzJmYjU0MzY0ZDZhZTc4IiwidXNlcl9pZCI6MX0.BQeJfYOMMV26CraRlyXEYXbsRB0vaKaGwldG0bPfIWY"
}
```


**[⬆ Back to Index](#index)**

---
<br />

### Gender

<h4 align ='center'> Listagem de Gêneros </h4>

```
api/genres/
```
or
```
api/genres/?page=1
```
###### GET -  todos tem acesso
Não é necessario corpo de requisição:

Resposta do servidor: 

`status 200`

```json
{
	"count": 5,
	"next": "https://doc-biblioteka.onrender.com/api/genres/?page=2",
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "Suspense"
		},
		{
			"id": 3,
			"name": "Ficção"
		}
	]
}
```

<h4 align ='center'> Criar Gênero </h4>

```
api/genres/
```

###### POST - apenas staff ou admin

Corpo de requisição:
```json
{
	"name": "Suspense"
}
```

Resposta do servidor: 

`status 201`

```json
{
	"id": 1,
	"name": "Suspense"
}
```


<h4 align ='center'> Consultar Gênero </h4>

```
api/genres/<int:pk>/
```
###### GET - todos tem acesso


<h4 align ='center'> Atualizar Gênero </h4>

```
api/genres/<int:pk>/
```
###### PATCH - apenas staff ou admin
Corpo de requisição:
```json
{
	"name": "um Genero Editadoo"
}
```

Resposta do servidor: 

`status 200`

```json
{
	"id": 4,
	"name": "um Genero Editadoo"
}
```
<h4 align ='center'> Deletar Gênero </h4>

###### DELETE - apenas staff ou admin

```
api/genres/<int:pk>/
```
Não é necessario corpo de requisição:

Resposta do servidor: 

`status 204`

Sem corpo de resposta

**[⬆ Back to Index](#index)**

---
<br />

### Publishing_company

<h4 align ='center'> Listar Editoras </h4>

```
api/publishing_company/
```
or
```
api/publishing_company/?page=1
```
		
###### GET -  todos tem acesso
```json
{
	"count": 4,
	"next": "https://doc-biblioteka.onrender.com/api/publishing_company/?page=2",
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "Editora 01"
		},
		{
			"id": 2,
			"name": "Editora 02"
		}
	]
}
```
<!-- Parei aqui -->
<h4 align ='center'> Criar Editoras </h4>

```
api/publishing_company/
```
###### POST - apenas staff ou admin

```
api/publishing_company/<int:pk>/
```
		
###### GET - todos tem acesso
###### PATCH - apenas staff ou admin
###### DELETE - apenas staff ou admin


**[⬆ Back to Index](#index)**

---
<br />

### Book

```
api/books/
```

###### GET usuários não autenticados podem acessar acessar.


###### POST - apenas staff ou admin pode cadastrar novos livros


```
api/books/<int:pk>/
```	
		
###### GET usuários não autenticados podem acessar acessar.
###### PATCH - apenas staff ou admin pode editar livros
###### DELETE - apenas staff ou admin pode deletar livros

**[⬆ Back to Index](#index)**

---
<br />

### Copy

```
api/books/<int:pk>/copys/
```
	
###### GET -  apenas staff ou admin pode listar cópias
###### POST - apenas staff ou admin pode cadastrar novas cópias


```
api/books/<int:pk>/copys/<int:fk>/
```
###### GET - apenas staff ou admin
###### PATCH - apenas staff ou admin pode editar cópias
###### DELETE - apenas staff ou admin pode deletar cópias


**[⬆ Back to Index](#index)**

---
<br />

### Loans

```
api/loans/
```	

###### GET -  apenas staff ou admin
Não é necessario corpo de requisição:
status 200
Resposta do servidor: 
```json
{
	"count": 7,
	"next": "http://127.0.0.1:8000/api/loans/?page=4",
	"previous": "http://127.0.0.1:8000/api/loans/?page=2",
	"results": [
		{
			"id": 5,
			"overdue": true,
			"created_at": "2023-07-09",
			"deadline": "2023-07-08",
			"finalized_loan": false,
			"copies": [
				1
			],
			"account": 2
		},
		{
			"id": 6,
			"overdue": false,
			"created_at": "2023-07-09",
			"deadline": "2023-07-08",
			"finalized_loan": true,
			"copies": [
				2
			],
			"account": 1
		}
	]
}
```	


###### POST - apenas staff ou admin 
Corpo de requisição:
```json
{
	"copies": [2],
	"account": 1
}
```	

status 201
Resposta do servidor: 
```json
{
	"id": 8,
	"overdue": false,
	"created_at": "2023-07-09",
	"deadline": "2023-07-12",
	"finalized_loan": false,
	"copies": [
		2
	],
	"account": 1
}
```	


```
api/loans/<int:pk>/
```	

###### GET - apenas staff ou admin ou user autenticado
Não é necessario corpo de requisição:
status 200
Resposta do servidor: 
```json
{
	"id": 8,
	"overdue": false,
	"created_at": "2023-07-09",
	"deadline": "2023-07-12",
	"finalized_loan": false,
	"copies": [
		2
	],
	"account": 1
}
```	
###### PUT - apenas staff ou admin
Finalizar agendamento:
Corpo de requisição:
```json
{
  "finalized_loan": true
}
```	

status 200
Resposta do servidor: 
```json
{
	"id": 8,
	"overdue": false,
	"created_at": "2023-07-09",
	"deadline": "2023-07-12",
	"finalized_loan": true,
	"copies": [
		2
	],
	"account": 1
}
```	

**[⬆ Back to Index](#index)**

---
<br />

