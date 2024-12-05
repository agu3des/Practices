

export class ClienteController {
    private inputNome: HTMLInputElement;
    private inputCpf: HTMLInputElement;
    private inputConta: HTMLInputElement;

    private clientes: Clientes;
    private contas: any;

    constructor() {
        this.inputNome = <HTMLInputElement>document.querySelector("#nome");
        this.inputCpf = <HTMLInputElement>document.querySelector("#cpf");
        this.inputConta = <HTMLInputElement>document.querySelector("#conta");
        this.clientes = new Clientes();
        this.contas = new Contas(); // Supondo que a classe Contas tenha um método de pesquisa
    }

    inserir(evento: Event): void {
        evento.preventDefault();

        const numeroConta = this.inputConta.value;
        const contaEncontrada = this.contas.pesquisar(numeroConta);

        if (contaEncontrada) {
            // Aqui, ao invés de criar diretamente um Cliente, criaremos um ClienteEspecial.
            const novoCliente = new ClienteEspecial(this.inputNome.value, this.inputCpf.value, contaEncontrada);
            
            // Adicionando o cliente à lista
            this.clientes.inserir(novoCliente);
            
            // Inserindo o cliente na tela
            this.inserirClienteNoHTML(novoCliente);

            // Limpando os campos de entrada
            this.inputNome.value = '';
            this.inputCpf.value = '';
            this.inputConta.value = '';
        } else {
            console.log('Conta não encontrada!');
        }
    }

    listar(): void {
        this.clientes.listar().forEach(cliente => {
            this.inserirClienteNoHTML(cliente);
        });
    }

    inserirClienteNoHTML(cliente: Cliente): void {
        const elementoP = document.createElement('p');
        elementoP.textContent = cliente.toString();
        const botaoApagar = document.createElement('button');
        botaoApagar.textContent = 'X';
        botaoApagar.addEventListener('click', (event) => {
            console.log('removendo cliente ' + cliente.toString());
            this.clientes.remover(cliente.cpf);
            (<Element>event.target).parentElement.remove();
        });
        elementoP.appendChild(botaoApagar);
        document.body.appendChild(elementoP);
    }
}
