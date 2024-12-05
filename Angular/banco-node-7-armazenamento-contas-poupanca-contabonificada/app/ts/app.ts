// Inicializando o ContaController para manipulação de contas
let contaController = new ContaController();
contaController.listar();

// Criando contas
const conta1 = new Conta('400', 100);
const conta2 = new Conta('500', 1500);

// Inicializando o ClienteController para manipulação de clientes
const clienteController = new ClienteController();

// Criando clientes normais
const cliente1 = new Cliente('José', '300', conta1);
const cliente2 = new Cliente('Maria', '301', conta2);

// Criando um ClienteEspecial e adicionando dependentes
const clienteEspecial = new ClienteEspecial('Carlos', '400', conta1);
clienteEspecial.adicionarDependente(cliente1);
clienteEspecial.adicionarDependente(cliente2);

// Logando informações no console para validação
console.log("Informações do Cliente Especial:");
console.log(clienteEspecial.toString());

// Listando os dependentes do ClienteEspecial
console.log("\nLista de Dependentes:");
clienteEspecial.listarDependentes().forEach(dependente => {
    console.log(dependente.toString());
});
