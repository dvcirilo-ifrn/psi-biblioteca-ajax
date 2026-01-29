# Exemplo de CRUD com AJAX no Django
Material de apoio da disciplina de [Programação de Sistemas para Internet](https://dvcirilo.github.io/psi-ifrn) do IFRN - Campus São Paulo do Potengi.

## Informações
- Sistema simples de lista de livros;
    - Usuários avulsos podem ver a lista e detalhes dos livros;
    - Há a funcionalidade de busca por titulo/autor/gênero;
    - O usuário avulso pode se cadastrar;
    - O usuário comum logado pode adicionar/remover livros aos seus favoritos;
    - O usuário comum logado pode listar seus favoritos;
    - O administrador pode gerenciar livros e usuários.
- O objetivo é demonstrar o uso do AJAX com [Django](https://www.djangoproject.com/);

## Implementação
- *Front-end* feito usando apenas blocos de exemplo do [Bootstrap 5](https://getbootstrap.com/);
- JavaScript *Vanilla* para manipulação do DOM e requisições (usando `fetch`);
- *Back-end* seguindo os exemplos da documentação do Django e usando FBVs (*Function Based Views*)
- Nomenclatura em português para facilitar a compreensão;
- Pastas de `templates` e `static` na raiz, com sub-pastas para cada *app*, evitando conflitos;
- 3 *apps*:
    - biblioteca: app principal
    - dashboard: páginas de gerenciamento do sistema
    - contas: gerenciamento de usuários
- Autenticação do Django;
- *Forms* com [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms);

## Rodando
- Clone o repositório;
- Dentro da pasta do repositório inicie e ative um `venv`;
- Instale as dependências:
    - `pip install -r requirements.txt`
- Inicie o BD:
    - `python manage.py migrate`
- Crie um *superuser*:
    - `python manage.py createsuperuser`
- Instale as fixtures (banco de dados inicial de livros)
    - `python manage.py loaddata livros.json`
- Baixe as [capas](https://drive.google.com/file/d/1lu0KvmThV-fP-TtD3dtad9BJ9GYZRbmn/view?usp=sharing) e coloque na pasta `media/biblioteca/capas/`
    - É necessário criar essas pastas;
    - Precisa estar logado com email escolar para conseguir baixar;
    - Caso não tenha acesso, é apenas uma pasta com 30 imagens *png* numeradas (`1.png`, `2.png`, etc.);
- Rode o servidor:
    - `python manage.py runserver`

## Contribuições
- O objetivo do sistema é apenas educacional;
- O código tenta ser simples;
- O código tenta seguir os exemplos das documentações:
    - Facilita o entendimento por iniciantes;
- O código tenta seguir boas práticas de estilo e segurança;
- São bem vindas contribuições no sentido de:
    - Simplificar o código;
    - Atualizar recomendações da documentação;
    - Atualizar as boas práticas.
- Crie seu *fork* e abra um PR para o *branch* `dev`!

