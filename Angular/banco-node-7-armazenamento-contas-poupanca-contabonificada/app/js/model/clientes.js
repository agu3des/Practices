/*2. Desenvolver a classe Clientes, que armazenará todos os clientes do banco num array de clientes (atributo da classe), e terá os seguintes métodos:
2.1 inserir, que recebe um parâmetro do tipo Cliente inserirá um cliente no array de clientes da classe Clientes
2.2 remover, que recebe um cpf e removerá o cliente daquele cpf, se existir
2.3 listar, que devolverá um array de Cliente
2.4 pesquisar, que receberá o cpf do cliente e devolverá o cliente encontrado (se encontrar) */
class Clientes {
    constructor() {
        this.clientes = new Array();
        const conta1 = new Conta('100', 1000);
        const conta2 = new Conta('200', 2000);
        const cliente1 = new Cliente('João', '100', conta1);
        const cliente2 = new Cliente('Maria', '200', conta2);
        this.clientes.push(cliente1, cliente2);
    }
    inserir(cliente) {
        this.clientes.push(cliente);
    }
    remover(cpf) {
        const clienteARemover = this.pesquisar(cpf);
        if (clienteARemover) {
            const indiceCliente = this.clientes.indexOf(clienteARemover);
            if (indiceCliente > -1) {
                this.clientes.splice(indiceCliente, 1);
            }
        }
    }
    pesquisar(cpf) {
        return this.clientes.find(cliente => cliente.cpf === cpf);
    }
    listar() {
        return this.clientes;
    }
}
