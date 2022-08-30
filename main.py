import numpy as np
import random
class Puzzle:
    
    def __init__(self,original,copia):
        self.original=original
        self.copia=copia
            
    def sort_matrix(self):
        count=0
        while count<2:
            self.random_move(self.copia)
            count=count+1
        return self.copia
        
    def random_solve(self):
        print("Resolviendo matriz aleatoriamente...")
        intentos=0
        print("Matriz inicial desordenada: \n",self.copia)
        while np.array_equiv(self.copia,self.original)==False:
            self.random_move(self.copia)
            intentos+=1
        print("Matriz final ordenada: \n",self.copia)
        print("Intentos: ",intentos)
        
    def obtener_nodos_hijos(self,matrix):
        copia=np.copy(matrix)
        cero=np.where(copia==0)
        row_num=cero[0]
        column_num=cero[1]
        nodos=[]
        # tratamos filas----------------------------
        if row_num==0:
            aux=copia[row_num+1,column_num]
            copia[row_num,column_num]=aux
            copia[row_num+1,column_num]=0
            nodos.append(copia)
            copia=np.copy(matrix)
            
        if row_num!=0 and row_num!=2:
            aux=copia[row_num+1,column_num]
            copia[row_num,column_num]=aux
            copia[row_num+1,column_num]=0
            # reestablecemos matriz
            nodos.append(copia)
            copia=np.copy(matrix)
            # ----------------------------------
            aux=copia[row_num-1,column_num]
            copia[row_num,column_num]=aux
            copia[row_num-1,column_num]=0
            nodos.append(copia)
            copia=np.copy(matrix)
            
        if row_num==2:
            aux=copia[row_num-1,column_num]
            copia[row_num,column_num]=aux
            copia[row_num-1,column_num]=0
            nodos.append(copia)
            copia=np.copy(matrix)
        # tratamos columnas---------------------------    
        if column_num==0:
            aux=copia[row_num,column_num+1]
            copia[row_num,column_num]=aux
            copia[row_num,column_num+1]=0
            nodos.append(copia)
            copia=np.copy(matrix)
            
        if column_num!=0 and column_num!=2:
            aux=copia[row_num,column_num+1]
            copia[row_num,column_num]=aux
            copia[row_num,column_num+1]=0
            nodos.append(copia)
            copia=np.copy(matrix)    
            
            aux=copia[row_num,column_num-1]
            copia[row_num,column_num]=aux
            copia[row_num,column_num-1]=0
            nodos.append(copia)
            copia=np.copy(matrix)               
                    
        if column_num==2:
            aux=copia[row_num,column_num-1]
            copia[row_num,column_num]=aux
            copia[row_num,column_num-1]=0
            nodos.append(copia)
            copia=np.copy(matrix)       

        return nodos
    def metodo_bidireccional(self):pass
        
    def random_move(self,matrix):
        cero=np.where(matrix==0)
        row_num=cero[0]
        column_num=cero[1]
        movements=["column_move","row_move"]
        movement=random.choice(movements)
        if movement=="column_move":
            self.column_move(row_num,column_num,matrix)
        if movement=="row_move":
            self.row_move(row_num,column_num,matrix)
                
    def column_move(self,row_num,column_num,matrix):
        if column_num==0:
            aux=matrix[row_num, column_num]
            matrix[row_num, column_num]=matrix[row_num, column_num+1]
            matrix[row_num, column_num+1]=aux
        if column_num==2:
            aux=matrix[row_num,column_num]
            matrix[row_num, column_num]=matrix[row_num, column_num-1]
            matrix[row_num, column_num-1]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=matrix[row_num, column_num]
            matrix[row_num, column_num]=matrix[row_num, column_num+random_number]
            matrix[row_num, column_num+random_number]=aux      
     # mover filas
    def row_move(self,row_num,column_num,matrix):
        if row_num==0:
            aux=matrix[row_num, column_num]
            matrix[row_num, column_num]=matrix[row_num+1, column_num]
            matrix[row_num+1, column_num]=aux
        if row_num==2:
            aux=matrix[row_num,column_num]
            matrix[row_num, column_num]=matrix[row_num-1, column_num]
            matrix[row_num-1, column_num]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=matrix[row_num, column_num]
            matrix[row_num, column_num]=matrix[row_num+random_number, column_num]
            matrix[row_num+random_number, column_num]=aux 


np_matrix_1=np.matrix('1 2 3; 4 5 6; 7 8 0')
np_matrix_2=np.matrix('1 2 3; 4 5 6; 7 8 0')
pz=Puzzle(np_matrix_1,np_matrix_2)

matriz_desordenada=pz.sort_matrix()

print("Matriz desordenada: ")
print(matriz_desordenada)

nodos_hijos=pz.obtener_nodos_hijos(matriz_desordenada)

pz.random_solve()
