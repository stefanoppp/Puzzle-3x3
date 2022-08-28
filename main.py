import numpy as np
import random
class Puzzle:
    
    def __init__(self,original,copia):
        self.original=original
        self.copia=copia
            
    def sort_matrix(self):
        count=0
        while count<1:
            cero=np.where(self.copia==0)
            row_num=cero[0]
            column_num=cero[1]
            movements=["column_move","row_move"]
            movement=random.choice(movements)
            if movement=="column_move":
                self.column_move(row_num,column_num)
            if movement=="row_move":
                self.row_move(row_num,column_num)
            count=count+1
        
    def random_solve(self):
        print("Resolviendo matriz aleatoriamente...")
        intentos=0
        while np.array_equiv(self.copia,self.original)==False:
            cero=np.where(self.copia==0)
            row_num=cero[0]
            column_num=cero[1]
            movements=["column_move","row_move"]
            movement=random.choice(movements)
            if movement=="column_move":
                self.column_move(row_num,column_num)
            if movement=="row_move":
                self.row_move(row_num,column_num)
            intentos=intentos+1
        print("Intentos: ",intentos)
        
    def metodo_bidireccional(self):
        print("Resolviendo matriz bidireccionalmente...")
        movimientos=0
        movimientos_original=[]
        movimientos_copia=[]
        while True:
            # movimiento en la copia
            if np.array_equiv(self.copia,self.original)==False:
                cero=np.where(self.copia==0)
                row_num=cero[0]
                column_num=cero[1]
                movements=["column_move","row_move"]
                movement=random.choice(movements)
                if movement=="column_move":
                    self.column_move(row_num,column_num)
                if movement=="row_move":
                    self.row_move(row_num,column_num)
                movimientos_copia.append(self.copia)
                movimientos=movimientos+1
            # movimiento en la original
            if np.array_equiv(self.copia,self.original)==False:
                cero=np.where(self.original==0)
                row_num=cero[0]
                column_num=cero[1]
                movements=["column_move","row_move"]
                movement=random.choice(movements)
                if movement=="column_move":
                    self.column_move(row_num,column_num)
                if movement=="row_move":
                    self.row_move(row_num,column_num)
                movimientos_original.append(self.original)
                   
            # if np.array_equiv(self.copia,self.original)==True:
            print(self.original)
            print(self.copia)
                # i=0
                # print("Solucion: ")
                # # mostramos la ruta que hizo para solucionar el puzzle
                # for matriz in movimientos_copia:
                #     i=i+1
                #     print("Paso ",i," de",movimientos,":\n ",matriz)
                # break
            # posiblemente haya q multiplicar por el len() del movimientos copia o orginial
        print("Movimientos: ",movimientos)
                
    def column_move(self,row_num,column_num):
        if column_num==0:
            aux=self.copia[row_num, column_num]
            self.copia[row_num, column_num]=self.copia[row_num, column_num+1]
            self.copia[row_num, column_num+1]=aux
        if column_num==2:
            aux=self.copia[row_num,column_num]
            self.copia[row_num, column_num]=self.copia[row_num, column_num-1]
            self.copia[row_num, column_num-1]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=self.copia[row_num, column_num]
            self.copia[row_num, column_num]=self.copia[row_num, column_num+random_number]
            self.copia[row_num, column_num+random_number]=aux      
     # mover filas
    def row_move(self,row_num,column_num):
        if row_num==0:
            aux=self.copia[row_num, column_num]
            self.copia[row_num, column_num]=self.copia[row_num+1, column_num]
            self.copia[row_num+1, column_num]=aux
        if row_num==2:
            aux=self.copia[row_num,column_num]
            self.copia[row_num, column_num]=self.copia[row_num-1, column_num]
            self.copia[row_num-1, column_num]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=self.copia[row_num, column_num]
            self.copia[row_num, column_num]=self.copia[row_num+random_number, column_num]
            self.copia[row_num+random_number, column_num]=aux 


np_matrix_1=np.matrix('1 2 3; 4 5 6; 7 8 0')
np_matrix_2=np.matrix('1 2 3; 4 5 6; 7 8 0')
pz=Puzzle(np_matrix_1,np_matrix_2)
pz.sort_matrix()
# pz.random_solve()
pz.metodo_bidireccional()
