/*2. Desenvolver a classe Clientes, que armazenará todos os clientes do banco num array de clientes (atributo da classe), e terá os seguintes métodos:
2.1 inserir, que recebe um parâmetro do tipo Cliente inserirá um cliente no array de clientes da classe Clientes
2.2 remover, que recebe um cpf e removerá o cliente daquele cpf, se existir
2.3 listar, que devolverá um array de Cliente
2.4 pesquisar, que receberá o cpf do cliente e devolverá o cliente encontrado (se encontrar) */

class Contas {

    private contas: Array<Conta>;

    constructor() {
        this.contas = new Array<Conta>();
        const c1 = new Conta('1', 100);
        const c2 = new Conta('2', 200);
        this.contas.push(c1, c2);
    }

    inserir(conta: Conta): void {
        this.contas.push(conta);
    }

    remover(numero: string): void {
        const contaARemover = this.pesquisar(numero);
        if (contaARemover) {
            const indiceConta = this.contas.indexOf(contaARemover);
            if (indiceConta > -1) {
                this.contas.splice(indiceConta, 1);
            }
        }
    }

    pesquisar(numero: string): Conta {
        return this.contas.find(
            conta => conta.numero === numero
        );
    }

    listar(): Array<Conta> {
        return this.contas;
    }

}
