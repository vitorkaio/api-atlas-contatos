#coding: utf-8

from pymongo import MongoClient

class AtlasDB(object):
    ''' Classe que abstrai o acesso ao mongodb Atlas. '''

    def __init__(self, url, colecao, documento):
        ''' Construtor, passe a url, colecao e o documento da conexão do mongo.
        Args:
            url (str): url com da conexão com o mongodb.
            colecao (str): colecão que será utilizada.
            documento (str): documentos que será acessado.
        '''
        self.__cliente = MongoClient(url)
        self.__col = self.__cliente[colecao]
        self.__doc = self.__col[documento]
    
    def getAll(self, id):
        ''' Retorna todos os itens do banco de dados em ordem alfabética.
        Returns: 
            res (cursor): Um cursor com todas os itens do banco de dados.
        '''
        res = self.__doc.find({'user_id': id}).sort('name', 1)
        return res

    def getAllCampoSort(self, campo, sort):
        '''Retorna todos os itens pelo campo crescente ou descrescente. 
        Args:
            campo (str): Campo que será ordenado.(kcak, ferro, calcio).
            sort (int): O tipo de ordenação, 1 para crescente ou -1 para descrescente.
        Returns:
            res (cursor): Um cursor com todas os itens do banco de dados.
        '''
        res = self.__doc.find({}).sort(campo, sort)
        return res

    def getPorNome(self, nome):
        '''Pesquisa itens por nome.
        Args:
            nome (str): Nome que será pesquisado.
        Returns:
            res (cursor): Retorna um cursor com os resultado ou None.
        '''
        res = self.__doc.find({'nome': {"$regex": nome.title()}})
        return res

    def getPorId(self, idItem):
        '''Pesquisa itens pelo id.
        Args:
           idItem (int): id que será pesquisado no banco de dados.
        Returns: 
            res (cursor/bool): Um cursor se for encontrado, False caso constrário.
        '''
        try:
            id_pes = int(idItem)
            res = self.__doc.find({'numero': int(idItem)})
            print(res)
            return res
        except:
            return False
