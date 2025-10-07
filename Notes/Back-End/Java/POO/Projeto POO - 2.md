# Projeto POO - 2

https://github.com/agu3des/SistemaBanco

https://drive.google.com/file/d/1MZsGoC7plf5yRfPz9dLNekioWnmUZD36/view?usp=drive_link

- Cenário
    
    Um Banco financeiro contratou você para implementar o sistema de informação bancário Banko, que permitirá aos funcionários criarem, alterarem, listarem e apagarem contas correntes e permitirá aos correntistas acessarem os caixas de autoatendimento para as operações de caixa (crédito, débito e transferência de valor), utilizando uma senha numérica. Banko possui dois tipos de contas: simples e especial. A diferença está no limite de débito, que é zero para uma conta simples e negativo para uma conta especial.
    
- Modelo de negócio do sistema
    
    ![image.png](Projeto%20POO%20-%202%202c0fa909425e4e5b9cacafe0e8436ac2/image.png)
    
- Requisitos (classe Fachada)
    
    
    | public static  
    ArrayList<Correntista> | listarCorrentistas() retorna todos os correntistas do repositório ordenados pelo cpf | X |
    | --- | --- | --- |
    | public static  
    ArrayList<Conta> | listarContas() retorna todas as contas do repositório | X |
    | public static void | criarCorrentista(cpf,nome,senha) – cria um correntista e o adiciona no repositório | X |
    | public static void | criarConta(cpf) – cria uma conta simples para o correntista (titular) e a adiciona ao  repositório | X |
    | public static void | criarContaEspecial(cpf, limite) – cria uma conta especial para o correntista e a adiciona  ao repositório | X |
    | public static void | inserirCorrentistaConta(id, cpf) – cria relacionamento entre um correntista e uma conta | X |
    | public static void | removerCorrentistaConta(id, cpf) – remove relacionamento entre um correntista e uma conta | X |
    | public static void | apagarConta(id) – remove os relacionamentos dos correntistas da conta e remove a  conta do repositório | X |
    | public static void | creditarValor(id, cpf, senha, valor) – credita um valor na conta do correntista | X |
    | public static void | debitarValor(id, cpf, senha, valor) – debita um valor na conta do correntista | X |
    | public static void | transferirValor(id1, cpf, senha, valor, id2) – transfere um valor da conta do correntista (id1)  para outra conta (id2) - do mesmo ou de outro correntista |  |
- Tarefas
    1. Desenvolver o sistema em Java, usando a arquitetura em quatro camadas (Interface de usuário, Repositório, Modelo de negócio e de Regras de negócio).
    2. A Interface do Usuário deve ter as seguintes telas:
        1. TelaPrincipal – contém os menus “Correntista”, “Conta” e “Caixa”
        2. TelaCorrentista – contém listagem dos correntistas e campos e botão para criar correntista e botão para mostrar os ids de suas contas
        3. TelaConta – contém listagem das contas (simples e especial) com seus atributos e saldo total (calculado) e campos para criar uma conta (simples e especial), além de botões para criar e apagar uma conta selecionada e para adicionar/remover cotitulares de uma conta selecionada 
        4. TelaCaixa – contém campos e botões para creditar, debitar e transferir dinheiro
        
    3. A classe Repositório deve possuir os métodos carregarObjetos() e salvarObjetos(), para ler e gravar os objetos do sistema, usando os arquivos/formatos:
        1. contas.csv (TIPODACONTA;id;data;saldo;limite), onde “limite” é apenas para conta especial 
        2. correntistas.csv (cpf;nome;senha;ids), onde ids é a lista de id das contas (separados por “,”)
- Regras de Negócio
    - [x]  Um correntista é identificado pelo cpf
    - [x]  A senha do correntista é numérica de 4 digitos
    - [x]  Uma conta é identificada por um id sequencial autonumerado (1,2,3...)
    - [x]  O saldo inicial de uma conta é zero
    - [x]  O saldo de uma conta não pode ser negativo, com exceção de uma conta especial, cujo saldo poderá ser negativo até o limite da conta
    - [x]  O limite de uma conta especial tem que ser maior ou igual a 50 reais
    - [x]  A data de uma conta é obtida do computador
    - [x]  A data de uma conta tem o formato “dia/mês/ano”
    - [x]  Não pode criar uma conta sem um correntista titular
    - [x]  O primeiro correntista de uma conta é o titular da conta e os demais correntistas da conta são os cotitulares da conta
    - [x]  Um correntista pode ser titular de no máximo uma conta
    - [x]  Um correntista pode ser cotitular de várias contas
    - [x]  Um correntista titular não pode ser removido de uma conta, a não ser que a conta seja apagada
    - [x]  Um correntista cotitular pode ser removido de uma conta
    - [x]  Uma conta pode ser apagada, se seu saldo for zero, implicando na remoção de seus correntistas
    - [x]  Um correntista não pode ser apagado, mesmo que suas contas forem apagadas
- Pontuação
    
    • Camadas de modelo, regras de negócio e repositório: 5pts
    • Camada de interface do usuário: 1pt
    • Apresentação do projeto: 4pts
    • Grupo (máximo) de 2 alunos
    
- Dúvidas
    
    Fazer for para adicionar contas no array de correntista
    
    A geração da data pode ser feita da fachada ou da conta: no construtor da classe conta
    
    Varrer contas para checar se o cpf já é titular de outra (criar conta fachada)
    
    Verificar que os digitos da senha são números
    
    Arquivos de contas separados
    
    Método de comparar em correntista e o sort no repositório getcorrentistas e get na fachada
    
- Códigos sobra
    
    ```java
    	private ArrayList<ContaEspecial> contasEspeciais = new ArrayList<>();
    	
    	public void adicionarContaEspecial(ContaEspecial ce)	{
    		contasEspeciais.add(ce);
    	}
    
    	public void removerContaEspecial(ContaEspecial ce)	{
    		contasEspeciais.remove(ce);
    	}
    	
    	public ContaEspecial localizarContaEspecial(int id)	{
    		for(ContaEspecial ce : contasEspeciais)
    			if(ce.getId() == id)
    				return ce;
    		return null;
    	}
    
    	public ArrayList<ContaEspecial> getContasEspeciais() {
    		return contasEspeciais;
    	}
    	
    	public int getTotalContasEspeciais()	{
    		return contasEspeciais.size();
    	}
    
    	public double getSaldoLimite() {
    		return saldo + limite;
    	}
    	
    ```
    
- Telas
    
    TelaCaixa: valores e creditar, debitar e transferir