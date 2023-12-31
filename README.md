
<div style="display: flex; justify-content: space-between;">
	<h1>BiblioteKa</h1>
	<div>
		<img align="center" alt="Django" height="30" width="60" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg">
		<img align="center" alt="PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
		<img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
	</div>
</div>

# <h1 style="text-align: center; color:#b2d9f7;">Index</h1>

* [Introdução](#introdução)
* [Base URL](#base--url)
* [Como Rodar os testes](#como--rodar--os--testes)
* [Endpoints](#endpoints)
* [Account](#account)
* [Login](#login)
* [Gender](#gender)
* [Publishing_company](#publishing_company)
* [Book](#book)
* [Copy](#copy)
* [Loans](#loans)



# <h1 style="text-align: center; color:#b2d9f7;">Introdução</h1>
<p style="letter-spacing: 2px; line-height: 200%;  text-align: justify;">
O sistema BiblioteKa é um software desenvolvido no quinto módulo do curso de Desenvolvimento Web Full Stack da Kenzie Academy Brasil. A aplicação gerencia atividades de uma biblioteca. Sendo assim, nosso objetivo é criar uma API para manipular os conteúdos e as regras de negócio.
</p>

<p style="letter-spacing: 2px; line-height: 200%;  text-align: justify;">
O banco de dados do sistema é composto por tabelas fundamentais com diferentes responsabilidades, sendo elas:
</p>

<ul>
	<li > 
		<p style="letter-spacing: 2px; line-height: 200%; color:#b2d9f7;">Accounts:</p>
		<p style="line-height: 200%;  text-align: justify;">	Contamos com 3 principais tipos de usuários: estudante, colaborador da biblioteca (staff) e admin. Os usuários do tipo estudante são aqueles que podem emprestar livros da biblioteca e devem devolvê-los dentro do prazo, eles têm acesso limitado. Os usuários do tipo colaborador da biblioteca são aqueles que trabalham na biblioteca, eles podem adicionar ou remover livros, cópias e agendamentos. Além disso, eles podem gerenciar usuários não staff. Os usuários do tipo admin são aqueles que têm acesso total ao sistema de biblioteca, a grande diferença entre ele e staff é a permissão de gerenciar e criar usuários do tipo staff.</p>
	</li>
	<li>
		<p style="letter-spacing: 2px; line-height: 200%; color:#b2d9f7;">Books:</p>
		<p style="line-height: 200%;  text-align: justify;">Usada para armazenar informações sobre os livros da biblioteca, como título, autor, capa, número de páginas e gênero.</p>
	</li>
	<li>
		<p style="letter-spacing: 2px; line-height: 200%; color:#b2d9f7;">Genres:</p>
		<p style="line-height: 200%;  text-align: justify;">A tabela de gênero está diretamente relacionada com a tabela de livros, oferecendo uma vasta gama de possibilidades na hora de cadastrar um novo livro no sistema.</p>
	 </li>
	<li>
		<p style="letter-spacing: 2px; line-height: 200%; color:#b2d9f7;">Copies:</p>
		<p style="line-height: 200%;  text-align: justify;">Ela é usada para armazenar informações sobre as cópias dos livros da biblioteca. Isso é importante porque permite que os usuários da biblioteca saibam quantas cópias de um livro estão disponíveis para empréstimo e quantas cópias já foram emprestadas.</p>	
	 </li>
	<li>
		<p style="letter-spacing: 2px; line-height: 200%; color:#b2d9f7;">Loans:</p>
		<p style="line-height: 200%;  text-align: justify;">Usada para armazenar informações sobre os agendamentos dos usuários da biblioteca em relação às cópias. No momento do agendamento é gerada uma data em que um usuário levou a cópia e uma data em que a cópia deve ser devolvida. Esse prazo final foi estabelecido como 3 dias úteis depois da data do agendamento. Além disso, o sistema da Biblioteka conta com uma automação que revisa todos os agendamentos uma vez ao dia. Essa automação verifica se os livros foram devolvidos dentro do prazo e define o campo de atraso como verdadeiro caso o agendamento tenha passado do tempo limite</p>	
	 </li>
	<li></li>
</ul>

**[⬆ Back to Index](#index)**



# <h1 style="text-align: center; color:#b2d9f7;">Como Rodar os testes</h1>
 

**[⬆ Back to Index](#index)**



# <h1 style="text-align: center; color:#b2d9f7;">Base url</h1>


```
https://doc-biblioteka.onrender.com/
```

**[⬆ Back to Index](#index)**



# <h1 style="text-align: center; color:#b2d9f7;">Endpoints</h1>

# <h2 style="text-align: center; color:#b2d9f7;">Account</h2>

Tipos de usuários:
<ul>
    <li>Estudante</li>
    <li>Colaborador da biblioteca (staff).</li>
    <li>Admin</li>
</ul>

# <h3 style="color:#b2d9f7;">Listagem de usuários</h3>


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

# <h3 style="color:#b2d9f7;">Criar usuário</h3>


```
api/accounts/
```

###### POST - Qualquer pessoa pode criar uma conta. Apenas Admin deve ter permissão para criar staff.


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

# <h3 style="color:#b2d9f7;">Consultar usuário</h3>


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
# <h3 style="color:#b2d9f7;">Editar usuário</h3>


```
api/accounts/<int:pk>/
```

###### PATCH - staff, admin e o próprio usuário


# <h3 style="color:#b2d9f7;">Deletar usuário</h3>


```
api/accounts/<int:pk>/
```
###### DELETE -staff, admin e o próprio usuário

**[⬆ Back to Index](#index)**



# <h2 style="text-align: center; color:#b2d9f7;">Login</h2>


# <h3 style="color:#b2d9f7;">Login</h3>

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


Resposta do servidor: 

`status 200`

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTYzMTk5NSwiaWF0IjoxNjg5MDI3MTk1LCJqdGkiOiJkMjM5NGJlZjdjOGQ0N2UyOTVhNmJiYTAzZjA5ZmNmMiIsInVzZXJfaWQiOjF9.EgkpxrRVwtBcVRDMnGFD02MTr7ONA7DkO9efdjHOoSg",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDgxMTk1LCJpYXQiOjE2ODkwMjcxOTUsImp0aSI6ImEzNjhlNTE1ZTZkODRiOGVhYzJmYjU0MzY0ZDZhZTc4IiwidXNlcl9pZCI6MX0.BQeJfYOMMV26CraRlyXEYXbsRB0vaKaGwldG0bPfIWY"
}
```


**[⬆ Back to Index](#index)**


# <h2 style="text-align: center; color:#b2d9f7;">Gender</h2>

# <h3 style="color:#b2d9f7;">Listagem de Gêneros</h3>


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


# <h3 style="color:#b2d9f7;"> Criar Gênero </h3>


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



# <h3 style="color:#b2d9f7;"> Consultar Gênero </h3>


```
api/genres/<int:pk>/
```
###### GET - todos tem acesso




# <h3 style="color:#b2d9f7;"> Atualizar Gênero  </h3>


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




# <h3 style="color:#b2d9f7;"> Deletar Gênero   </h3>


```
api/genres/<int:pk>/
```
###### DELETE - apenas staff ou admin

Não é necessario corpo de requisição:

Resposta do servidor: 

`status 204`

Sem corpo de resposta

**[⬆ Back to Index](#index)**

# <h2 style="text-align: center; color:#b2d9f7;">Publishing_company</h2>

# <h3 style="color:#b2d9f7;">Listar Editoras</h3>

```
api/publishing_company/
```
or
```
api/publishing_company/?page=1
```
###### GET -  todos tem acesso
Não é necessario corpo de requisição:

Resposta do servidor: 

`status 200`

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


# <h3 style="color:#b2d9f7;">Criar Editoras</h3>


```
api/publishing_company/
```
###### POST - apenas staff ou admin

Corpo de requisição:
```json
{
	"name": "Editora 01"
}
```

Resposta do servidor: 

`status 201`

```json
{
	"id": 1,
	"name": "Editora 01"
}
```
# <h3 style="color:#b2d9f7;">Consultar Editora</h3>


```
api/publishing_company/<int:pk>/
```	
###### GET - todos tem acesso

Não é necessario corpo de requisição:

Resposta do servidor: 

`status 200`
# <h3 style="color:#b2d9f7;">Editar  Editora</h3>



```
api/publishing_company/<int:pk>/
```	
###### PATCH - apenas staff ou admin
Corpo de requisição:
```json
{
	"name": "um valor Editado"
}
```

Resposta do servidor: 

`status 201`

```json
{
	"id": 4,
	"name": "um valor Editado"
}
```
# <h3 style="color:#b2d9f7;">Deletar  Editora</h3>

>

```
api/publishing_company/<int:pk>/
```	
###### DELETE - apenas staff ou admin
Não é necessario corpo de requisição:

Resposta do servidor: 

`status 204`

Sem corpo de resposta

**[⬆ Back to Index](#index)**

# <h2 style="text-align: center; color:#b2d9f7;">Book</h2>


# <h3 style="color:#b2d9f7;"> Listar Livros</h3>


```
api/books/
```
or
```
api/books/?page=1
```

###### GET usuários não autenticados podem acessar acessar.

Não é necessario corpo de requisição:

Resposta do servidor: 

`status 200`

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "A cabana",
			"author": "William P. Young",
			"number_page": 240,
			"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
			"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
			"published": 2008,
			"number_copy": 7,
			"copies_available": 7,
			"publishing_company": {
				"id": 7,
				"name": "Publishing Company 01"
			},
			"genres": [
				{
					"id": 1,
					"name": "Suspense"
				}
			]
		}
	]
}
```
# <h3 style="color:#b2d9f7;"> Cadastrar Livro</h3>


```
api/books/
```

###### POST - apenas staff ou admin pode cadastrar novos livros
Corpo de requisição:
```json
{
	"title": "A cabana",
    "author": 	" William P. Young ",
    "number_page": 240,
    "description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
    "cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
    "published": 2008,
    "number_copy": 7,
    "copies_available": 7,
	"publishing_company": {"name": "Publishing Company 01"},
	"users": [1],
	"genres": [{"name": "Suspense"}]
}
```

Resposta do servidor: 

`status 201`

```json
{
	"id": 1,
	"title": "A cabana",
	"author": "William P. Young",
	"number_page": 240,
	"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
	"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
	"published": 2008,
	"number_copy": 7,
	"copies_available": 7,
	"publishing_company": {
		"id": 7,
		"name": "Publishing Company 01"
	},
	"genres": [
		{
			"id": 1,
			"name": "Suspense"
		}
	]
}
```
# <h3 style="color:#b2d9f7;"> Consultar Livro</h3>


		
```
api/books/<int:pk>/
```	
###### GET usuários não autenticados podem acessar acessar.


# <h3 style="color:#b2d9f7;"> Editar Livro</h3>




```
api/books/<int:pk>/
```	

###### PATCH - apenas staff ou admin pode editar livros

Corpo de requisição:
```json
{
	  "title": "Um título Editado"
}
```
# <h3 style="color:#b2d9f7;"> Deletar Livro</h3>


```
api/books/<int:pk>/
```	

###### DELETE - apenas staff ou admin pode deletar livros

**[⬆ Back to Index](#index)**


# <h2 style="text-align: center; color:#b2d9f7;">Copy</h2>

# <h3 style="color:#b2d9f7;"> Listar Cópias</h3>


<h4 align ='center'> </h4>
	
```
api/books/copys/
```
ou
```
api/books/copys/?page=1
```

###### GET -  apenas staff ou admin pode listar cópias
Não é necessario um corpo de requisição.

Resposta do servidor:
`Statu 200`

```json
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"number_copy_book": 1,
			"available": true,
			"conservation_state": "Bom estado",
			"book": {
				"id": 1,
				"title": "A cabana",
				"author": "William P. Young",
				"number_page": 240,
				"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
				"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
				"published": 2008,
				"number_copy": 7,
				"copies_available": 7,
				"publishing_company": {
					"id": 7,
					"name": "Publishing Company 01"
				},
				"genres": [
					{
						"id": 1,
						"name": "Suspense"
					}
				]
			}
		},
		{
			"id": 2,
			"number_copy_book": 2,
			"available": true,
			"conservation_state": "Bom estado",
			"book": {
				"id": 1,
				"title": "A cabana",
				"author": "William P. Young",
				"number_page": 240,
				"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
				"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
				"published": 2008,
				"number_copy": 7,
				"copies_available": 7,
				"publishing_company": {
					"id": 7,
					"name": "Publishing Company 01"
				},
				"genres": [
					{
						"id": 1,
						"name": "Suspense"
					}
				]
			}
		}
	]
}
```
# <h3 style="color:#b2d9f7;"> Cadastrar Cópia</h3>


```
api/books/<int:pk>/copys/
```
###### POST - apenas staff ou admin pode cadastrar novas cópias

Corpo de requisição:
```json
{
	"number_copy_book": 1,
	"conservation_state": "Bom estado"
}
```

Resposta do servidor 

`Status 201`

```json
{
	"id": 1,
	"number_copy_book": 1,
	"available": true,
	"conservation_state": "Bom estado",
	"book": {
		"id": 1,
		"title": "A cabana",
		"author": "William P. Young",
		"number_page": 240,
		"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
		"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
		"published": 2008,
		"number_copy": 7,
		"copies_available": 7,
		"publishing_company": {
			"id": 7,
			"name": "Publishing Company 01"
		},
		"genres": [
			{
				"id": 1,
				"name": "Suspense"
			}
		]
	}
}
```
# <h3 style="color:#b2d9f7;"> Consultar Cópia</h3>


###### GET - apenas staff ou admin

# <h3 style="color:#b2d9f7;"> Editar Cópia</h3>


###### PATCH - apenas staff ou admin pode editar cópias

# <h3 style="color:#b2d9f7;"> Deletar Cópia</h3>


###### DELETE - apenas staff ou admin pode deletar cópias


**[⬆ Back to Index](#index)**



# <h2 style="text-align: center; color:#b2d9f7;">Loans</h2>

# <h3 style="color:#b2d9f7;"> Listar todos  Agendamentos</h3>
 
```
api/loans/
```	
ou
```
api/loans/?page=1
```	

###### GET -  apenas staff ou admin

Não é necessario corpo de requisição:

`Status 200`

Resposta do servidor: 
```json
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"overdue": false,
			"created_at": "2023-07-11",
			"deadline": "2023-07-14",
			"finalized_loan": false,
			"account": 1,
			"loan_copies": [
				{
					"id": 1,
					"number_copy_book": 1,
					"available": false,
					"conservation_state": "Bom estado",
					"book": {
						"id": 1,
						"title": "A cabana",
						"author": "William P. Young",
						"number_page": 240,
						"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
						"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
						"published": 2008,
						"number_copy": 7,
						"copies_available": 7,
						"publishing_company": {
							"id": 7,
							"name": "Publishing Company 01"
						},
						"genres": [
							{
								"id": 1,
								"name": "Suspense"
							}
						]
					}
				}
			]
		},
		{
			"id": 2,
			"overdue": false,
			"created_at": "2023-07-11",
			"deadline": "2023-07-14",
			"finalized_loan": false,
			"account": 1,
			"loan_copies": [
				{
					"id": 2,
					"number_copy_book": 2,
					"available": false,
					"conservation_state": "Bom estado",
					"book": {
						"id": 1,
						"title": "A cabana",
						"author": "William P. Young",
						"number_page": 240,
						"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
						"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
						"published": 2008,
						"number_copy": 7,
						"copies_available": 7,
						"publishing_company": {
							"id": 7,
							"name": "Publishing Company 01"
						},
						"genres": [
							{
								"id": 1,
								"name": "Suspense"
							}
						]
					}
				}
			]
		}
	]
}
```	
# <h3 style="color:#b2d9f7;">  Criar Agendamento</h3>


###### POST - apenas staff ou admin 
Corpo de requisição:
```json
{
	"copies": [1],
	"account": 1
}
```	
`status 201`

Resposta do servidor: 
```json
{
	"id": 1,
	"overdue": false,
	"created_at": "2023-07-11",
	"deadline": "2023-07-14",
	"finalized_loan": false,
	"account": 1,
	"loan_copies": [
		{
			"id": 1,
			"number_copy_book": 1,
			"available": false,
			"conservation_state": "Bom estado",
			"book": {
				"id": 1,
				"title": "A cabana",
				"author": "William P. Young",
				"number_page": 240,
				"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
				"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
				"published": 2008,
				"number_copy": 7,
				"copies_available": 6,
				"publishing_company": {
					"id": 7,
					"name": "Publishing Company 01"
				},
				"genres": [
					{
						"id": 1,
						"name": "Suspense"
					}
				]
			}
		}
	]
}
```	
<p style="letter-spacing: 2px; line-height: 200%;  text-align: justify;">
Nota: Observe que ao criar um agendamento para a cópia de id 1, o campo “available” que antes era verdadeiro agora é falso. Da mesma forma, o campo “copies_available” do livro correspondente foi decrementado em 1.
</p>

# <h3 style="color:#b2d9f7;">  Consultar Agendamento</h3>


```
api/loans/<int:pk>/
```	

###### GET - apenas staff ou admin ou user autenticado
Não é necessario corpo de requisição:
`status 200`
Resposta do servidor: 
```json
{
	"id": 1,
	"overdue": false,
	"created_at": "2023-07-11",
	"deadline": "2023-07-14",
	"finalized_loan": false,
	"account": 1,
	"loan_copies": [
		{
			"id": 1,
			"number_copy_book": 1,
			"available": false,
			"conservation_state": "Bom estado",
			"book": {
				"id": 1,
				"title": "A cabana",
				"author": "William P. Young",
				"number_page": 240,
				"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
				"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
				"published": 2008,
				"number_copy": 7,
				"copies_available": 6,
				"publishing_company": {
					"id": 7,
					"name": "Publishing Company 01"
				},
				"genres": [
					{
						"id": 1,
						"name": "Suspense"
					}
				]
			}
		}
	]
}
```	
# <h3 style="color:#b2d9f7;">  Devolução do livro - Atualizar  Agendamento</h3>


###### PUT - apenas staff ou admin

Corpo de requisição:
```json
{
  "finalized_loan": true
}
```	

`status 200`

Resposta do servidor: 
```json
{
	"id": 1,
	"overdue": false,
	"created_at": "2023-07-11",
	"deadline": "2023-07-14",
	"finalized_loan": true,
	"account": 1,
	"loan_copies": [
		{
			"id": 1,
			"number_copy_book": 1,
			"available": true,
			"conservation_state": "Bom estado",
			"book": {
				"id": 1,
				"title": "A cabana",
				"author": "William P. Young",
				"number_page": 240,
				"description": "Durante uma viagem de fim de semana, a filha mais nova de Mack Allen Phillips é raptada e evidências de que ela foi brutalmente assassinada são encontradas numa velha cabana. Após quatro anos vivendo numa tristeza profunda causada pela culpa e pela saudade da menina, Mack recebe um estranho bilhete, aparentemente escrito por Deus, convidando-o a voltar à cabana onde acontecera a tragédia. Apesar de desconfiado, ele vai ao local numa tarde de inverno e adentra passo a passo o cenário de seu mais terrível pesadelo. Mas o que ele encontra lá muda o seu destino para sempre. Em um mundo cruel e injusto, A cabana levanta um questionamento atemporal: se Deus é tão poderoso, por que não faz nada para amenizar nosso sofrimento? As respostas que Mack encontra vão surpreender você e podem transformar sua vida de maneira tão profunda quanto transformaram a dele. Você vai querer partilhar esse livro com todas as pessoas que ama.",
				"cover": "https://m.media-amazon.com/images/I/91rc6PHsvIL._SY466_.jpg",
				"published": 2008,
				"number_copy": 7,
				"copies_available": 7,
				"publishing_company": {
					"id": 7,
					"name": "Publishing Company 01"
				},
				"genres": [
					{
						"id": 1,
						"name": "Suspense"
					}
				]
			}
		}
	]
}
```	

<p style="letter-spacing: 2px; line-height: 200%;  text-align: justify;">
Nota: Observe que ao finalizar o agendamento da cópia de id 1, o campo “available” que antes era falso agora é verdadeiro. Da mesma forma, o campo “copies_available” do livro correspondente foi acrescentado em 1.
</p>


**[⬆ Back to Index](#index)**

---
<br />

