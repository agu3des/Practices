# DTO

A arquitetura de um projeto em Java geralmente segue o padrão **MVC (Model-View-Controller)** e algumas camadas adicionais para organização, como **config, response, repositories e services**. Vamos explorar cada uma dessas camadas e seu propósito:

---

### **Config (Configurações)**

**Responsável por:** Arquivos de configuração da aplicação, como conexão com o banco de dados, segurança e outras configurações globais.

**Exemplos de uso:**

- Configuração do Spring Security
- Configuração do banco de dados (DataSource, JPA, Hibernate)
- Configuração do CORS
- Configuração de Beans

**Exemplo:**

```java
@Configuration //Quando a aplicacao iniciar essas configuracoes devem ser carregadas
public class CorsConfig {
    @Bean //o metodo retorna um objeto que será gerenciado elo spring
    public WebMvcConfigurer corsConfigurer() { //aplicar as regras de CORS nas requisicoes HTTP
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**").allowedOrigins("*").allowedMethods("GET", "POST", "PUT", "DELETE");
            }
        };
    }
}

```

---

### **Controllers (Controladores)**

**Responsável por:** A camada de entrada da aplicação, ou seja, a interface entre o cliente (frontend, mobile, API externa) e a lógica de negócio.

**Função:**

- Recebe as requisições HTTP (GET, POST, PUT, DELETE)
- Processa os dados recebidos (validação, autenticação, etc.)
- Encaminha a solicitação para a camada de serviço (`Service`)
- Retorna a resposta para o cliente

**Exemplo:**

```java
@RestController
@RequestMapping("/empregados")
public class EmpregadoController {

    @Autowired
    private EmpregadoService empregadoService;

    @GetMapping("/{id}")
    public ResponseEntity<EmpregadoResponse> getEmpregadoById(@PathVariable Long id) {
        EmpregadoResponse response = empregadoService.getEmpregadoById(id);
        return ResponseEntity.ok(response);
    }
}

```

---

### **Models (Modelos ou Entidades)**

**Responsável por:** Representar as tabelas do banco de dados como objetos Java.

**Função:**

- Mapeia os atributos das tabelas do banco
- Define as relações entre tabelas
- Contém anotações do JPA (`@Entity`, `@Table`, `@Column`, etc.)

**Exemplo:**

```java
@Entity
@Table(name = "empregado")
public class Empregado {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "primeiro_nome", nullable = false)
    private String primeiroNome;

    @Column(name = "salario")
    private Double salario;

    @ManyToOne
    @JoinColumn(name = "cod_depto")
    private Departamento departamento;
}

```

---

### **Response (DTO - Data Transfer Object)**

**Responsável por:** Definir a estrutura da resposta que será enviada ao cliente.

**Função:**

- Evitar expor a estrutura completa da entidade
- Filtrar informações sensíveis
- Personalizar os dados da resposta

**Exemplo:**

```java
public class EmpregadoResponse {
    private String nomeCompleto;
    private String cargo;
    private Double salario;

    public EmpregadoResponse(Empregado empregado) {
        this.nomeCompleto = empregado.getPrimeiroNome();
        this.cargo = empregado.getCargo();
        this.salario = empregado.getSalario();
    }
}

```

---

### **Repositories (Repositórios)**

**Responsável por:** A camada de acesso ao banco de dados.

**Função:**

- Fazer operações como `findById`, `save`, `delete`, `findAll`, etc.
- Utiliza Spring Data JPA para simplificar as consultas

**Exemplo:**

```java
@Repository
public interface EmpregadoRepository extends JpaRepository<Empregado, Long> {
    List<Empregado> findByCargo(String cargo);
}

```

---

### **Services (Serviços)**

**Responsável por:** A lógica de negócio da aplicação.

**Função:**

- Implementa regras de negócio
- Realiza validações
- Interage com os `Repositories`
- Converte `Models` em `Response`

**Exemplo:**

```java
@Service
public class EmpregadoService {

    @Autowired
    private EmpregadoRepository empregadoRepository;

    public EmpregadoResponse getEmpregadoById(Long id) {
        Empregado empregado = empregadoRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Empregado não encontrado"));

        return new EmpregadoResponse(empregado);
    }
}

```

---

## **Resumo Geral**

| Camada | Responsável por |
| --- | --- |
| **Config** | Configuração da aplicação (segurança, CORS, banco de dados) |
| **Controllers** | Lidar com requisições HTTP e direcionar para a camada de serviço |
| **Models** | Representar as entidades do banco de dados |
| **Response (DTO)** | Definir o formato dos dados retornados para o cliente |
| **Repositories** | Interagir com o banco de dados (consultas, inserções, remoções) |
| **Services** | Implementar a lógica de negócio da aplicação |

## **Fluxo Completo de uma Requisição**

1. **cliente** (navegador, app, frontend) faz uma requisição para `GET /empregados/{id}`.
2. **Controller** recebe a requisição e chama o **Service**.
3. **Service** busca os dados no **Repository**.
4. **Repository** acessa o banco de dados e retorna um **Model**.
5. **Service** converte o **Model** para um **Response (DTO)**.
6. **Controller** retorna o **Response** ao cliente.