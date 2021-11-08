# Controle de Leitura

`Controle de Leitura` é uma plataforma com o objetivo organizar as suas leituras.

![Tela principal](https://github.com/MarlonFL15/Controle-de-leitura/blob/main/galeria/tabela_leituras.png)

### Motivação

---

Esse projeto foi realizado com o intuito de colocar em prática meus conhecimentos em django. Comecei a estudar esse framework recentemente, e esse projeto surgiu como ideia para colocar o conhecimento adquirido em prática.

Funcionalidades do projeto:
+ Permitir que usuários façam login e se cadastrem;
+ Permitir que os usuários cadastrem suas leituras. Cada leitura leitura está associada a um livro. Além disso, cada leitura contém uma nota (avalição de 1 a 5), status (Lendo, Lido ou Pretendo Ler) e resenha;
+ Permitir que super usuários cadastrem os livros que serão associados a cada leitura;

### Sobre o desenvolvimento

---

* Para o front-end foi utilizado o `Adminlte`, um template gratuito que pode ser baixado em : https://adminlte.io/;
* Para o banco de dados, foi escolhido o SGBD MySQL;
* Foi utilizado o modo de administração padrão do django para manter o controle dos livros;

### Instalação e configuração

---

#### Dependências

* Python 3

Clone o projeto, entre no diretório e baixe todas as bibliotecas necessárias:
    
    $ git clone https://github.com/MarlonFL15/Controle-de-leitura.git
    $ cd Controle-de-leitura
    $ pip install -r requirements.txt
    
    
Após ter baixado tudo, você precisa configurar o banco de dados. Para isso, vá até o arquivo `settings.py` na pasta `controle_livros` e altere as seguintes linhas de acordo com as suas configurações:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'controle_livros',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

Para criar um super usuário e poder cadastrar os livros, você precisa ir no terminal e digitar o seguinte comando:

    $ python manage.py createsuperuser 

Após ter criado o super usuário, você deve executar as migrações e executar o servidor de desenvolvimento:
  
    $ python manage.py migrate
    $ python manage.py runserver

### Conclusões finais

---

Com o desenvolvimento desse projeto, consegui aplicar em prática alguns assuntos que venho estudando sobre django. Eu trabalhei com o django ORM e com a parte de autenticação de usuários. Além disso, também trabalhei com formulários, desenvolvi as telas a partir de um template pronto e utilizei o módulo de administração padrão do django.


### Galeria de imagens

---

Caso você queira ver mais imagens de como ficou a solução final, você pode acessar este link para uma pasta no google drive:
https://drive.google.com/drive/folders/1QkWSf9XFYXhsWPvZC4JJ3FCbgtKITIYT?usp=sharing



