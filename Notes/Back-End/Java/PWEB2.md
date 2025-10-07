# PWEB2

DOM → componente

WEB → contêiner

Funcionam como um peixe que precisa de um aquário

Browser → http → web conteiner → jpa → eis resources

O request geralmente pega e o response escreve

O método devolve a string e nós fazemos o tratamento → servelet

Nós dizemos o que é e onde buscar, o maven busca e trata → maven

- Agora é o request e o response
- Se segue o padrão do maven vc se livra de fazer configuração

No content-type é onde diz o tipo do arquivo (que está no corpo)

Pode-se colocar conteúdos estáticos

Antes havia uma definição no arquivo xml para dizer o caminho, hoje só colocar na classe

Entrega de uma aplicação web com java → war

Implementação de referência

- JEE e Aplicações Web
    
    World Wide Web e Economia da Informação (Empresas que dominam o âmbito tecnológico detém o poder)
    
    Transformar dados em informações estratégicas
    
    Antes cada parte da empresa possuía seu software, aí surgem os erps (centralizar diversas partes de um sistema) → Plataforma JEE surge aqui, feita em java (objetos e componentes), baseada em módulos, de forma que você vai 
    
    Definir um conjunto de funcionalidades que ajudem a empresas a integrarem e escalarem suas aplicações distribuídas às demandas do negócio 
    
    Fornecer um sistema para seus fornecedores
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image.png)
    
    Pode ser apenas java ou alguma tecnologia de front (html, angular) - clientes
    
    Tem a camada central: coração, a parte para ser web e ejb (java, objeto local que reflete uma cópia do objeto real no servidor - lentos, complexos e não portáveis, obrigava interfaces muitas vezes com métodos vazios)
    
    Persistir o objeto java simples com o hibernate e após isso o JPA
    
    Web Conteiner - como fazer web em java
    
    Gerenciamento de componentes por container: dentro de cada camada tem um container e um componente 
    
    um ejb é um componente (classe, objeto), e para que ele exista e faça seu papel preciso de que fique hospedado num container ejb, esse que vem na forma de um servidor de aplicações e as aplicações java executam dentro dele  
    
    Provavelmente um erp
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image%201.png)
    
    Apenas Web
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image%202.png)
    
    Foco da disciplina
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image%203.png)
    
    Regras de nomeclatura sendo seguidas → java bean. Ex: setNome e getNome
    
    - API de persistência exige que seja um java bean
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image%204.png)
    
    - Não é mais JDBC e sim JPA
    - Servlet pede ao dao a info e depois recebe de volta e passa para a página JSP
    
    Proptocolo http
    
    ![image.png](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/image%205.png)
    
    GET → pede informações, geralmente passa parâmetros para algo ser feito
    
    POST → enviar informações (muda o estadop interno da aplicação)
    

[Spring](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/Spring%2021d2e5a697c38063aff3d6533b1def8c.md)

