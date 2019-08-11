#!/usr/bin/env python
# coding: utf-8

# In[1]:


import button_creation as bc
import random


# In[2]:


#bl.main_window.mainloop()


# In[3]:



x_mine = []
y_mine = []

for _ in range(10):
    x_mine.append(random.randint(0,9))
    y_mine.append(random.randint(0,9))
    
print(x_mine)
y_mine

# x_mine = [0, 5, 2, 0, 3, 8, 3, 3, 3, 8]
# y_mine = [7, 0, 7, 1, 8, 4, 2, 4, 9, 0]

    


# In[14]:


mines_matrix = [[0]*10 for y in range(10)]
mines_index = [] 
for i in range(10):
    mines_matrix[x_mine[i]][y_mine[i]] = 1
    mines_index.append([x_mine[i],y_mine[i]])
    

mines_matrix


# In[12]:


cell_indication = [[0]*10 for y in range(10)]


# In[15]:


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
            
cell_indication


# In[7]:


mines_index


# In[ ]:




