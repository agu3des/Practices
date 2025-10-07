# Faculdade

Using as a professional:
Nos 2 seguintes há tratamento na requisição assíncrona de modo que ele não precise baixar mais de uma vez
- next.js: 
- remix:

Lembra o conceito do vite

Comandos no package.json do react

```jsx
//next.js
$ npx create-next-app //next.js
```

Assim que baixa por esse comando a página default é essa →

![Captura de tela de 2023-11-22 15-33-35.png](Faculdade%201e5d77a1b706416ba3afce7444c7e1ec/Captura_de_tela_de_2023-11-22_15-33-35.png)

```jsx
//FUNCTION COMPONENT
function Hello() {
	return <h1>Olá react</h1>;
}
export default function Home() {
	return (
		<div>
			<Hello />
			<Hello />
		</div>
	);
}
```

```jsx
//CLASS COMPONENT, não tão utilizada atualmente
export default class App extends React.Component {
  render() {
    return <h1>Investimentos</h1>;
  }
}
```

Babel: transforma de um para outro de uma linguagem para outra, de modo a facilitar a forma  como enxergamos

JSX é uma forma simplificada de criar os create element blablabla

```jsx
import { jsx as _jsx } from "react/jsx-runtime";
function Hello() {
  return /*#__PURE__*/_jsx("h1", {
    children: "Ol\xE1 react"
  });
}
```

No react a tag vazia se chama **fragment** <> </>

Não aceita tag vazia, ex: <img src=””**/**> esse contra barra é o que indica um fechamento ou o fragmente em cima e em baixo

Utilizar o padrão camelCase, usar em palavras compostas, ex: className

Se tiver em maiúscula já associa a um componente ex: Hello

```jsx
<Hello className="text-lg"/>
```

Utilizando a interpolação de variáveis ele não precisa do $, é só colocar as chaves . Se for número é direto, se for str é aspas duplas.

```jsx
function Hello() {
	const name = 'React';
	const year = 2023;
	return (
		<h1 className="text-lg">
		Olá {name}-{year} {'ifpb'}-{2023} {{a: 1}}</h1>;
	);
}	
export default function Home() {
	return (
		<div>
			<Hello />
			<Hello></Hello>
		</div>
	);
}
```

Interpolação de variável: no react não precisa colocar o $, ou seja, é só colocar entre chaves. Para usar json é só coloca-lo entre chaves duplas {{a: 1}}

```jsx
function Hello() {
	return (
		<h1 className="text-lg">
		Olá {props.name}</h1>;
	);
}	
export default function Home() {
	return (
		<>
			<Hello name="Luiz"/>
			<Hello name="IFPB"></Hello>
		</>
	);
}
```

props: são atributos dos componentes. Que fica dentro do parâmetro das funções como tá lá em cima

```jsx
function Hello({ name }) {
	return <h1 className="text-lg">Olá {name}</h1>;

export default function Home() {
	const people = [
	{
		name: 'Ana',
		email: 'ana@email.com',
	},
	{
		name: 'Bob',
		email: 'bob@email.com',
	},
];
	return (
		<>
			{people.map((person) => (
				<Hello name={person.name} key={person.email} />
			))}
		</>
	);
}
```

### React Hooks

Funções que começam com ‘Use’

```jsx
'use client';
 
import { useState } from 'react';
import { IconEye, IconEyeOff } from '@tabler/icons-react';
import InvestmentCard from '@/components/InvestmentCard';
import { investments } from '@/data/seed';
 
export default function Home() {
  const [isShowValues, setIsShowValues] = useState(true);
 
  const toggleShowValues = () => {
    setIsShowValues(!isShowValues);
  };
 
  return (
    <>
      <header className="my-12">
        <div className="float-right" onClick={toggleShowValues}>
          {isShowValues ? <IconEye size={24} /> : <IconEyeOff size={24} />}
        </div>
        <h1 className="text-center text-2xl font-bold">Investimentos</h1>
      </header>
 
      <div className="investments grid grid-cols-3 gap-3">
        {investments.map((investment) => (
          <InvestmentCard
            {...investment}
            isShowValue={isShowValues}
            key={investment.id}
          />
        ))}
      </div>
    </>
  );
}
```

pega a variável

altera um state →set

Cria-se uma função:

Toggle - altera de uma situação para outra / de um estado para outro, ex: tenho true e quero ir para false

Quando se trabalha com estado não se usa atribuições e sim funções que alteram ela

### Conditional Rendering

```jsx
{isShowValues ? <IconEye size={24} /> : <IconEyeOff size={24} />}
```

Se isso for verdade (?) faça isso, se não (:) faça tal coisa

Se não fosse com react: deixa a div vazia se for fazer tal coisa insira na div

**OnClick** - quando tocar faça tal coisa / função

Quando o componente precisa de interação, ele precisa ser renderizado no cliente / ‘use client’ é algo do nextjs

Só mantém o async porque puxa os dados do supabase, e isso faz com que dê um probleminha no client

Para que o componente funcione tem que alterar o state e props

Como passar ele para outro canto: utilizar atributos das props, na page principal eu digo que ele vai receber e na outra eu declaro fisicamente e passo o ternário

Qaundo adiciona um contexto, tem qeu se adicionar também nas outras páginas que ele é usado

Importa um a um apenas o que será usado

Contexto é bom ~~pa~~ra organizar código

```jsx
          {books.map(book => (
            <div key={book.id}>
              <p>{book.name}</p>
              <button 
                value={book.id}
                onClick={(e) => handleSelectBook(e.target.value)}
                className="mt-1 ml-1 py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-[#debcbe] text-white hover:bg-pink-500 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 transition-all text-sm dark:bg-gray-800 dark:hover:bg-gray-600 dark:focus:ring-offset-gray-800"
              >
                Veja mais
              </button>
            </div>
          ))}
```

0x1h3pgb6XTSZYkA