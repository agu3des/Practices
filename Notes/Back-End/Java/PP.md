# PP

https://refactoring.guru/design-patterns

- **Simple Factory**
    
    designa uma classe a definição de um método de criação que retorna qual produto instanciar de acordo com um argumento de entrada
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image.png)
    
    Composto por uma fábrica concreta, essa que não herda de outra camada de abstração
    
    Método de criação normalmente é definido como um método estático
    
    **OBS:** caso se extraia subclasses de uma fábrica simples a solução migra para um Factory Method clássico ****
    
    Estrutura do padrão
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%201.png)
    
    1. Definir a interface (e métodos) que representam a abstração para os produtos concretos
    2. As classes de produtos concretos implementam a interface AbstractProduct
    3. A fábrica simples é responsável pela lógica de criação de todas as instâncias de produtos disponíveis de acordo com o argumento de entrada. 
        1. O tipo de retorno é a interface.
        2. A classe cliente utiliza a fábrica simples para solicitar a criação dos objetos produto de que necessita, invocando o método create().
        3. A classe cliente não tem ciência de como o produto é criado e não está acoplada a nenhum produto concreto.
    4. Centraliza o código de criação dos objetos em uma única classe, o que pode vir a violar o princípio de responsabilidade única (a fábrica pode vir a crescer para incluir muitos tipos diferentes de objetos).
    5. Viola o princípio de open/close, já que caso seja necessário criar uma novo tipo de objeto será necessário alterar a lógica da fábrica para incluir essa nova lógica de criação. (pode se resolver trocando para Factory Method)
- **Null Object**
    
    null, None ou nil são termos que indicam a situação de indefinição/ausência de uma informação
    
    Em linguagens OO, a tentativa de acessar um método/atributo inexistente, gera uma exceção (NullPointerException - Java)
    
    ```java
    //Para resolver isso utilizamos: 
    if (veiculo != null){
    	veiculo.acelerar()
    }
    ```
    
    Deve-se utilizar a checagem de algo igual a null em várias partes do projeto, essas condicionais de teste evitam essa exceção que pode vir a causar erros em tempo de execução.
    
    É um padrão de projeto que encapsula a indisponibilidade de um objeto oferecendo uma alternativa “substituível ” com comportamento padrão de não fazer nada (objeto nulo) .
    
    O código cliente poderá funcionar mesmo recebendo um objeto nulo.
    
    Exemplo de padrão de reuso por herança
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%202.png)
    
    O método isNull() é sugerido para identificação do objeto concreto.
    
    O objeto real é a classe que corresponde ao objeto dependente, cujas instâncias fornecem o comportamento que o cliente espera.
    
    A classe NullObject fornece uma interface idêntica ao objeto concreto, de modo que um objeto nulo possa ser substituído por um objeto real, quando não existir.
    
    Objetos desta classe não contém funcionalidades (comportamento neutro), porém implementa todas as operações definidas pela classe abstrata.
    
    O cliente pode utilizar uma fábrica que ficará com a responsabilidade de retornar o objeto real ou o nulo.
    
    Elimina necessidade de verificações de referências nulas no código, e reduz a possibilidade de erros por causa dessas referências.
    
    Excessivas classes para a representação de um objeto nulo dificulta o entendimento e aumento o uso da memória.
    
    1. O método isNull() retorna true para o NullObject e false para um objeto da classe real.
    2. Implementar método, classe ou solução que tenha a responsabilidade de recuperar a classe real, de forma parametrizada. Se a chave não for encontrada, deve retornar um objeto nulo.
    3. Nos locais que a referência para o objeto da classe real é comparada com null substitui com a solução que invoca a criação/recuperação do objeto da classe real.
    4. A classe cliente terá o código que vai interagir com a criação/recuperação do objeto real. 
    5. Geralmente implementada como um Singleton. 
- **Strategy**
    
    Padrão comportamental 
    
    Múltiplos algoritmos implementados em classes separadas → estratégias
    
    Classe original → contexto → deve ter um campo para armazenar uma referência para uma dessas estratégias
    
    Utiliza de uma interface genérica que expõe o único método para acionar o algoritmo encapsulado dentro da estratégia escolhida
    
    Realizarem a mesma tarefa de forma diferente → faça algo específico de diversas maneiras
    
    Objetos intercambiáveis
    
    Define uma estratégia para resolver determinado problema durante a execução de um programa
    
    Composição, para reuso de código
    
    O cliente que escolhe qual vai ser a implementação real, ou seja, a estratégia
    
    Ex: gps → planejamento automático de rotas → cada algoritmo de roteamento tem seu modo
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%203.png)
    
    Quando usar:
    
    - Diferentes variantes de um algoritmo dentro de um objeto e ser capaz de trocar em tempo de execução
    - Alteração indireta no comportamento de um objeto durante a execução ao associá-lo com diferentes sub-objetos
    - Muitas classes parecidas diferindo apenas na forma que executam um comportamento → extrair para uma hierarquia separada
    - Separar lógica do negócio de detalhes da implementação do algoritmo
    - Open/Close
    
    1. Interface estratégia comum a todas as estratégias concretas. Ela declara um método abstrato que o contexto usa para rodar a estratégia
    2. As estratégias concretas implementam diferentes variações de um algoritmo que o contexto usa
    3. O contexto mantém uma referência (atributo) para um objeto da estratégia concreta por meio da interface → é a raiz do padrão → não sabe qual estratégia está usando
    4. O cliente cria uma estratégia concreta específica e repasse à classe contexto por meio de um método setter 
    5. **O cliente pode mudar a estratégia associada ao contexto durante a execução**
    
