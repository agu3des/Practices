class ClienteEspecial extends Cliente {
    constructor(nome, cpf, conta) {
        super(nome, cpf, conta);
        this._dependentes = new Array();
    }
    adicionarDependente(dependente) {
        this._dependentes.push(dependente);
    }
    listarDependentes() {
        return this._dependentes;
    }
    toString() {
        let dependentesInfo = this._dependentes
            .map(dep => dep.toString())
            .join('\n');
        return `${super.toString()}
        \nDependentes:\n${dependentesInfo || 'Nenhum dependente'}`;
    }
}
