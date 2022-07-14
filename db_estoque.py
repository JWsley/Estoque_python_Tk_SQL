from re import X
import mysql.connector


from class_estoque import Estoque
from class_fabric import Fabric
from class_info import *
class Db_estoque:

    def __init__(self):
        self.cConnect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'estoque'
        ) 
        self.mycursor = self.cConnect.cursor()
        self.Estq = Estoque()
        self.fabr = Fabric()
        self.quan_inicial = 0
        self.verifyx = bool
        self.pls = []

        

    def exib(self):
        self.mycursor.execute('select * from estoque'  )
        list = self.mycursor.fetchall()
        for i in list:
           print('==================================================')
           print("•",i,">>>")
           print('==================================================')

#U


    def update(self):
        nome  = input('Informe um novo nome:')
        cod  = int(input('Informe o codigo:'))
        sql = f'update pessoas set nome = "{nome}" where id="{cod}"'
        self.mycursor.execute(sql)
        self.cConnect.commit()





#D

    def delete(self):
        cod2  = int(input('Informe o codigo:'))
        sql2 = f'delete from pessoas 2 where id = {cod2}'
        self.mycursor.execute(sql2)
        self.conexao.commit()



    def cadastrar_produto(self,nome,fabric_des):
        list = []
        codl = []

        self.mycursor.execute(f'select nomeFabri from fabricante;')
        var = self.mycursor.fetchall()

        for i  in var:
            list.append(var)
           
        liststr = str(list)
        
       
        print('----------------------------- -----------------------------\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

        
        if fabric_des in liststr:
            print('.............  ............................... ............... ............ .......... ........ ....')
            
            self.mycursor.execute('select count(cod) from produto')
            code =self.mycursor.fetchall()
            print(code)

         
            codein = str(code).replace('[','').replace(']','').replace('(','').replace(',','').replace(')','')
            codint = int(codein)+1
            codf = str(codint).replace('[','').replace(']','').replace('(','').replace(',','').replace(')','')
            print(codf)
            codfinal = int(codf)
            print(codfinal)

            executesql = f'insert into produto (nome,empr,quan) value ("{nome}","{fabric_des}",{self.quan_inicial})'
            self.mycursor.execute(executesql)
            self.cConnect.commit() 
            self.Estq.armazena.append(Info(cod =codfinal,nome=nome,fabric=fabric_des,quan=self.quan_inicial))
            print('Cadastro efetuado com sucesso!!!')
            self.verifyx = True
            return self.verifyx
        else:
            self.verifyx = False
            return self.verifyx



    def listar_tudo(self):
        self.mycursor.execute('select * from  produto' )
        list = self.mycursor.fetchall()
        for i in list:
           print('==================================================')
           print("•",i,">>>")
           print('==================================================')



    def listar_unidade(self,code):
        
        if code == '':
            self.mycursor.execute('select * from  produto' )
            list = self.mycursor.fetchall()
            
            for i in list:
                exib = (f' {i} ').replace(',',' | ').replace("'",'♦').replace('(','╠{').replace(')','}╣')
                self.pls.append(exib)
        
        else:
            self.mycursor.execute(f'select * from  produto where cod={code}' )
            list = self.mycursor.fetchall()
            
            for i in list:
                exib = (f' {i} ').replace(',',' | ').replace("'",'♦').replace('(','╠{').replace(')','}╣')
                return exib

    
    def update_produto(self,code,new_name):
        self.mycursor.execute(f'update produto set nome = "{new_name}" where cod={code}' )
        self.cConnect.commit()
       


    