- **Bridge**
    
    Padrão estrutural
    
    Dividir uma classe grande em duas hierarquias separadas: abstração e implementação
    
    Desenvolvê-las separadamente
    
    Abstração: camada de controle de alto nível , não deve fazer nenhum tipo de trabalho por conta própria, mas sim delegar o trabalho para a camada de implementação
    
    A interface de Implementação declara os métodos em comum para todas as implementações concretas
    
    A abstração só irá se comunicar com uma implementação concreta por meio dos métodos da interface
    
    As implementações concretas contém códigos específicos para os métodos abstratos
    
    Abstrações refinadas podem ser especializadas para fornecer variantes para controle da lógica
    
    A classe cliente interage apenas com a abstração, liga o objeto da abstração com um dos objetos concretos de implementação
    
    Trocar implementações em tempo de execução
    
    open/closed e single responsability 
    
    1. Defina a abstração e a implementação
    2. Quais as operações o cliente precisa e defina na classe abstração base
    3. Declare as operações que a abstração precisa na interface geral de implementação
    4. Classes concretas que sigam a interface de implementação
    5. Na classe de abstração deve ter um campo de referência para o tipo de implementação
    
    Principal objetivo é desacoplar a abstração da implementação
    
    Baseado em composição
    
- **Template Method**
    
    Padrão comportamental que define a estrutura de passos de um algoritmo, mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura.
    
    Utiliza hook methods como técnica base.
    
    Aplicável quando se deseja definir um algoritmo geral para uma série de passos para cumprir um requisito da aplicação.]
    
    Deve ser feita de forma que os passos sejam facilmente substituídos.
    
    Ex: algoritmo gera gráfico de barras a partir de dados extraídos de PDF, Excel, CSV 
    
    A lógica de cada subclasse é “injetada” na lógica padrão da superclasse.
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%204.png)
    
    Um classe abstrata define métodos que agem como etapas de um algoritmo, bem como o próprio método padrão que chama esses métodos em uma ordem específica.
    
    Os passos podem ser abstratos ou ter alguma implementação padrão.
    
    As etapas abstratas definem os hook methods (técnica para permitir a extensão de comportamento).
    
    As classes concretas podem sobrescrever todas as etapas mas jamais o método padrão (template).
    
    A classe cliente instancia a classe concreta, quando o metodoTemplate() for invocado, ele vai executar a lógica seguindo o comportamento que foi definido pela lógica da classe concreta  
    
    ```java
    AbstractClass ac = new
    ConcreteClass1();
    ac.templateMethod()
    ```
    
    Quando quiser deixar os clientes estenderem apenas etapas particulares do algoritmo, mas não o algoritmo e sua estrutura
    
    Permite que transforme o algoritmo “rígido” em uma série de etapas individuais que podem facilmente ser estendidas por subclasses enquanto ainda mantém intacta a estrutura definida em uma superclasse
    
    Para cada variação crie uma nova subclasse concreta.  
    
    É baseado em herança, funciona em nível de classe (é estático)
    
    OBS: o factory method é uma especialização do Template Method ou servir como uma etapa em um grande
    
- **Factory Method**
    
    Fornece uma interface para criar objetos em uma superclasse e deixa que as subclasses decidam qual o tipo de objeto concreto será instanciado
    
    Substitua chamadas diretas de construção de objetos (usando o new) para um método fábrica
    
    O objeto retornado pelo método de fábrica é chamado de “produto”
    
    Pode ser visto como uma especialização do Template Method
    
    O método fábrica deve ser abstrato para forçar as subclasses a implementarem suas próprias versões do método
    
    Criadores concretos implementam o método fábrica base para criar e retornar um tipo diferente de produto concreto.
    
    O método de fábrica atua sob o princípio do método hook, porém, retornando o objeto produto para desempenhar seu papel
    
    Desacoplar a superclasse da criação de uma dependência.
    
    Caso uma nova instância da dependência precise ser utilizada pela superclasse, basta criar uma nova subclasse que retorne aquela instância.
    
    1. Classe criadora não souber as dependências exatas 
    2. Separa o código de construção do produto do código que utiliza o produto
    3. Uma classe deseja que suas subclasses especifiquem os objetos criados
    4. open/closed e single responsability
- **Revisão - Prova**
    
    ![1000101675.jpg](PP%201fd2e5a697c380bf90ccf97769a9f044/1000101675.jpg)
    
    ![1000101677.jpg](PP%201fd2e5a697c380bf90ccf97769a9f044/1000101677.jpg)
    
    | Critério | Simple Factory | Null Object | Strategy | Bridge | Template Method | Factory Method |
    | --- | --- | --- | --- | --- | --- | --- |
    | **Objetivo** | Encapsular criação de objetos | Evitar uso de `null`, fornecendo comportamento padrão | Encapsular algoritmos intercambiáveis | Separar abstração da implementação | Definir esqueleto de algoritmo, delegando etapas para subclasses | Delegar a criação de objetos para subclasses |
    | **Tipo** | Criacional | Comportamental | Comportamental | Estrutural | Comportamental | Criacional |
    | **Forma de instanciação** | Através de um método estático | Instância concreta de uma classe nula | Estratégias são injetadas ou escolhidas em tempo de execução | Abstração e implementação instanciadas separadamente | Instanciado pela subclasse ou diretamente | Método abstrato que retorna instância em subclasses |
    | **Injeção de dependência** | Possível, mas não essencial | Normalmente injetado como padrão ao invés de `null` | Essencial para alternar estratégias | Sim, separa implementações com injeção de dependência | Não necessariamente | Sim, com classes concretas retornando instâncias |
    | **Herança** | Normalmente não usa, mas pode ter hierarquia de produtos | Pode ou não usar herança, depende da implementação | Interface comum entre estratégias | Interface (ou classe abstrata) para abstração e implementação | Base usa herança para delegar comportamento | Requer herança para especialização do método fábrica |
    | **Extensibilidade** | Média – requer alterações na fábrica para adicionar novos tipos | Alta – novo comportamento sem alterar lógica principal | Alta – fácil adicionar novas estratégias | Alta – novas abstrações e implementações são independentes | Média – exige criação de nova subclasse | Alta – novas fábricas criadas por subclasses |
    | **Aplicabilidade** | Quando a criação de objetos deve ser centralizada | Quando se deseja evitar verificações de `null` frequentes | Quando há múltiplos comportamentos intercambiáveis | Quando abstração e implementação variam independentemente | Quando algoritmos seguem mesma estrutura geral | Quando classes delegam a criação de objetos a subclasses |
    | **Vantagens** | Centraliza lógica de criação, oculta complexidade | Código mais limpo, evita `NullPointerException` | Alta flexibilidade e reutilização | Flexibilidade para mudar abstração e implementação | Reuso de código comum entre algoritmos | Promove encapsulamento e desacoplamento |
    | **Desvantagens** | Pouco flexível para adição de novos produtos | Pode mascarar erros lógicos | Aumenta número de classes | Pode introduzir complexidade extra | Rígido se mudanças na estrutura forem necessárias | Requer mais classes e estruturação |
    | **Diferenças principais** | Simples e direto, apenas criação | Lida com ausência de objetos com comportamento padrão | Troca de comportamento sem alterar cliente | Divide e abstrai múltiplas variações | Algoritmo fixo com passos customizáveis | Subclasse decide qual objeto instanciar |
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%205.png)
    

