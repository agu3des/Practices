# Thymeleaf

- **Principais comandos e atributos do Thymeleaf**
    
    ### ✅ **1. `th:text`** — Exibe texto no HTML
    
    Substitui o conteúdo do elemento.
    
    ```html
    <p th:text="${mensagem}">Texto padrão</p>
    
    ```
    
    ---
    
    ### ✅ **2. `th:if` / `th:unless`** — Condicionais
    
    Renderiza o elemento **se** (ou **se não**) a condição for verdadeira.
    
    ```html
    <p th:if="${usuarioLogado}">Bem-vindo!</p>
    <p th:unless="${usuarioLogado}">Faça login</p>
    
    ```
    
    ---
    
    ### ✅ **3. `th:each`** — Repetição (loop)
    
    Itera sobre listas (tipo `for-each`).
    
    ```html
    <tr th:each="livro : ${listaLivros}">
      <td th:text="${livro.titulo}"></td>
    </tr>
    
    ```
    
    ---
    
    ### ✅ **4. `th:href` / `th:src`** — Links e imagens dinâmicas
    
    Insere valores dinâmicos em `href` e `src`.
    
    ```html
    <a th:href="@{/produtos}">Ver produtos</a>
    <img th:src="@{/imagens/logo.png}" alt="Logo">
    
    ```
    
    ---
    
    ### ✅ **5. `th:value`** — Valor de inputs
    
    Preenche campos de formulários.
    
    ```html
    <input type="text" th:value="${usuario.nome}" />
    
    ```
    
    ---
    
    ### ✅ **6. `th:object` + `{}`** — Bind de formulário
    
    Associa um formulário a um objeto.
    
    ```html
    <form th:action="@{/salvar}" th:object="${usuario}" method="post">
      <input type="text" th:field="*{nome}" />
      <input type="email" th:field="*{email}" />
    </form>
    
    ```
    
    ---
    
    ### ✅ **7. `th:action` + `th:method`** — Envio de formulário
    
    Define para onde e como o formulário será enviado.
    
    ```html
    <form th:action="@{/login}" th:method="post">
    
    ```
    
    ---
    
    ### ✅ **8. `th:switch` / `th:case`** — Estrutura de switch
    
    Semelhante ao `switch-case` em Java.
    
    ```html
    <div th:switch="${status}">
      <p th:case="'ATIVO'">Ativo</p>
      <p th:case="'INATIVO'">Inativo</p>
      <p th:case="*">Desconhecido</p>
    </div>
    
    ```
    
    ---
    
    ### ✅ **9. `th:fragment` + `th:replace/include`** — Reutilização de componentes
    
    Usado para **layouts**, **headers**, **footers**, etc.
    
    ```html
    <!-- Em fragmento.html -->
    <div th:fragment="menu">...</div>
    
    <!-- Usando -->
    <div th:replace="fragmento :: menu"></div>
    
    ```
    
    ---
    
    ### ✅ **10. `th:classappend`** — Adiciona classes dinamicamente
    
    Útil para estilização condicional.
    
    ```html
    <div th:classappend="${ativo} ? 'ativo' : 'inativo'"></div>
    
    ```