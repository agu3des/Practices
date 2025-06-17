class Pais:
    def __init__(self, nomePais, nomeCapital, dimensao:int):
        self.__nomePais = nomePais
        self.__nomeCapital = nomeCapital
        self.__dimensao = dimensao
        self.__listaFronteiras = []
    
    @property
    def listaFronteiras(self):
        return self.__listaFronteiras.copy() #mostra só uma cópia e não o programa original / ñ catuca o seu
    # @property
    # def paisFronteira(self):
    #     return self.paisFronteira para pegar eu tenho que usar o mesmo nome da propriedade

    # @paisFronteira.setter
    # def paisFronteira(self, paisFronteira):
    #     if paisFronteira not in self.listaFronteiras:
    #         self.listaFronteiras.append(paisFronteira.title())
    #     return self.listaFronteiras
    #retira pq não é interessante

    def addFronteira(self, pais:str):
        '''
        Adiciona um país que faz fronteira com o object em questão.
        
        Argumentos
        ----------
        pais(str)? o país vai ser adicionado como de fronteira.

        Exceção
        -------
        Lança um Exception() quando tenta adicionar um país que já está cadastrado.
        '''
        if pais.title() not in self.__listaFronteiras:
            self.__listaFronteiras.append(pais.title())
        raise Exception(f'O país: {pais} já está resgistrado como fronteirisso do {self.__nomePais}.')
    #para exceção p/ criar um objeto vc abre um raise e o nome do objeto

    def fazFronteiraCom(self, outroPais: 'Pais')->bool:
     return True if outroPais.__nomePais in self.__listaFronteiras else False

    def __str__(self):
        return f'{self.__nomePais},capital  {self.__nomeCapital}, {self.__dimensao} Km²'