---

- 🔹 **1. Abstract Factory**
    - **Tipo:** Criacional
    - **Objetivo:** Fornece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas.
    - **Herança:** Utiliza herança para definir interfaces de criação e composição para fábricas concretas.
    - **Injeção de Dependência:** Facilita ID ao permitir a troca de famílias inteiras de objetos.
    - **Vantagens:**
        - Consistência entre objetos relacionados
        - Isola a criação de objetos do cliente
    - **Desvantagens:**
        - Complexidade aumenta com o número de produtos
        - Difícil adicionar novos produtos
    - **Formas de Instanciação:** Interface de fábrica + classes concretas
    - **Princípios:**
        - ✅ Princípio da Responsabilidade Única (SRP)
        - ✅ Aberto/Fechado (OCP)
        - ❌ Pode violar ISP e DIP se mal utilizado
    
    ### ✅ Código explicativo:
    
    ```java
    interface GUIFactory {
        Button createButton();
        Checkbox createCheckbox();
    }
    
    ```
    
    Duas famílias de produtos: `Button` e `Checkbox`. A fábrica (`GUIFactory`) cria essas famílias sem expor classes concretas.
    
    ```java
    class WindowsFactory implements GUIFactory {
        public Button createButton() { return new WindowsButton(); }
        public Checkbox createCheckbox() { return new WindowsCheckbox(); }
    }
    
    ```
    
    Fábrica concreta (`WindowsFactory`) define como criar os produtos da família Windows.
    
    ### ✅ Por que é **Abstract Factory**:
    
    - Cria famílias de objetos relacionados (`Button`, `Checkbox`) **sem acoplamento a implementações específicas**.
    - O cliente (`Application`) não precisa saber se está usando Windows ou Mac.
    - Isola a lógica de criação, respeitando o princípio da **inversão de dependência**.
- 🔹 **2. Observer**
    - **Tipo:** Comportamental
    - **Objetivo:** Permite que objetos observadores sejam notificados quando o estado de outro objeto (sujeito) mudar.
    - **Herança:** Interfaces para sujeito e observadores
    - **Injeção de Dependência:** Observadores são injetados no sujeito, promovendo baixo acoplamento.
    - **Vantagens:**
        - Facilita comunicação reativa
        - Baixo acoplamento entre sujeito e observadores
    - **Desvantagens:**
        - Ordem de notificação pode ser imprevisível
        - Pode causar problemas de desempenho
    - **Formas de Instanciação:** Registro dinâmico dos observadores
    - **Princípios:**
        - ✅ Aberto/Fechado (OCP)
        - ✅ Inversão de Dependência (DIP)
        - ✅ Princípio da Responsabilidade Única (SRP)
    
    ### ✅ Código explicativo:
    
    ```java
    interface Observer {
        void update(String message);
    }
    
    ```
    
    Define a interface comum para todos que desejam receber atualizações.
    
    ```java
    class NotificationService {
        private List<Observer> observers = new ArrayList<>();
    
        void subscribe(Observer o) { observers.add(o); }
        void notifyAllObservers(String msg) {
            for (Observer o : observers) o.update(msg);
        }
    }
    
    ```
    
    O sujeito (`NotificationService`) mantém uma lista de observadores e os **notifica quando algo muda**.
    
    ### ✅ Por que é **Observer**:
    
    - Separa **quem produz o evento (sujeito)** de **quem reage a ele (observadores)**.
    - Permite **registro e notificação dinâmica**.
    - Promove **baixo acoplamento**, pois o sujeito não conhece detalhes dos observadores.
- 🔹 **3. State**
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%206.png)
    
    - **Tipo:** Comportamental
    - **Objetivo:** Permite que um objeto altere seu comportamento quando seu estado interno muda.
    - **Herança:** Interface de estado + classes concretas
    - **Injeção de Dependência:** Pode usar ID para alternar dinamicamente entre estados.
    - **Vantagens:**
        - Clareza de código para múltiplos estados
        - Evita grandes blocos de `if/else`
    - **Desvantagens:**
        - Muitas classes para cada estado
    - **Formas de Instanciação:** Estados instanciados dinamicamente ou singleton
    - **Princípios:**
        - ✅ Aberto/Fechado (OCP)
        - ✅ SRP
        - ✅ DIP
    
    ### ✅ Código:
    
    ```java
    interface State {
        void handle();
    }
    
    class HappyState implements State {
        public void handle() { System.out.println("Estou feliz!"); }
    }
    
    class SadState implements State {
        public void handle() { System.out.println("Estou triste..."); }
    }
    
    class Person {
        private State state;
    
        public void setState(State s) { this.state = s; }
        public void behave() { state.handle(); }
    }
    
    class Main {
        public static void main(String[] args) {
            Person p = new Person();
            p.setState(new HappyState());
            p.behave();  // Output: Estou feliz!
    
            p.setState(new SadState());
            p.behave();  // Output: Estou triste...
        }
    }
    
    ```
    
    ### ✅ Por que é **State**:
    
    - O comportamento de `Person` muda conforme seu **estado interno** (`HappyState`, `SadState`).
    - O padrão encapsula os estados em **classes separadas**, evitando `if-else`.
    - Facilita **manutenção e adição de novos estados** sem alterar a classe principal.
- 🔹 **4. Chain of Responsibility**
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%207.png)
    
    - **Tipo:** Comportamental
    - **Objetivo:** Passa uma solicitação por uma cadeia de manipuladores até que ela seja tratada.
    - **Herança:** Interface comum para os manipuladores
    - **Injeção de Dependência:** Permite montar a cadeia externamente
    - **Vantagens:**
        - Flexível e extensível
        - Evita acoplamento direto entre remetente e receptor
    - **Desvantagens:**
        - Pode ser difícil depurar
        - Nem sempre uma solicitação será tratada
    - **Formas de Instanciação:** Encadeamento manual de objetos
    - **Princípios:**
        - ✅ OCP, DIP
        - ✅ SRP
        - ❌ LSP se um manipulador falha silenciosamente
    
    ### ✅ Exemplo:
    
    ```java
    abstract class Handler {
        protected Handler next;
        public void setNext(Handler next) { this.next = next; }
        public abstract void handle(String request);
    }
    
    class AuthHandler extends Handler {
        public void handle(String request) {
            if (request.equals("auth")) {
                System.out.println("Autenticado.");
            } else if (next != null) {
                next.handle(request);
            }
        }
    }
    
    class LogHandler extends Handler {
        public void handle(String request) {
            System.out.println("Log registrado para: " + request);
            if (next != null) next.handle(request);
        }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            Handler auth = new AuthHandler();
            Handler log = new LogHandler();
            auth.setNext(log);
    
            auth.handle("auth"); // Autenticado + log
            auth.handle("logout"); // Apenas log
        }
    }
    
    ```
    
    ### ✅ Por que é **Chain of Responsibility**:
    
    - Cada handler decide se **processa ou passa adiante**.
    - Permite encadear **múltiplas responsabilidades** dinamicamente.
    - Evita acoplamento direto entre remetente e manipuladores.
- 🔹 **5. Mediator**
    - **Tipo:** Comportamental
    - **Objetivo:** Define um objeto que encapsula a comunicação entre objetos para reduzir o acoplamento.
    - **Herança:** Interface do Mediator e componentes participantes
    - **Injeção de Dependência:** Componentes injetam ou recebem o Mediator
    - **Vantagens:**
        - Reduz dependências entre objetos
        - Facilita manutenção
    - **Desvantagens:**
        - Mediator pode se tornar complexo (Deus-objeto)
    - **Formas de Instanciação:** Mediador central é criado e distribuído
    - **Princípios:**
        - ✅ DIP
        - ✅ SRP
        - ❌ SRP se o Mediator crescer demais
    
    ### ✅ Exemplo:
    
    ```java
    interface Mediator {
        void notify(Component sender, String event);
    }
    
    abstract class Component {
        protected Mediator mediator;
        public Component(Mediator m) { this.mediator = m; }
    }
    
    class Button extends Component {
        public Button(Mediator m) { super(m); }
        public void click() {
            System.out.println("Botão clicado.");
            mediator.notify(this, "click");
        }
    }
    
    class TextBox extends Component {
        public TextBox(Mediator m) { super(m); }
        public void clear() { System.out.println("TextBox limpo."); }
    }
    
    class FormMediator implements Mediator {
        private Button button;
        private TextBox textBox;
    
        public void setComponents(Button b, TextBox t) {
            this.button = b;
            this.textBox = t;
        }
    
        public void notify(Component sender, String event) {
            if (sender == button && event.equals("click")) {
                textBox.clear();
            }
        }
    }
    
    ```
    
    ### ✅ Por que é **Mediator**:
    
    - Centraliza a **comunicação entre componentes** (Button e TextBox).
    - Remove o acoplamento direto entre eles.
    - Componentes apenas conhecem o **mediador**, não os outros.
- 🔹 **6. Adapter**
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%208.png)
    
    - **Tipo:** Estrutural
    - **Objetivo:** Permite que interfaces incompatíveis trabalhem juntas.
    - **Herança:** Implementa a interface esperada adaptando a real
    - **Injeção de Dependência:** Pode usar ID para injetar adaptadores
    - **Vantagens:**
        - Reutilização de código legado
        - Integração de APIs externas
    - **Desvantagens:**
        - Pode introduzir complexidade adicional
    - **Formas de Instanciação:** Classe ou objeto wrapper
    - **Princípios:**
        - ✅ OCP
        - ✅ DIP
    
    ### ✅ Exemplo:
    
    ```java
    interface Target {
        void request();
    }
    
    class LegacyService {
        public void legacyRequest() {
            System.out.println("Executando requisição legada...");
        }
    }
    
    class Adapter implements Target {
        private LegacyService legacy;
        public Adapter(LegacyService legacy) { this.legacy = legacy; }
        public void request() {
            legacy.legacyRequest();
        }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            LegacyService legacy = new LegacyService();
            Target adapter = new Adapter(legacy);
            adapter.request(); // Executa o método legado através da nova interface
        }
    }
    
    ```
    
    ### ✅ Por que é **Adapter**:
    
    - Conecta uma **interface antiga** (LegacyService) a uma nova (Target).
    - Permite reutilizar código legado **sem alterá-lo**.
    - Fornece uma **interface compatível** ao cliente.
- 🔹 **7. Decorator**
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%209.png)
    
    - **Tipo:** Estrutural
    - **Objetivo:** Adiciona funcionalidades a um objeto dinamicamente.
    - **Herança:** Interface comum entre componente e decoradores
    - **Injeção de Dependência:** Decoradores injetam componentes
    - **Vantagens:**
        - Composição flexível
        - Evita herança excessiva
    - **Desvantagens:**
        - Muitas classes envolvidas
    - **Formas de Instanciação:** Composição de objetos em tempo de execução
    - **Princípios:**
        - ✅ OCP
        - ✅ DIP
        - ✅ SRP
    
    Acrescentar um comportamento que o original não é capaz de executar.
    
    ### ✅ Exemplo:
    
    ```java
    interface Notifier {
        void send(String msg);
    }
    
    class EmailNotifier implements Notifier {
        public void send(String msg) {
            System.out.println("Enviando Email: " + msg);
        }
    }
    
    class SMSDecorator implements Notifier {
        private Notifier wrappee;
        public SMSDecorator(Notifier wrappee) { this.wrappee = wrappee; }
    
        public void send(String msg) {
            wrappee.send(msg);
            System.out.println("Enviando SMS: " + msg);
        }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            Notifier notifier = new SMSDecorator(new EmailNotifier());
            notifier.send("Seu código é 1234");
        }
    }
    
    ```
    
    ### ✅ Por que é **Decorator**:
    
    - Adiciona **comportamento adicional** (SMS) dinamicamente sem modificar o objeto original (Email).
    - Usa composição, não herança.
    - Permite empilhar múltiplos decoradores.
- 🔹 **8. Facade**
    - **Tipo:** Estrutural
    - **Objetivo:** Fornece uma interface simplificada para um subsistema complexo.
    - **Herança:** Não necessariamente usa
    - **Injeção de Dependência:** O facade pode receber subsistemas por ID
    - **Vantagens:**
        - Esconde a complexidade
        - Fácil de usar
    - **Desvantagens:**
        - Pode virar um “Deus objeto” se crescer demais
    - **Formas de Instanciação:** Classe intermediária que coordena outros objetos
    - **Princípios:**
        - ✅ SRP
        - ✅ DIP
        - ❌ OCP se for expandido em vez de estendido
    
    ### ✅ Exemplo:
    
    ```java
    class AuthService {
        public void authenticate() { System.out.println("Autenticado."); }
    }
    
    class PaymentService {
        public void pay() { System.out.println("Pagamento realizado."); }
    }
    
    class NotificationService {
        public void notifyUser() { System.out.println("Notificação enviada."); }
    }
    
    class EcommerceFacade {
        private AuthService auth = new AuthService();
        private PaymentService payment = new PaymentService();
        private NotificationService notification = new NotificationService();
    
        public void completeOrder() {
            auth.authenticate();
            payment.pay();
            notification.notifyUser();
        }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            EcommerceFacade facade = new EcommerceFacade();
            facade.completeOrder();
        }
    }
    
    ```
    
    ### ✅ Por que é **Facade**:
    
    - Fornece uma **interface simplificada** (`completeOrder`) para um conjunto de serviços.
    - Esconde complexidade de subsistemas.
    - Cliente não precisa saber a **ordem ou dependência entre os serviços**.
- 🔹 **9. Singleton**
    - **Tipo:** Criacional
    - **Objetivo:** Garante que uma classe tenha uma única instância e fornece um ponto de acesso global.
    - **Herança:** Normalmente não usa
    - **Injeção de Dependência:** Frequentemente substituído por ID moderno
    - **Vantagens:**
        - Única instância compartilhada
        - Controla acesso global
    - **Desvantagens:**
        - Dificulta testes
        - Introduz estado global
    - **Formas de Instanciação:** Lazy ou eager loading
    - **Princípios:**
        - ❌ DIP
        - ❌ SRP
        - ❌ Testabilidade
    
    ### ✅ Exemplo:
    
    ```java
    class Logger {
        private static Logger instance;
    
        private Logger() {}
    
        public static Logger getInstance() {
            if (instance == null) instance = new Logger();
            return instance;
        }
    
        public void log(String msg) {
            System.out.println("LOG: " + msg);
        }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            Logger logger = Logger.getInstance();
            logger.log("Sistema iniciado.");
        }
    }
    
    ```
    
    ### ✅ Por que é **Singleton**:
    
    - Garante **uma única instância** de `Logger`.
    - Fornece um ponto global de acesso com `getInstance()`.
    - Útil para **recursos compartilhados**, como logs ou conexões.
- 🔹 **10. Visitor**
    - **Tipo:** Comportamental
    - **Objetivo:** Permite adicionar novas operações a objetos sem alterar suas classes.
    - **Herança:** Interface de visitante + elementos visitáveis
    - **Injeção de Dependência:** Visitante é injetado no elemento
    - **Vantagens:**
        - Separação clara entre estrutura e comportamento
        - Facilita adição de novas operações
    - **Desvantagens:**
        - Dificulta adição de novos elementos
    - **Formas de Instanciação:** Visitor concreto é passado aos elementos
    - **Princípios:**
        - ✅ OCP
        - ❌ LSP se os elementos forem alterados
    
    ### ✅ Exemplo:
    
    ```java
    interface Visitor {
        void visit(Book b);
        void visit(Movie m);
    }
    
    interface Item {
        void accept(Visitor v);
    }
    
    class Book implements Item {
        public void accept(Visitor v) { v.visit(this); }
    }
    
    class Movie implements Item {
        public void accept(Visitor v) { v.visit(this); }
    }
    
    class PriceVisitor implements Visitor {
        public void visit(Book b) { System.out.println("Preço do livro: R$20"); }
        public void visit(Movie m) { System.out.println("Preço do filme: R$30"); }
    }
    
    // Uso
    class Main {
        public static void main(String[] args) {
            Item[] items = { new Book(), new Movie() };
            Visitor visitor = new PriceVisitor();
    
            for (Item i : items) i.accept(visitor);
        }
    }
    
    ```
    
    ### ✅ Por que é **Visitor**:
    
    - Permite aplicar **operações específicas sem modificar as classes** `Book` ou `Movie`.
    - Cada `Item` aceita um visitante e delega a lógica para ele.
    - Facilita a **extensão de comportamentos**, mantendo a estrutura intacta.
