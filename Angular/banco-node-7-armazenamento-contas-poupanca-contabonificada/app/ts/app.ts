let contaController = new ContaController();
contaController.listar();

const conta1 = new Conta('400', 100);
const conta2 = new Conta('500', 1500);
const clienteController = new ClienteController();

// Criando clientes normais
const cliente1 = new Cliente('José', '300', conta1);
const cliente2 = new Cliente('Maria', '301', conta2);

// Criando um ClienteEspecial e adicionando dependentes
const clienteEspecial = new ClienteEspecial('Carlos', '400', conta1);
clienteEspecial.adicionarDependente(cliente1);
clienteEspecial.adicionarDependente(cliente2);

console.log(clienteEspecial.toString()); // Mostra os dependentes do ClienteEspecial
