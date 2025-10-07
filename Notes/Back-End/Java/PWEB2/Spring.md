# Spring

Um framework não intrusivo baseado nos padrões de Inversão de Controle (IoC) e Injeção de Dependências (DI)

Não exige que suas classes de modelo e negócios tenham uma rígida hierarquia, como eram a J2EE (em especial para os Java Beans)

**POJO** (plain old java object) → nomeclatura para seus métodos de acesso e um construtor sem parâmetros

Retira a preocupação do ciclo de vida do objeto (java já faz a parte de descarte pois tem um coletor de lixo)

Sua aplicação fica responsável pelas regras específicas do seu negócio

**Inversão de Controle:** 

![image.png](Spring%2021d2e5a697c38063aff3d6533b1def8c/image.png)

- Métodos e rotinas que serão chamados por um código de infraestrutura
- Este código fica responsável por verificar se algum evento aconteceu, em caso afirmativo, chama o código escrito pelo programador
- Em resumo o framework fornece o básico e o programador complementa com o que é de seu interesse

![image.png](Spring%2021d2e5a697c38063aff3d6533b1def8c/image%201.png)

A injeção é a passagem de uma dependência para outro objeto (cliente)

Ao invés de você implementar uma classe concreta, apenas faz a implementação

**Injeção de Dependência**

É a forma de IC em que um objeto fornece as dependências de um outro objeto

Dependência é um objeto que pode ser usado (serviço)