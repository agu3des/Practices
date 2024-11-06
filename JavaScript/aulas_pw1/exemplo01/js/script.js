const names = ['Ana', 'Maria', 'Braga'];

const listNameElement = document.createElement('ul');
document.body,appendChild(listNameElement);
for(let name of names){
   const liElement = document.createElement('li');
    liElement.textContent = name;
    listNameElement.appendChild(liElement);
}
names.forEach(name => listNameElement.appendChild(document.createElement('li').textContent = name))

function inputName() {
    const inputNameElement = document.querySelector('#name');
    const liElement = document.createElement('li');
    const nameDigitado = inputNameElement.value;
    liElement.textContent = nameDigitado;

    listNameElement.appendChild(liElement);

}