import numpy as np

class HashTable:
    '''
    Tabela Hash usando a técnica de sondagem linear para tratamento de colisão 
    '''
    def __init__(self,size=10):
        self.__ocupados = 0 #como é dispersa, se n tiver contador tem que varrer toda vez
        self.__table = np.full(size,None) #array, posso pedir o len do array logo n é necessário um atributo tamanho
        self.__keys = [None]*size
        self.__values = [None]*size

    def __hash(self,key:any)->int:
        '''
        Cálculo do hash modular
        '''
        return hash(key) % len(self.__table) #hash é de python/faz só por isso só tem a chave
                            #é o nosso m
    
    def __rh(self,index:int):
        return (index+1) % len(self.__table)

    def isFull(self):
        return self.__ocupados == len(self.__table)

    def put(self, key:any, data:any):
        if self.isFull():
            return False
        hashData = self.__hash(key)
        print(f'Valor de hash {hashData} para o par ({key}, {data}).')

        while self.__table[hashData] != None:
            hashData = self.__rh(hashData)
            print(f'Valor de rehash {hashData} para o par ({key}, {data}).')
        self.__table[hashData] = data
        self.__ocupados += 1

    def get(self, key:any)->any:
        index = self.__hash(key)
        initial_index = index
        while self.__keys[index] is not None:
            if self.__keys[index] == key:
                return self.__keys[index], self.__values[index]
            index = (index + 1) % len(self.__table)
            if index == initial_index:  # Verifica se voltou ao ponto inicial
                break
        return None, None  # Retorna None se a chave não for encontrada

    def search(self, key):
        index = self.__hash(key)
        while self.__table[index] is not None:
            if self.__table[index] == key:
                return index
            index = (index + 1) % len(self.__table)
        return None

    def remove(self, key):
        index = self.search(self.__hash)
        if index is not None:
            self.__table[index] = None
            print(f"Chave {key} removida da tabela hash.")
        else:
            print(f"Chave {key} não encontrada na tabela hash.")

    def __str__(self):
        return str(self.__table)

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        '''
        Fazer a pesquisa utilizando os cholchetes. ex: ht[2] = 99
        '''
        self.put(key, data)