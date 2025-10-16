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

**MVC** é um padrão de arquitetura de software que divide uma aplicação em três camadas interconectadas: Model (Modelo), View (Visão) e Controller (Controlador). Essa separação de responsabilidades facilita a manutenção, o reuso de código e a escalabilidade do sistema. O modelo gerencia os dados e a lógica de negócio, a visão cuida da apresentação ao usuário e o controlador intermedia as requisições do usuário e as interações com o modelo e a visão. 
Camadas do MVC

Model (Modelo): Gerencia os dados e a lógica de negócio da aplicação. Ele interage com o banco de dados, realiza operações e fornece os dados necessários quando solicitados pelo Controller.

View (Visão): Responsável pela apresentação dos dados ao usuário. Ela não contém lógica de negócio, mas recebe as informações do Controller e as exibe de forma visual. 

Controller (Controlador): Atua como intermediário, recebendo as requisições do usuário. Ele processa essas requisições, delega as tarefas ao Model e decide qual View deve ser apresentada ao usuário. 
