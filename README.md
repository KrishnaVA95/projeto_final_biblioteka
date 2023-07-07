
# BiblioteKa
<div>
  <img align="center" alt="Django" height="30" width="60" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg">
  <img align="center" alt="PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

O sistema de BiblioteKa é um software que foi desenvolvido, em python, para gerenciar as atividades de uma biblioteca. O banco de dados do sistema é composto por várias tabelas:

-> Usuários: Contamos com 3 principais tipos de usuários: estudante, colaborador da biblioteca (staff) e admin. Os usuários do tipo estudante são aqueles que podem emprestar livros da biblioteca e devem devolvê-los dentro do prazo, eles têm acesso limitado. Os usuários do tipo colaborador da biblioteca são aqueles que trabalham na biblioteca, eles podem adicionar ou remover livros, cópias e agendamentos. Além disso, eles podem gerenciar usuários não staff. Os usuários do tipo admin são aqueles que têm acesso total ao sistema de biblioteca, a grande diferença entre ele e staff é a permissão de gerenciar e criar usuários do tipo staff.

-> Livros: Usada para armazenar informações sobre os livros da biblioteca, como título, autor, capa, número de páginas e gênero.

-> Gêneros: A tabela de gênero está diretamente relacionada com a tabela de livros, oferecendo uma vasta gama de possibilidades na hora de cadastrar um novo livro no sistema.

-> Cópias: Ela é usada para armazenar informações sobre as cópias dos livros da biblioteca. Isso é importante porque permite que os usuários da biblioteca saibam quantas cópias de um livro estão disponíveis para empréstimo e quantas cópias já foram emprestadas.

-> Agendamentos: Usada para armazenar informações sobre os agendamentos dos usuários da biblioteca em relação às cópias. No momento do agendamento é gerada uma data em que um usuário levou a cópia e uma data em que a cópia deve ser devolvida. Esse prazo final foi estabelecido como 3 dias úteis depois da data do agendamento. Além disso, o seu sistema da biblioteca conta com uma automação que revisa todos os agendamentos uma vez ao dia. Essa automação verifica se os livros foram devolvidos dentro do prazo e define o campo de atraso como verdadeiro caso o agendamento tenha passado do tempo limite




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


