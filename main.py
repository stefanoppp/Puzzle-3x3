import numpy as np
import random
class Puzzle:
    
    def __init__(self,original,copia):
        self.original=original
        self.copia=copia
            
    def sort_matrix(self):
        count=0
        while count<1:
            self.random_move(self.copia)
            self.random_move(self.original)
            count=count+1
        print(self.copia)
        print(self.original)
        
    def random_solve(self):
        print("Resolviendo matriz aleatoriamente...")
        intentos=0
        print("Matriz inicial desordenada: \n",self.copia)
        while np.array_equiv(self.copia,self.original)==False:
            self.random_move(self.copia)
            intentos+=1
        print("Matriz final ordenada: \n",self.copia)
        print("Intentos: ",intentos)
        
    def metodo_bidireccional(self):
        print("Resolviendo matriz bidireccionalmente...")
        movimientos=0
        movimientos_original=[]
        movimientos_copia=[]
        print(self.copia)
        print(self.original)
    # while True:
        # movimiento en la copia
        if np.array_equiv(self.copia,self.original)==False:
            self.random_move(self.copia)
            movimientos_copia.append(self.copia)
            movimientos=movimientos+1
         # movimiento en la original. Reevaluamos condicion
            if np.array_equiv(self.original,self.copia)==False:
                self.random_move(self.copia)
                movimientos_original.append(self.original)
                
        if np.array_equiv(self.copia,self.original)==True:
            print(self.original)
            print(self.copia)
            i=0
            print("Solucion: ")
            # mostramos la ruta que hizo para solucionar el puzzle
            # for matriz in movimientos_original:
            #     print(matriz)
        print("Matrices Finales: \n")
        print(self.copia)
        
        print(self.original)        
            # break
            # posiblemente haya q multiplicar por el len() del movimientos copia o orginial
        print("Movimientos: ",movimientos)
        
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
pz.sort_matrix()
# pz.random_solve()
# pz.metodo_bidireccional()
