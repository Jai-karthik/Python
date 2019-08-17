#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


x_mine = []
y_mine = []

for _ in range(10):
    x_mine.append(random.randint(0,9))
    y_mine.append(random.randint(0,9))


# In[ ]:


mines_matrix = [[0]*10 for y in range(10)]
mines_index = [] 
for i in range(10):
    mines_matrix[x_mine[i]][y_mine[i]] = 1
    mines_index.append([x_mine[i],y_mine[i]])


# In[ ]:


cell_indication = [[0]*10 for y in range(10)]


# In[ ]:


for x in range(10):
    for y in range(10):
        if (mines_matrix[x][y] == 0):
            if(x==0):
                if(y==0):
                    cell_indication[x][y] =mines_matrix[x][y+1] + mines_matrix[x+1][y+1] + mines_matrix[x+1][y]
                elif(y>0 and y<9):
                    cell_indication[x][y] =mines_matrix[x][y-1] + mines_matrix[x][y+1] + mines_matrix[x+1][y-1] + mines_matrix[x+1][y] + mines_matrix[x+1][y+1]
                elif(y==9):
                    cell_indication[x][y] =mines_matrix[x][y-1] +  mines_matrix[x+1][y-1] + mines_matrix[x+1][y]
            elif(x>0 and x<9):
                if(y==0):
                    cell_indication[x][y] =mines_matrix[x-1][y] + mines_matrix[x-1][y+1] +  mines_matrix[x][y+1] + mines_matrix[x+1][y] + mines_matrix[x+1][y+1] 
                elif(y>0 and y<9):
                    cell_indication[x][y] =mines_matrix[x-1][y-1] + mines_matrix[x-1][y] + mines_matrix[x-1][y+1] + mines_matrix[x][y-1] + mines_matrix[x][y+1] + mines_matrix[x+1][y-1] + mines_matrix[x+1][y] + mines_matrix[x+1][y+1]

                elif(y==9):
                    cell_indication[x][y] =mines_matrix[x-1][y-1] + mines_matrix[x-1][y] + mines_matrix[x][y-1] + mines_matrix[x+1][y-1] + mines_matrix[x+1][y]
            elif(x==9):
                if(y==0):
                    cell_indication[x][y] =mines_matrix[x-1][y] + mines_matrix[x-1][y+1]  + mines_matrix[x][y+1]

                elif(y>0 and y<9):
                    cell_indication[x][y] =mines_matrix[x-1][y-1] + mines_matrix[x-1][y] + mines_matrix[x-1][y+1]+ mines_matrix[x][y-1]  + mines_matrix[x][y+1]                                

                elif(y==9):
                    cell_indication[x][y] =mines_matrix[x-1][y-1] + mines_matrix[x-1][y] + mines_matrix[x][y-1] 
        else:
            cell_indication[x][y] ='*'


# In[ ]:




