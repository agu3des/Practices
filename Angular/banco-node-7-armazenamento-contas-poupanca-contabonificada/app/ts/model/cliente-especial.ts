//6. Desenvolver a classe ClienteEspecial, que herda de Cliente e tem uma lista de dependentes (array de Cliente) (mas a tela de Cliente não precisa pensar em colocar os dependentes, apenas um cliente básico)
export class ClienteEspecial extends Cliente {
    private _dependentes: Cliente[]; // Lista de dependentes

    constructor(nome: string, cpf: string, conta: Conta) {
        super(nome, cpf, conta); // Chama o construtor da classe pai (Cliente)
        this._dependentes = [];
    }

    // Método para adicionar dependentes
    adicionarDependente(dependente: Cliente): void {
        this._dependentes.push(dependente);
    }

    // Sobrescrevendo o método toString para incluir os dependentes
    toString(): string {
        let dependentesInfo = this._dependentes.map(dependente => dependente.toString()).join("\n");
        return `${super.toString()}\nDependentes:\n${dependentesInfo}`;
    }
}
