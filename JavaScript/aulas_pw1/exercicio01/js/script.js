const nomes = ['Ana', 'Carla', 'Trísia'];

const listaNomesElement = document.createElement('ul');
document.body.appendChild(listaNomesElement);

for (let nome of nomes) {
    inserirNomeNaLista(nome);
}

function inserirNome() {
    const inputNomeElement = document.querySelector('#nome');
    inserirNomeNaLista(inputNomeElement.value);
}

function inserirNomeNaLista(nome) {
    const liElement = document.createElement('li');
    const botaoRemoverElement = document.createElement('button');
    botaoRemoverElement.textContent = 'X';
    botaoRemoverElement.addEventListener('click', (event) => {
        liElement.remove();
    });

    const spanElement = document.createElement('span');
    spanElement.textContent = nome + ' ';

    spanElement.addEventListener('click', event => {
        const inputElement = document.createElement('input');
        inputElement.value = nome;
        liElement.appendChild(inputElement);
        spanElement.remove();
    });

    liElement.appendChild(spanElement);
    liElement.appendChild(botaoRemoverElement);

    listaNomesElement.appendChild(liElement);
}