- 🔹 **11. Proxy**
    
    ![image.png](PP%201fd2e5a697c380bf90ccf97769a9f044/image%2010.png)
    
    - **Tipo:** Estrutural
    - **Objetivo:** Controlar o acesso a um objeto, podendo adicionar lógica extra antes ou depois da chamada real.
    - **Herança:** Interface ou classe base compartilhada entre Proxy e Real Subject.
    - **Injeção de Dependência:** Pode injetar o objeto real dentro do proxy.
    - **Vantagens:**
        - Controle de acesso centralizado
        - Pode adicionar cache, logs, segurança e lazy loading
        - Encapsula complexidade do objeto real
    - **Desvantagens:**
        - Aumenta a complexidade estrutural
        - Possível sobrecarga de desempenho se mal projetado
    - **Formas de Instanciação:** Proxy criado manualmente ou gerado dinamicamente (Reflection, bibliotecas como CGLIB)
    - **Princípios:**
        - ✅ Aberto/Fechado (OCP)
        - ✅ SRP
        - ⚠️ DIP (pode violar se Proxy depender de uma implementação concreta)
    
    ---
    
    ### ✅ Código:
    
    ```java
    interface Service {
        void request();
    }
    
    class RealService implements Service {
        public void request() {
            System.out.println("Executando operação no serviço real...");
        }
    }
    
    class ServiceProxy implements Service {
        private RealService realService;
    
        public void request() {
            if (realService == null) {
                realService = new RealService(); // Lazy loading
            }
            System.out.println("[Proxy] Verificando permissões...");
            realService.request();
            System.out.println("[Proxy] Operação concluída.");
        }
    }
    
    class Main {
        public static void main(String[] args) {
            Service service = new ServiceProxy();
            service.request();
        }
    }
    
    ```
    
    ---
    
    ### ✅ Por que é **Proxy**:
    
    - O cliente interage com o **Proxy** como se fosse o objeto real.
    - O **Proxy** adiciona lógica extra (permissão, log, lazy loading) **antes e depois** da chamada ao objeto real.
    - O padrão mantém **a mesma interface**, permitindo trocar Proxy e Real Service de forma transparente.
- 🔸 **Comparativo Geral**
    
    
    | Padrão | Tipo | ID-Friendly | Herança | Complexidade | Vantagem Principal | Violação Comum |
    | --- | --- | --- | --- | --- | --- | --- |
    | Abstract Factory | Criacional | ✅ | Alta | Média | Criação consistente de objetos relacionados | ISP, DIP |
    | Observer | Comportamental | ✅ | Média | Baixa | Comunicação desacoplada | - |
    | State | Comportamental | ✅ | Média | Média | Alternância clara de estados | - |
    | Chain of Responsibility | Comportamental | ✅ | Média | Média | Flexibilidade na manipulação | LSP |
    | Mediator | Comportamental | ✅ | Média | Alta | Comunicação centralizada | SRP |
    | Adapter | Estrutural | ✅ | Baixa | Baixa | Compatibilização de interfaces | - |
    | Decorator | Estrutural | ✅ | Média | Média | Adição dinâmica de responsabilidades | - |
    | Facade | Estrutural | ✅ | Baixa | Baixa | Simplificação da interface | OCP |
    | Singleton | Criacional | ❌ | Baixa | Baixa | Garantia de instância única | DIP, SRP |
    | Visitor | Comportamental | ✅ | Alta | Alta | Adição de comportamentos sem alterar estrutura | LS |

---

**Prova**

- 🔸**Comparativo**
    
    
    | Padrão | Tipo | Objetivo Principal | Quando Usar | Vantagens | Desvantagens |
    | --- | --- | --- | --- | --- | --- |
    | **Proxy** | Estrutural | Controlar o acesso a um objeto, podendo adicionar lógica extra (ex.: cache, segurança, carregamento sob demanda) sem mudar a interface original. | Quando um objeto é caro para criar ou acessar, ou quando precisa de controle de acesso. | - Oculta complexidade de acesso- Pode implementar lazy loading- Mantém mesma interface do objeto real | - Aumenta complexidade- Pode introduzir latência se mal implementado |
    | **Adapter** | Estrutural | Converter a interface de uma classe existente para outra esperada pelo cliente, sem alterar o código original. | Quando precisa integrar sistemas ou classes incompatíveis. | - Reuso de código legado- Facilita integração entre APIs | - Pode gerar camadas extras de abstração desnecessárias se usado demais |
    | **State** | Comportamental | Alterar o comportamento de um objeto quando seu estado interno muda, sem usar condicionais complexos. | Quando um objeto muda de comportamento com base em seu estado interno. | - Elimina grandes blocos `if/else` ou `switch`- Facilita inclusão de novos estados | - Pode aumentar número de classes- Estrutura inicial mais complexa |
    | **Decorator** | Estrutural | Adicionar funcionalidades a um objeto de forma dinâmica, sem alterar a classe original. | Quando deseja estender o comportamento de um objeto em tempo de execução. | - Alta flexibilidade- Evita herança excessiva | - Muitos decoradores aninhados podem dificultar depuração |
    | **Chain of Responsibility** | Comportamental | Passar uma requisição por uma cadeia de manipuladores até que um deles a processe. | Quando há múltiplos possíveis manipuladores para uma solicitação. | - Desacopla remetente e receptor- Flexível para reorganizar/manter handlers | - Pode ser difícil rastrear qual handler processou a requisição- Se mal projetado, pode não haver processamento da requisição |
    
    ---
    
    **Resumo visual de propósito**:
    
    - **Proxy** → “Colocar um segurança na porta” antes de acessar um objeto.
    - **Adapter** → “Traduzir” para que duas partes conversem.
    - **State** → “Trocar de roupa” para mudar de comportamento.
    - **Chain** → “Passar a bola” até alguém decidir jogar.
    - **Decorator** → “Colocar acessórios” sem mudar o que você é.
    
    ![Captura de tela 2025-08-09 142611.png](PP%201fd2e5a697c380bf90ccf97769a9f044/Captura_de_tela_2025-08-09_142611.png)
    
    ![Captura de tela 2025-08-09 143011.png](PP%201fd2e5a697c380bf90ccf97769a9f044/Captura_de_tela_2025-08-09_143011.png)
    
    ![ChatGPT Image 9 de ago. de 2025, 14_31_33.png](PP%201fd2e5a697c380bf90ccf97769a9f044/ChatGPT_Image_9_de_ago._de_2025_14_31_33.png)
    
    ![Captura de tela 2025-08-09 142647.png](PP%201fd2e5a697c380bf90ccf97769a9f044/Captura_de_tela_2025-08-09_142647.png)
    
    ![Captura de tela 2025-08-09 142711.png](PP%201fd2e5a697c380bf90ccf97769a9f044/Captura_de_tela_2025-08-09_142711.png)
    
    ![Captura de tela 2025-08-09 142927.png](PP%201fd2e5a697c380bf90ccf97769a9f044/Captura_de_tela_2025-08-09_142927.png)
    