- Revisão
    
    ### JEE
    
    **Estrutura:**
    Tomcat - container
    Controler - componente
    Bin -
    Objetivo: Serve para criar aplicações web dinâmica com estrutura específica de pastas: Servlet e jsp
    Ferramentas de desenvolvimento:
    
    - maven:
    1. tem estrutura de pastas nas quais as IDEs mantém
    2. cada vez que estabelece uma dependência tem que colocar a referência (artifact id, group id e version) no pom.xml
    - spring:
    1. objetos leves @repository, @service, @controller, @autowired, @configuration
    2. Quero injetar em outro: Java bin, gets e sets, @component
    Injeção de dependência:que fazer uso de um entidade mas sem saber do ciclo de vida dela, de como ela é feita
    Ex: não quero saber como foi feito o repositório, mas preciso de um lugar pra armazenar os dados, injeta um entity manager
    Isso é uma forma de utilizar inversão de controle
    @autowired no set ou no construtor
    Diferença: tem que usar o @controller(aplicação web) e não restController (web service,
    Sistema perguntando a sistema)
    
    Model and view: um tipo de retorno 
    
    Indepotente: Não altera o estado interno da aplicação
    
    mvn wirefire -deploy
    
    Método devirados ou queryByMethodName: pelo nome do método ele faz a consulta
    
    ### Thymeleaf
    
    Engine template html para completar gabaritos html
    
    Forma geral que deve ser completada
    
    Extende o html utilizando pseudo atributos
    
    Conteúdos das tags
    
    Th muda o corpo da tag
    
    Th:text - faz mais sentindo quando tem variável 
    
    Th:action - usa em form, para ter uma ação 
    
    Th:href - links
    
    **Formatadores:** 
    
    #strings, #numbers, #dates, #decimals
    
    Ex: “${#dates.format(u.dataNasc, ‘dd/MM/yyyy)}”
    
    Th:if - renderiza a expressão após a verificação do if 
    
    Th:unless
    
    ge - greater or equal
    
    gt - greater than
    
    Th:switch - para cada case uma nova tag, renderiza a tag se for o case, o default seria *
    
    Th:each - laço de repetição 
    
    Ex: <tr th:each=”f:${funcionario}”
    
        <td>[[${f.nome}]]</td>
    
        <td>[[${f.matricula}]]</td>
    
    $ - retorno um valor
    
    @ - valor preciso (url)
    
    *- referenciar um objeto
    
    Ex: th:object=”${aluno}”
    
           [[*{nome}]]
    
    ~ - referenciar um fragmento
    
    Ex: ~{nomearq :: nometag}
    
          ~{nomearqtag}
    
- Resposta - Prova 1 - ChatGPT
    
    ---
    
    ### **1) Marque V ou F para as afirmativas abaixo (3,0):**
    
    | Afirmativa | Correta? | Justificativa |
    | --- | --- | --- |
    | Um POJO é um objeto Java que necessita de uma superclasse específica | **F** | POJO (Plain Old Java Object) **não precisa de herança ou anotações** especiais. É uma classe simples. |
    | A anotação Spring que define uma classe controladora é a `@SpringController` | **F** | A anotação correta é `@Controller`. Não existe `@SpringController`. |
    | Para adicionar um objeto ao model sempre, em qualquer método da classe controladora, usamos `@ModelAttribute` sobre o método que produz o objeto | **V** | Correto. O método anotado com `@ModelAttribute` é executado antes dos métodos `@RequestMapping`. |
    | Uma das formas de injeção de dependência no Spring é anotar a variável de instância com `@Inject` | **V** | Correto. `@Inject` (da JSR-330) é suportado, embora o mais comum no Spring seja `@Autowired`. |
    | O construtor de uma classe que possui variáveis injetadas não é seguro para realizar inicializações | **F** | O construtor **é o local mais seguro** para inicializações com dependências injetadas. |
    | No Spring MVC com Thymeleaf podemos ou não usar a extensão do nome da página template a ser devolvida | **V** | Correto. Pode-se usar `"home"` ou `"home.html"`, dependendo da configuração. |
    | Seja a expressão JSP-EL `$(a.b)`, `a` pode ser uma lista ou um array, mas não um mapa | **F** | Em JSP-EL, `a` pode ser um mapa, lista ou array. É possível acessar `a.b`, `a["chave"]`, etc. |
    | Para usar a expressão `*(...)` do Thymeleaf numa tag HTML precisamos do `th:object` na tag pai | **V** | Correto. `*{}` depende do contexto de um `th:object`. |
    | Para realizar iterações num template Thymeleaf usamos o pseudo-atributo `th:for` | **F** | O atributo correto é `th:each`, e **não** `th:for`. |
    | Para mapear um método a uma URL usamos a anotação `@RequestMapping`, que pode ter um String como parâmetro para indicar o path da URL que ativa o método | **V** | Correto. Ex: `@RequestMapping("/login")` |
    
    ---
    
    ### **2) Explique o problema que o redirect resolve. (2,0)**
    
    **Problema resolvido pelo redirect:**
    
    Evita o problema do **reenvio de formulário (form resubmission)** quando o usuário aperta F5 após um `POST`. Se não for feito um redirecionamento, o navegador tentará reenviar os dados do formulário.
    
    **Como resolve:**
    
    Ao processar um `POST`, ao invés de devolver diretamente uma página, o servidor envia um **redirect para uma nova URL** (geralmente um `GET`). Assim, se o usuário recarregar a página, ele apenas faz um `GET`, e não reenvia os dados.
    
    **Exemplo com Spring:**
    
    ```java
    @PostMapping("/salvar")
    public String salvar(Entidade entidade) {
        servico.salvar(entidade);
        return "redirect:/lista"; // redireciona para a lista após salvar
    }
    
    ```
    
    ---
    
    ### **3) Explique o que é a injeção de dependência no Spring. (3,0)**
    
    **Injeção de Dependência (DI)** é um princípio onde objetos recebem suas dependências de **fora da classe**, em vez de criarem-nas internamente. Isso aumenta a modularidade e facilita testes.
    
    **O que torna um objeto apto a ser injetado:**
    
    O objeto deve ser um **bean do Spring**, ou seja, precisa estar anotado com uma anotação como:
    
    - `@Component`
    - `@Service`
    - `@Repository`
    - `@Controller`
    
    ou ser registrado manualmente no contexto Spring.
    
    **Formas de injeção no Spring:**
    
    1. **Via construtor (recomendado):**
    
    ```java
    @Service
    public class MeuServico {
        private final MeuRepositorio repo;
    
        public MeuServico(MeuRepositorio repo) {
            this.repo = repo;
        }
    }
    
    ```
    
    1. **Via campo (menos recomendada):**
    
    ```java
    @Autowired
    private MeuRepositorio repo;
    
    ```
    
    1. **Via setter:**
    
    ```java
    @Autowired
    public void setRepo(MeuRepositorio repo) {
        this.repo = repo;
    }
    
    ```
    
    Também pode-se usar `@Inject` ou `@Resource` como alternativas.
    
    ---
    
    ### **4) Uso do `JpaRepository` no Spring (2,0)**
    
    O `JpaRepository` é uma interface do Spring Data JPA que já oferece métodos prontos para acesso ao banco de dados.
    
    **Exemplo de interface:**
    
    ```java
    public interface ProdutoRepository extends JpaRepository<Produto, Long> {
        List<Produto> findByNomeContaining(String nome);
    }
    
    ```
    
    **Tipos de métodos que podemos usar:**
    
    - **Prontos do JpaRepository**:
        - `findAll()`
        - `findById(Long id)`
        - `save(Produto p)`
        - `deleteById(Long id)`
    - **Métodos personalizados por convenção de nome:**
    
    ```java
    List<Produto> findByPrecoGreaterThan(Double preco);
    
    ```
    
    **Uso em serviço ou controlador:**
    
    ```java
    @Service
    public class ProdutoService {
    
        @Autowired
        private ProdutoRepository repo;
    
        public void salvar(Produto produto) {
            repo.save(produto);
        }
    
        public List<Produto> buscarPorNome(String nome) {
            return repo.findByNomeContaining(nome);
        }
    }
    
    ```
    
    ---
    
- Resposta - Prova 2 - ChatGPT
    
    ---
    
    ### **1) Marque V ou F para as afirmativas abaixo (4,0):**
    
    | Afirmativa | Correta? | Justificativa |
    | --- | --- | --- |
    | Um POJO é um objeto Java que necessita de uma superclasse específica | **F** | POJO = Plain Old Java Object → classe simples, **sem heranças ou anotações específicas**. |
    | A anotação Spring que define uma classe controladora é a `@SpringController` | **F** | A correta é `@Controller`. `@SpringController` **não existe**. |
    | Para adicionar um objeto ao model sempre, em qualquer método da classe controladora, usamos `@ModelAttribute` sobre o método que produz o objeto | **V** | Corretíssimo. O método com `@ModelAttribute` executa antes de todos os métodos `@RequestMapping`. |
    | A forma de injeção de dependência no Spring é anotar a variável de instância com `@Inject` | **V** | Embora `@Autowired` seja mais comum no Spring, `@Inject` também é **válido e funcional**. |
    | O construtor de uma classe que possui variáveis injetadas não é seguro para realizar inicializações | **F** | Pelo contrário: **é o mais seguro**. Evita problemas de dependência nula. |
    | No Spring MVC com Thymeleaf os templates HTML não são URL endereçáveis por si só | **F** | Falso. Os templates podem sim ser mapeados e acessados por URL via `@GetMapping`, etc. |
    | Seja a expressão Thymeleaf `${a.b}`, `a` pode ser uma lista ou um array, mas não um mapa | **F** | Falso. `a` **pode ser mapa** também. Ex: `${mapa["chave"]}` ou `${mapa.chave}`. |
    | Para usar a expressão `*{...}` do Thymeleaf numa tag HTML precisamos do `th:object` na tag pai | **V** | Correto! `*{}` é relativo ao `th:object`. |
    | Para realizar iterações num template Thymeleaf usamos o pseudo-atributo `th:forEach` | **F** | O correto é `th:each`, não existe `th:forEach`. |
    
    ---
    
    ### **2) Controlador e templates do Spring MVC e Thymeleaf (3,0)**
    
    **Controlador:**
    
    ```java
    @Controller
    public class ImcController {
    
        @GetMapping("/form")
        public String exibirFormulario(Model model) {
            model.addAttribute("pessoa", new Pessoa());
            return "formulario";
        }
    
        @PostMapping("/imc")
        public String calcularImc(@ModelAttribute Pessoa pessoa, RedirectAttributes redirectAttributes) {
            double alturaM = pessoa.getAltura() / 100.0; // altura em cm → metros
            double imc = pessoa.getPeso() / (alturaM * alturaM);
            redirectAttributes.addFlashAttribute("nome", pessoa.getNome());
            redirectAttributes.addFlashAttribute("imc", imc);
            return "redirect:/resultado";
        }
    
        @GetMapping("/resultado")
        public String exibirResultado() {
            return "resultado";
        }
    }
    
    ```
    
    **Classe Pessoa:**
    
    ```java
    public class Pessoa {
        private String nome;
        private double peso;
        private double altura;
    
        // getters e setters
    }
    
    ```
    
    **formulario.html (Thymeleaf):**
    
    ```html
    <!DOCTYPE html>
    <html xmlns:th="http://www.thymeleaf.org">
    <head><title>Formulário IMC</title></head>
    <body>
      <form th:action="@{/imc}" th:object="${pessoa}" method="post">
        Nome: <input type="text" th:field="*{nome}" /><br>
        Peso (kg): <input type="number" step="0.01" th:field="*{peso}" /><br>
        Altura (cm): <input type="number" step="0.1" th:field="*{altura}" /><br>
        <button type="submit">Calcular IMC</button>
      </form>
    </body>
    </html>
    
    ```
    
    **resultado.html:**
    
    ```html
    <!DOCTYPE html>
    <html xmlns:th="http://www.thymeleaf.org">
    <head><title>Resultado</title></head>
    <body>
      <p th:text="'Olá ' + ${nome} + ', seu IMC é: ' + ${imc}"></p>
    </body>
    </html>
    
    ```
    
    ---
    
    ### **3) Qual forma de definir uma path variable está correta no Spring? (1,0)**
    
    **Alternativa correta:**
    
    ✅ **Letra (a)**
    
    ```java
    @RequestMapping("/user/{id}")
    public String handleRequest(@PathVariable("id") String userId, Model map) {
        // uso do userId
        return "algumaPagina";
    }
    
    ```
    
    > A chave é o uso de /user/{id} com @PathVariable("id").
    > 
    
    ---
    
    ### **4) Tipos de consultas no `JpaRepository` (2,0)**
    
    O `JpaRepository` oferece dois tipos principais de consultas:
    
    ### a) **Consultas automáticas por nome de método:**
    
    O Spring interpreta o nome do método e gera a SQL automaticamente.
    
    ```java
    List<Cliente> findByNome(String nome);
    List<Produto> findByPrecoGreaterThan(Double preco);
    
    ```
    
    ### b) **Consultas com anotação `@Query`:**
    
    Para definir JPQL ou SQL manualmente.
    
    ```java
    @Query("SELECT p FROM Produto p WHERE p.preco < :precoMax")
    List<Produto> buscarProdutosBaratos(@Param("precoMax") double precoMax);
    
    ```
    
    ### c) **Consultas nativas (opcional):**
    
    ```java
    @Query(value = "SELECT * FROM produto WHERE categoria = ?1", nativeQuery = true)
    List<Produto> buscarPorCategoria(String categoria);
    
    ```
    
    ---
    
- Respostas detalhadas questões V e F
    
    ## ✅ **QUESTIONÁRIO 1:**
    
    ### **1.** Um POJO é um objeto Java que necessita de uma superclasse específica.
    
    **❌ Falso.**
    
    Um **POJO (Plain Old Java Object)** é um objeto Java simples, sem herança obrigatória, sem anotações específicas, e sem necessidade de implementar interfaces. Ele **não precisa de nenhuma superclasse**. Exemplo:
    
    ```java
    public class Pessoa {
        private String nome;
        private int idade;
        // getters e setters
    }
    
    ```
    
    ---
    
    ### **2.** A anotação Spring que define uma classe controladora é a `@SpringController`.
    
    **❌ Falso.**
    
    A anotação correta é `@Controller` (ou `@RestController`). **Não existe** `@SpringController` no Spring Framework.
    
    ```java
    @Controller
    public class MeuControlador { }
    
    ```
    
    ---
    
    ### **3.** Para adicionar um objeto ao model sempre, em qualquer método da classe controladora, usamos `@ModelAttribute` sobre o método que produz o objeto.
    
    **✅ Verdadeiro.**
    
    Um método com `@ModelAttribute` irá adicionar o objeto retornado ao `Model` **antes da execução de qualquer método mapeado** da classe:
    
    ```java
    @ModelAttribute("usuario")
    public Usuario usuario() {
        return new Usuario();
    }
    
    ```
    
    ---
    
    ### **4.** Uma das formas de injeção de dependência no Spring é anotar a variável de instância com `@Inject`.
    
    **✅ Verdadeiro.**
    
    `@Inject` vem da especificação JSR-330 (javax.inject.Inject) e é **totalmente compatível com o Spring**, funcionando como alternativa ao `@Autowired`.
    
    ---
    
    ### **5.** O construtor de uma classe que possui variáveis injetadas não é seguro para realizar inicializações.
    
    **❌ Falso.**
    
    Injeção via construtor é **a forma mais recomendada** no Spring. Ela garante imutabilidade e que as dependências sejam obrigatórias:
    
    ```java
    @Service
    public class ProdutoService {
        private final ProdutoRepository repository;
    
        public ProdutoService(ProdutoRepository repository) {
            this.repository = repository;
        }
    }
    
    ```
    
    ---
    
    ### **6.** No Spring MVC com Thymeleaf podemos ou não usar a extensão do nome da página template a ser devolvida.
    
    **✅ Verdadeiro.**
    
    Quando retornamos uma view, **não precisamos colocar a extensão** `.html`. O `ViewResolver` configurado no Spring assume isso.
    
    ```java
    return "pagina"; // Thymeleaf buscará "pagina.html" automaticamente
    
    ```
    
    ---
    
    ### **7.** Seja a expressão JSP-EL `${a.b}`, `a` pode ser uma lista ou array, mas não um mapa.
    
    **❌ Falso.**
    
    No JSP EL, `a` **pode ser um mapa**. A expressão `${a.b}` acessa `a.get("b")` se `a` for `Map`.
    
    ---
    
    ### **8.** Para usar a expressão `{}` do Thymeleaf numa tag HTML, precisamos do `th:object` na tag pai.
    
    **✅ Verdadeiro.**
    
    `th:object` define o objeto base do formulário, permitindo o uso de `*{campo}` para acessar propriedades:
    
    ```html
    <form th:object="${usuario}">
        <input th:field="*{nome}" />
    </form>
    
    ```
    
    ---
    
    ### **9.** Para realizar iterações em um template Thymeleaf usamos o pseudo-atributo `th:forEach`.
    
    **❌ Falso.**
    
    O atributo correto é `**th:each**`. Não existe `th:forEach` no Thymeleaf.
    
    ```html
    <tr th:each="produto : ${produtos}">
        <td th:text="${produto.nome}"></td>
    </tr>
    
    ```
    
    ---
    
    ### **10.** Para mapear um método a uma URL usamos a anotação `@RequestMapping`, que pode ter uma String como parâmetro para indicar o path da URL.
    
    **✅ Verdadeiro.**
    
    `@RequestMapping("/caminho")` ou `@GetMapping("/caminho")` indicam a URL que deve acionar aquele método.
    
    ---
    
    ## ✅ **QUESTIONÁRIO 2:**
    
    ### **1.** Um POJO é um objeto Java que necessita de uma superclasse específica.
    
    **❌ Falso.**
    
    Mesmo caso da questão anterior: POJOs não precisam herdar de nenhuma classe específica.
    
    ---
    
    ### **2.** A anotação Spring que define uma classe controladora é `@SpringController`.
    
    **❌ Falso.**
    
    A anotação correta é `@Controller`. `@SpringController` **não existe**.
    
    ---
    
    ### **3.** Para adicionar um objeto ao model sempre, em qualquer método da classe controladora, usamos `@ModelAttribute`.
    
    **✅ Verdadeiro.**
    
    Como explicado antes, é a forma correta de adicionar atributos globais ao `Model`.
    
    ---
    
    ### **4.** A forma de injeção de dependência no Spring é anotar a variável de instância com `@Inject`.
    
    **✅ Verdadeiro.**
    
    `@Inject` é suportado no Spring como forma de injeção de dependência (alternativa ao `@Autowired`).
    
    ---
    
    ### **5.** O construtor de uma classe com variáveis injetadas não é seguro para inicializações.
    
    **❌ Falso.**
    
    Pelo contrário: é **a maneira mais segura** de garantir que todas as dependências estejam disponíveis.
    
    ---
    
    ### **6.** No Spring MVC com Thymeleaf os templates HTML não são URL endereçáveis por si sós.
    
    **✅ Verdadeiro.**
    
    Templates HTML do Thymeleaf são processados pelo Spring — **não são acessados diretamente por URL**.
    
    ---
    
    ### **7.** A expressão Thymeleaf `${a.b}`, `a` pode ser uma lista ou array, mas não um mapa.
    
    **❌ Falso.**
    
    Como no primeiro questionário, `a` pode ser **qualquer estrutura**, inclusive `Map`.
    
    ---
    
    ### **8.** Para usar `{}` do Thymeleaf, precisamos do `th:object` na tag pai.
    
    **✅ Verdadeiro.**
    
    Sem `th:object`, `*{}` não sabe qual objeto está referenciando.
    
    ---
    
    ### **9.** Para realizar iterações no template Thymeleaf usamos `th:forEach`.
    
    **❌ Falso.**
    
    O correto é `th:each`.
    
    ---
    
    ### **10.** Para mapear um método a uma URL usamos `@RequestMapping`, com um `String value` indicando o path.
    
    **✅ Verdadeiro.**
    
    Correto. Pode ser usado com `@RequestMapping("/exemplo")` ou `@GetMapping`.
    
    ---
    

Comando para rodar spring no terminal: **mvn spring-boot:run**

[Thymeleaf](PWEB2%201dd2e5a697c380b68840ca0391c1f15b/Thymeleaf%2023a2e5a697c380dd8a0cd52af83d556e.md)