const listaDeUsuarios = [
    {nome: "João", idade: 30, cpf: "12345"},
    {nome: "Maria", idade: 25, cpf: "67890"},
    {nome: "José", idade: 35, cpf: "24680"}
];


const listaUsuariosElement = document.createElement('ul');
document.body.appendChild(listaUsuariosElement);

for (let usuario of listaDeUsuarios) {
    inserirUsuarioNaLista(usuario);
}

function inserirUsuario() {
    const inputUsuarioNome = document.querySelector('#nome');
    const inputUsuarioIdade = document.querySelector('#idade');
    const inputUsuarioCpf = document.querySelector('#cpf');

    let nome = inputUsuarioNome.value;
    let idade = inputUsuarioIdade.value;
    let cpf = inputUsuarioCpf.value;

    const inputUsuarioElement = { nome, idade, cpf };


    inserirUsuarioNaLista(inputUsuarioElement);
}

function inserirUsuarioNaLista(usuario) {
    const liElement = document.createElement('li');

    const botaoRemoverElement = document.createElement('button');
    botaoRemoverElement.textContent = 'X';
    botaoRemoverElement.addEventListener('click', (event) => {
        liElement.remove();
    });

    const spanElement = document.createElement('span');

//    let usuarioStr = JSON.stringify(usuario);

    let usuarioStr = `Nome: ${usuario.nome}    -    Idade: ${usuario.idade}    -    CPF: ${usuario.cpf}  `;

    spanElement.textContent = usuarioStr;

    spanElement.addEventListener('click', (event) => {

        const inputElement = document.createElement('input');

        inputElement.value = usuarioStr;

        liElement.appendChild(inputElement);

        spanElement.remove();
    });

    liElement.appendChild(spanElement);
    liElement.appendChild(botaoRemoverElement);

    listaUsuariosElement.appendChild(liElement);
}




