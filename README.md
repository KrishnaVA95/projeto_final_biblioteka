
# BiblioteKa
<div>
  <img align="center" alt="Django" height="30" width="60" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg">
  <img align="center" alt="PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>




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
List
###### GET - Apenas staff e admin podem listar todos os usuários
não é necessario um corpo de requisição

create
###### POST - Qualquer pessoa pode criar uma conta. Apenas Admin deve ter permissão para criar staff.

datos de entrada: 
```json
{
	"name": "",
	"email": "",
	"password": "",
	"address": "",
	"cpf":""
}

```
dados de saída:
```json
{
	"id": 1,
	"name": "",
	"email": "",
	"address": "",
	"cpf": "",
	"is_staff": false,
	"permission_loan": true
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
###### POST - apenas staff ou admin 

```
api/loans/<int:pk>/
```	

###### GET - apenas staff ou admin ou user autenticado
###### PATCH - apenas staff ou admin
###### DELETE - apenas staff ou admin 


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


