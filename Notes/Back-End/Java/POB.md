# POB

- dao no eclipse
    
    baixar o aquivo do drive
    
    adicionar a pasta lib do professor, pegar os 3 arquivos e adicionar no buildpath 
    

```java
@Table(name = "Bolas")
@Collum(name = "material")
//Dá pra definir regras nesses tipo de renomeações
```

```java
*@Version*				//ativar controle de vers�o  do objeto
private long versao;

// Controla as versões, deve ser adicionado em cada classe que deseja-se controlar
// ele se autoincrementa, sendo: versão + 1
// ou seja, quando dois tentam acessar ao mesmo tempo o que conseguir primeiro vai mudar a versão e quando o outro for acessar ele vai tentar gravar uma versão antiga em um objeto que já foi alterado
// em resumo: controle de versionamento
```

```java
	public Produto readLock(Object chave){
		try{
			String nome = (String) chave;
			TypedQuery<Produto> q = manager.createQuery("select p from Produto p where p.nome = :x", Produto.class);

			q.setLockMode(LockModeType.PESSIMISTIC_WRITE);
			//******************************************

			q.setParameter("x", nome);
			Produto prod = q.getSingleResult();
			return prod;
		}catch(NoResultException e){
			return null;
		}
	} //o lock para que quando for ler ele bloquei
```

Pesquisar sobre não entidades e dto e cashe