- 🔸 **Exercícios**
    
    ### Exercício 1
    
    **I. Problema**
    
    Uma empresa de streaming de vídeos quer implementar um sistema que gerencie o acesso aos seus conteúdos exclusivos. Os assinantes só podem acessar os vídeos se estiverem com a assinatura ativa. Porém, o sistema precisa validar o acesso sem expor diretamente os vídeos, garantindo uma camada de controle.
    
    Além disso, para evitar sobrecarga, o sistema deve carregar os vídeos apenas quando um usuário realmente começar a assisti-los, e liberar recursos quando o vídeo não estiver sendo assistido.
    
    **II. Tarefa**
    
    Crie uma aplicação que simule o controle de acesso aos vídeos da plataforma. Considere que o sistema verifica se o usuário tem direito de acesso antes de permitir o streaming e que os vídeos são carregados sob demanda.
    
    Implemente as classes para representar usuários, vídeos e o controle de acesso, e modele a interação entre eles.
    
    Monte o diagrama de classes da sua solução.
    
    Resposta: proxy
    
    ---
    
    ### Exercício 2
    
    **I. Problema**
    
    Uma loja online vende produtos que podem ser customizados com várias opções, como embalagem para presente, garantia estendida, entrega expressa, entre outras.
    
    Os clientes podem escolher qualquer combinação dessas opções para adicionar ao produto base. Cada opção deve alterar o preço final e, às vezes, o comportamento do produto (como a forma de entrega).
    
    **II. Tarefa**
    
    Crie um sistema que permita montar produtos personalizados, adicionando dinamicamente diferentes opções que alteram o preço e a descrição do produto.
    
    Desenvolva as classes necessárias para representar produtos e opções, e garanta que o sistema possa adicionar ou remover opções de forma flexível.
    
    Desenhe o diagrama de classes que represente a estrutura do sistema.
    
    Resposta: decorator
    
    ---
    
    ### Exercício 3
    
    **I. Problema**
    
    Um sistema de vendas online possui vários estados para o pedido: "Novo", "Pago", "Enviado", "Entregue" e "Cancelado".
    
    Cada estado do pedido permite um conjunto específico de operações (ex: só pode enviar pedido se estiver pago, não pode cancelar pedido entregue, etc). O sistema deve garantir que as transições e operações respeitem as regras de cada estado.
    
    **II. Tarefa**
    
    Implemente uma aplicação que modele os diferentes estados do pedido e suas regras de transição e operação.
    
    Garanta que a lógica de mudança de estado esteja encapsulada de forma que o objeto pedido possa alterar seu comportamento conforme o estado em que se encontra.
    
    Crie o diagrama de classes para a solução.
    
    Resposta: state
    
    ---
    
    ### Exercício 4
    
    **I. Problema**
    
    Um sistema de suporte ao cliente recebe solicitações de diversos tipos (técnico, financeiro, comercial). Cada solicitação pode ser tratada por um agente específico.
    
    Quando uma solicitação chega, ela deve ser encaminhada para o agente apropriado. Se o agente não puder resolver, deve passar para o próximo na cadeia, até que alguém consiga resolver ou a solicitação seja descartada.
    
    **II. Tarefa**
    
    Implemente uma aplicação que modele o fluxo de tratamento das solicitações, com agentes responsáveis por diferentes tipos de demandas.
    
    Cada agente deve decidir se trata ou passa para o próximo agente.
    
    Desenhe o diagrama de classes que exemplifique a cadeia de tratamento.
    
    Resposta: chain
    
    ---
    
    ### Exercício 5
    
    **I. Problema**
    
    Uma aplicação precisa integrar diferentes sistemas de pagamento (cartão de crédito, boleto bancário, carteira digital), cada um com sua própria API e formato de dados.
    
    O sistema central deseja utilizar uma interface única para realizar pagamentos, independente do sistema de pagamento específico.
    
    **II. Tarefa**
    
    Implemente um sistema que permita realizar pagamentos usando uma interface padrão, adaptando as chamadas para as APIs específicas dos sistemas externos.
    
    Crie as classes que representam a interface comum e os adaptadores para cada sistema de pagamento.
    
    Apresente o diagrama de classes da solução.
    
    Resposta: adapter
    
