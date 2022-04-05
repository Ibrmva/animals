from tkinter import *
from time import sleep
from random import randint, choice
import tkinter
from turtle import heading



class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        self.c = c
        self.a = []
        self.b = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            self.b.append([]) 
            for j in range(self.m):
                self.a[i].append(choice([0, 4]))
                self.a[i].append(0)
                self.b[i].append(0)
                if 4 == 1 and self.a[i][j] == 0:    
                    self.a[i][j] = 1    
                elif (randint(1,7) == 1) and self.a[i][j] == 0:    
                    self.a[i][j] = 2    
                elif (randint(1,5) == 1) and self.a[i][j] == 0:    
                    self.a[i][j] = 3
                elif(randint(5, 7) ==1) and self.a[i][j] == 0:
                    self.a[i][j] = 4       
        self.draw()

        
    def step(self):
        b = []
        for i in range(self.n): 
            b.append([])
            for j in range(self.m):
                b[i].append(0)
       
        for i in range(1, self.n - 1):     #№1 Lion VS Jackal
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 4]))
                self.a[i].append(0)
                if self.a[i][j] == 1:
                    neib_sum = self.a[i][j]
                    if neib_sum < 4 : #if jackals surround the lion
                        b[i][j] = 0 #died
                    elif neib_sum <  2: #if jackals surround the lion 
                        b[i][j] = 1 #alived
                    else:
                        b[i][j] = self.a[i][j]

        for i in range(1, self.n - 1):     #If Lions surround the jackals
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 4]))
                self.a[i].append(0)
                if self.a[i][j] == 2:
                    neib_sum = self.a[i - 1][j-1] + self.a[i-1][j] + self.a[i][j+1]
                    if neib_sum  >= 1 :
                        b[i][j] = 0
                    elif neib_sum == 0:
                        b[i][j] = 2
                    else:
                        b[i][j] = self.a[i][j]

        for i in range(1, self.n - 1):     # №2 Leoprd VS Rhinoceros
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 4]))
                self.a[i].append(0)
                if self.a[i][j] == 3:
                    neib_sum = self.a[i][j-1] + self.a[i][j] + self.a[i+1][j]
                    if neib_sum <= 4 or neib_sum >= 5: #if leopards surround the rhinoceros
                        b[i][j] = 1 #alived
                    elif neib_sum == 11: 
                        b[i][j] = 0 #died
                    else:
                        b[i][j] = self.a[i][j]

        for i in range(1, self.n - 1):     
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 4]))
                self.a[i].append(0)
                if self.a[i][j] == 4:
                    neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] #if rhinoceros surround leopards 
                    if neib_sum < 2 or neib_sum > 3:
                        b[i][j] = 0 #died
                    elif neib_sum == 0:
                        b[i][j] = 4
                    else:
                        b[i][j] = self.a[i][j]

        self.a = b
        
                    
    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()
 
    def draw(self):
       
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "yellow"  #Lion 
                elif (self.a[i][j] == 2):
                    color = "brown" #Jackals
                elif (self.a[i][j] == 3):
                    color = "red" #Rhinoceros
                elif (self.a[i][j] ==4 ):
                    color = "pink" #Leoprd
                else:
                    color = "light green"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

        
root = tkinter.Tk()

root.geometry("1600x1600")
c = Canvas(root, width=1600, height=1600)
c.pack()

f = Field(c, 40, 40, 1600, 1600)
f.print_field()


root.mainloop()

