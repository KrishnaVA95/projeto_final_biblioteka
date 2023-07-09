
# BiblioteKa
<div>
  <img align="center" alt="Django" height="30" width="60" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg">
  <img align="center" alt="PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

# INDEX
<ul align="center" >
	<li> ## Introdução {###Introdução}</li>

</ul>


### Introdução
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





# Como Rodar os tests: 

# Rotas e Endpoints
base url:
```

```
### Account
Tipos de usuários:
<ul>
    <li>Estudante</li>
    <li>Colaborador da biblioteca (staff).</li>
    <li>Admin</li>
</ul>


```
api/accounts/
```

###### GET - Apenas staff e admin podem listar todos os usuários
Não é necessario corpo de requisição:
status 200
Resposta do servidor: 
```

```


###### POST - Qualquer pessoa pode criar uma conta. Apenas Admin deve ter permissão para criar staff.

Corpo de requisição:
```json
{
	"username": "user",
	"password": "1234",
	"cpf": "00000000007",
	"email": "user@mail.com",
	"address": "rua 01, numero 000"
}
```

status 201
Resposta do servidor: 
```json
{
	"id": 4,
	"cpf": "00000000007",
	"username": "user",
	"email": "user@mail.com",
	"is_staff": false,
	"address": "rua 01, numero 000",
	"created_at": "2023-07-09",
	"permission_loan": true,
	"loans": []
}
```


```
api/accounts/login/
```
###### POST -Login
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
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTUxNDk2NSwiaWF0IjoxNjg4OTEwMTY1LCJqdGkiOiIzZDkyMjNkOGNlN2I0NDcyOWFhYjU5NWM2MzJkY2JiZSIsInVzZXJfaWQiOjR9.4YNclXtwpY-IuN66plToo_pC5xLdeegvaeGKOG9wh_o",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTY0MTY1LCJpYXQiOjE2ODg5MTAxNjUsImp0aSI6IjMwYjQ0ZjFjZDg5MjQzNGNhODE3OWY4ZDQwNDJkNGIxIiwidXNlcl9pZCI6NH0.rgdOrMMFjvlaSZuavcouvZWpMIr0e0vM-1nNBzxcLfs"
}
```

```
api/accounts/<int:pk>/
```

###### GET -  staff, admin e o próprio usuário
###### PATCH - staff, admin e o próprio usuário
###### DELETE -staff, admin e o próprio usuário

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


### Gender
```
api/genres/
```

###### GET -  todos tem acesso
###### POST - apenas staff ou admin

```
api/genres/<int:pk>/
```
		
	
###### GET - todos tem acesso
###### PATCH - apenas staff ou admin
###### DELETE - apenas staff ou admin



### Publishing_company

```
api/publishing_company/
```
		
###### GET -  todos tem acesso
###### POST - apenas staff ou admin

```
api/publishing_company/<int:pk>/
```
		
###### GET - todos tem acesso
###### PATCH - apenas staff ou admin
###### DELETE - apenas staff ou admin