- 🔸 **Gabarito**
    
    # Exercício 1
    
    ### Solução
    
    O sistema terá:
    
    - **Interface Vídeo**: com método `assistir()`.
    - **Classe VídeoReal**: representa o vídeo real, com o conteúdo.
    - **Classe VídeoProxy**: controla o acesso ao vídeo real. Verifica se o usuário tem assinatura ativa antes de permitir o acesso e carrega o vídeo só quando solicitado.
    - **Classe Usuário**: contém informações sobre o usuário, incluindo status da assinatura.
    
    Assim, o proxy atua como intermediário controlando o acesso e a criação do vídeo real.
    
    ### Diagrama de Classes
    
    ```
    +----------------+            +----------------+
    |   Usuário      |            |    Vídeo       |
    |----------------|<>----------| <<interface>>  |
    | - nome         |            | + assistir()   |
    | - assinaturaAtiva |          +----------------+
    +----------------+                  ^
                                       |
                          +---------------------+
                          |    VídeoReal        |
                          |---------------------|
                          | - conteúdo          |
                          | + assistir()        |
                          +---------------------+
                                 ^
                                 |
                          +---------------------+
                          |    VídeoProxy       |
                          |---------------------|
                          | - usuário: Usuário  |
                          | - vídeoReal: VídeoReal |
                          | + assistir()        |
                          +---------------------+
    
    ```
    
    ---
    
    # Exercício 2
    
    ### Solução
    
    Temos:
    
    - **Interface Produto**: com métodos `getDescricao()` e `getPreco()`.
    - **Classe ProdutoBase**: produto simples.
    - **Classe DecoradorProduto**: abstrata que implementa Produto e contém um Produto interno.
    - **Classes Concretas de Decoradores**: embalagem para presente, garantia estendida, entrega expressa, etc., que estendem DecoradorProduto e adicionam funcionalidade (preço e descrição).
    
    Assim, o cliente monta o produto final adicionando quantos decoradores quiser.
    
    ### Diagrama de Classes
    
    ```
    +--------------------+
    |    Produto         |  <<interface>>
    |--------------------|
    | + getDescricao()    |
    | + getPreco()        |
    +--------------------+
           ^
           |
    +--------------------+
    |   ProdutoBase      |
    |--------------------|
    | - descricao         |
    | - preco             |
    | + getDescricao()    |
    | + getPreco()        |
    +--------------------+
           ^
           |
    +------------------------+
    | DecoradorProduto       |
    |------------------------|
    | - produto: Produto     |
    | + getDescricao()       |
    | + getPreco()           |
    +------------------------+
           ^
           |
    +--------------------+   +-----------------------+  +--------------------+
    | EmbalagemPresente  |   | GarantiaEstendida     |  | EntregaExpressa    |
    +--------------------+   +-----------------------+  +--------------------+
    | + getDescricao()    |   | + getDescricao()       |  | + getDescricao()    |
    | + getPreco()        |   | + getPreco()           |  | + getPreco()        |
    +--------------------+   +-----------------------+  +--------------------+
    
    ```
    
    ---
    
    # Exercício 3
    
    ### Solução
    
    Para modelar os estados do pedido:
    
    - **Classe Pedido**: contém um atributo estado do tipo EstadoPedido.
    - **Interface EstadoPedido**: métodos para ações possíveis (pagar, enviar, cancelar, entregar).
    - **Classes concretas para cada estado**: Novo, Pago, Enviado, Entregue, Cancelado, implementando as regras específicas para cada ação e fazendo transições para outros estados.
    
    Assim, o comportamento do pedido muda conforme seu estado atual.
    
    ### Diagrama de Classes
    
    ```
    +---------------+
    |   Pedido      |
    |---------------|
    | - estado: EstadoPedido |
    | + pagar()     |
    | + enviar()    |
    | + cancelar()  |
    | + entregar()  |
    +---------------+
             |
             v
    +---------------------+
    |   EstadoPedido      |  <<interface>>
    |---------------------|
    | + pagar()           |
    | + enviar()          |
    | + cancelar()        |
    | + entregar()        |
    +---------------------+
         /   |    |    |   \
    +------+ +------+ +------+ +-------+ +---------+
    | Novo | | Pago | | Envi | | Entreg | |Cancel  |
    +------+ +------+ +------+ +-------+ +---------+
    | ...  | | ...  | | ...  | | ...   | | ...     |
    +------+ +------+ +------+ +-------+ +---------+
    
    ```
    
    ---
    
    # Exercício 4
    
    ### Solução
    
    Aqui teremos:
    
    - **Classe Solicitação**: contém os dados da solicitação.
    - **Interface Handler (Agente)**: método `setProximo()` e `processar(solicitacao)`.
    - **Classes Concretas de Agentes**: Técnico, Financeiro, Comercial.
    - Cada agente decide se trata a solicitação ou passa para o próximo.
    
    Assim, a solicitação percorre uma cadeia até ser tratada.
    
    ### Diagrama de Classes
    
    ```
    +-----------------+
    |   Solicitação   |
    +-----------------+
    | - tipo          |
    | - detalhes      |
    +-----------------+
    
    +-----------------------+
    |     Handler           |  <<interface>>
    +-----------------------+
    | + setProximo(handler)  |
    | + processar(solicitacao) |
    +-----------------------+
               ^
               |
    +--------------------+    +---------------------+    +-------------------+
    | AgenteTecnico      |    | AgenteFinanceiro    |    | AgenteComercial   |
    +--------------------+    +---------------------+    +-------------------+
    | - proximo: Handler |    | - proximo: Handler  |    | - proximo: Handler|
    | + processar(...)   |    | + processar(...)    |    | + processar(...)  |
    +--------------------+    +---------------------+    +-------------------+
    
    ```
    
    ---
    
    # Exercício 5
    
    ### Solução
    
    Para unificar sistemas de pagamento diferentes:
    
    - **Interface Pagamento**: método `pagar(valor)`.
    - **Classes específicas dos sistemas de pagamento externos** (ex: APICartaoCredito, APIBoleto, APIWallet), com métodos próprios.
    - **Adaptadores**: classes que implementam Pagamento e adaptam as chamadas para as APIs específicas.
    - **Classe Cliente**: usa a interface Pagamento para realizar pagamentos.
    
    ### Diagrama de Classes
    
    ```
    +-----------------+
    |   Pagamento     |  <<interface>>
    +-----------------+
    | + pagar(valor)  |
    +-----------------+
          ^           ^           ^
          |           |           |
    +------------+ +------------+ +-------------+
    | AdapterCC  | | AdapterBoleto | | AdapterWallet |
    +------------+ +------------+ +-------------+
    | - apiCC    | | - apiBoleto  | | - apiWallet  |
    | + pagar()  | | + pagar()    | | + pagar()   |
    +------------+ +------------+ +-------------+
    
    +----------------+
    | APICartaoCredito|
    +----------------+
    | + processarPagamento() |
    +----------------+
    
    +----------------+
    | APIBoleto      |
    +----------------+
    | + gerarBoleto()|
    +----------------+
    
    +----------------+
    | APIWallet      |
    +----------------+
    | + transferir() |
    +----------------+
    
    ```
    
    ---