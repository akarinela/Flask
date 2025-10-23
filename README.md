Nesse repositorio vou guardar as aulas sobre novo conteudo de Desenvolvimento Web ll **Flask**

---

**Flask** é um microframework web para a linguagem de programação Python, projetado para ser leve e flexível. Ele fornece um núcleo mínimo e extensível para criar aplicações web, permitindo que os desenvolvedores adicionem bibliotecas e ferramentas para funcionalidades como bancos de dados e validação de formulários. É frequentemente recomendado para iniciantes por sua simplicidade, mas também é usado para construir aplicações complexas e é adequado para criar tanto sites quanto APIs. É um framework escrito em Python, utilizando-o para construir aplicações web. 

Microframework: Significa que possui um núcleo pequeno e simples, sem a obrigatoriedade de componentes como um ORM (Object-Relational Mapper) ou sistema de validação de formulários. Ele oferece a flexibilidade para escolher e adicionar essas funcionalidades através de extensões. 

Leve e flexível: Por ser leve, permite que os desenvolvedores tenham mais controle sobre a estrutura da aplicação e só adicionem o que precisam. 

---

**Fluxo de execução no FLASK:**
1. O arquivo principal (__init__) importa o Flask e cria as bases do site.
2. As rotas são criadas em um arquivo separado chamado de routes.py ou views.py.
3. O arquivo principal importa as rotas do arquivo de views e esse precisa importar o app do __init__ para que a conexao funcione.
4. Para criar um site (visual) o Flask pode renderizar templates HTML. Para isso você divide em duas pastas: templates, onde são armazenados os arquivos HTML, e static, onde são salvos os arquivos estáticos de CSS, JS e outros.
5. Para funcionalidades adicionais, como bancos de dados, você pode usar extensões como o Flask-SQLAlchemye criar um arquivo models.pypara configurar as tabelas. Para formulários, o Flask-WTFForms é utilizado e um arquivo forms.py deve ser criado.

---

**Templates e Static no Flask**
Estrutura de pastas:
- controllers: onde ficam as rotas (funções) da aplicação
- templates: onde ficam os arquivos HTML que serão renderizados plo Flask
- static: onde ficam os arquivos estáticos (CSS, JS, imagens, etc)
- 
**Por que separar HTML, CSS e JS em pastas diferentes?**
1. Organização do projeto
- Cada tipo de arquivo tem seu lugar definido
- Fica mais fácil encontrar e alterar apenas aquilo que se quer
- Em projetos maiores, essa organização evita bagunça e perda de tempo
- 
2. Separação de responsabilidades
- HTML: estrutura de conteúdo da página
- CSS: aparência (cores, estilos, posicionamento, etc)
- JavaScript: comportamento e interatividade
- 
3. Reuso e manutenção
- Um mesmo CSS pode ser usado em várias páginas
- Se precisar alterar o estilo, basta mudar em um único arquivo
- Isso reduz erros e facilita correções
- 
4. Padrões de mercado
- Frameworks e equipes profissionais seguem essa mesma lógica
- São boas práticas da área
5. Escalabilidade
- Se o projeto crescer a estrutura continua funcionando
- É possível adicionar novas páginas, novos títulos ou scripts "sem misturar tudo".
**O que são Templates no Flask?**
- São modelos de página HTML que podem ser reutilizados
- O flask usar o motor de templates Jinja2
Exemplos de uso:
<h1> Olá, {{ var }}! </h1>
<ul>
    {% for item in lista %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% if usuario_logado %}
    <p>Bem-vindo de volta!</p>
{% else %}
    <p>Faça login para continuar.</p>
{% endif %}
