import numpy as np
import random
class Puzzle:
    
    def __init__(self,inicial_state):
        self.inicial_state=inicial_state
        
    def movement(self):
        # averiguamos el cero
        print(self.inicial_state)
        print("\t")
        count=0
        while count<=49:
            cero=np.where(self.inicial_state==0)
            row_num=cero[0]
            column_num=cero[1]
            # seleccionamos metodo a invocar
            movements=["column_move","row_move"]
            movement=random.choice(movements)
            if movement=="column_move":
                self.column_move(row_num,column_num)
            if movement=="row_move":
                self.row_move(row_num,column_num)
            count=count+1
        print(self.inicial_state)
        
        
    def column_move(self,row_num,column_num):
        if column_num==0:
            aux=self.inicial_state[row_num, column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num, column_num+1]
            self.inicial_state[row_num, column_num+1]=aux
        if column_num==2:
            aux=self.inicial_state[row_num,column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num, column_num-1]
            self.inicial_state[row_num, column_num-1]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=self.inicial_state[row_num, column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num, column_num+random_number]
            self.inicial_state[row_num, column_num+random_number]=aux      
     # mover filas
    def row_move(self,row_num,column_num):
        if row_num==0:
            aux=self.inicial_state[row_num, column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num+1, column_num]
            self.inicial_state[row_num+1, column_num]=aux
        if row_num==2:
            aux=self.inicial_state[row_num,column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num-1, column_num]
            self.inicial_state[row_num-1, column_num]=aux
        else:
            numbers=[1,-1]
            random_number=random.choice(numbers)
            aux=self.inicial_state[row_num, column_num]
            self.inicial_state[row_num, column_num]=self.inicial_state[row_num+random_number, column_num]
            self.inicial_state[row_num+random_number, column_num]=aux 


np_matrix=np.matrix('1 2 3; 4 5 6; 7 8 0')
pz=Puzzle(np_matrix)
pz.movement()        