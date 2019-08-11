#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import Mines as mines


# In[2]:


main_window = tk.Tk()
main_window.title('Minesweeper')
button_frame = tk.Frame(main_window)
button_frame.pack()


# In[3]:


button_list = [[""]*10 for y in range(10)]
btn_texts = [[""]*10 for y in range(10)]

    
for i in range(10):
    for j in range(10):
        btn_texts[i][j] = tk.StringVar()
        btn_texts[i][j].set("") 
        button_list[i][j] = tk.Button(button_frame, textvariable=btn_texts[i][j], width=3,height = 1,borderwidth=1,
                                      state = 'normal', bg = 'lightgreen', command= lambda i=i , j=j: showGrid(i,j))
        button_list[i][j].grid(row =i, column = j) 


# In[4]:


def showGrid(x,y):
    row1 = button_list[x][y].grid_info()['row']      # Row of the button
    column1 = button_list[x][y].grid_info()['column']   # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)
    print("Grid position of 'btn': {} {}".format(row1, column1))
    print(mines.mines_matrix[x][y])
    btn_texts[x][y].set(str(x)+','+str(y))
    btn_texts[x][y].set(mines.cell_indication[x][y])
    zero_list = []
    
    if(mines.cell_indication[x][y] == '*'):
        for a in mines.mines_index:
            x = a[0]
            y = a[1]
            btn_texts[x][y].set(mines.cell_indication[x][y])
            button_list[x][y].configure(bg = 'red')
            
            
    
   
    if(mines.cell_indication[x][y] == 0 and [x,y] not in zero_list):
        zero_list.append([x,y])
        for a in zero_list:
            x = a[0]
            y = a[1]
                   
            if(x-1 >= 0):
                if(y-1 >=0):
                    if(mines.cell_indication[x-1][y-1] == 0 and [x-1,y-1] not in zero_list):
                        zero_list.append([x-1,y-1])
                if(y>=0 and y<=9):
                    if(mines.cell_indication[x-1][y] == 0 and [x-1,y] not in zero_list):
                        zero_list.append([x-1,y])
                if(y+1<=9):
                    if(mines.cell_indication[x-1][y+1] == 0 and [x-1,y+1] not in zero_list):
                        zero_list.append([x-1,y+1])




            if(x>=0 and x<=9):
                if(y-1 >=0):
                    if(mines.cell_indication[x][y-1] == 0 and [x,y-1] not in zero_list):
                        zero_list.append([x,y-1])
                if(y+1<=9):
                    if(mines.cell_indication[x][y+1] == 0 and [x,y+1] not in zero_list):
                        zero_list.append([x,y+1])



            if(x+1 <= 9):
                if(y-1 >=0):
                    if(mines.cell_indication[x+1][y-1] == 0 and [x+1,y-1] not in zero_list):
                        zero_list.append([x+1,y-1])
                if(y>=0 and y<=9):
                    if(mines.cell_indication[x+1][y] == 0 and [x+1,y] not in zero_list):
                        zero_list.append([x+1,y])
                if(y+1<=9):
                    if(mines.cell_indication[x+1][y+1] == 0 and [x+1,y+1] not in zero_list):
                        zero_list.append([x+1,y+1])
            
        
        for a in zero_list:
            x = a[0]
            y = a[1]
            if(x-1 >= 0):
                if(y-1 >=0):
                    btn_texts[x-1][y-1].set("" if mines.cell_indication[x-1][y-1]==0 else mines.cell_indication[x-1][y-1])
                    button_list[x-1][y-1].configure( state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y-1].set(mines.cell_indication[x-1][y-1])
                    
                if(y>=0 and y<=9):
                    btn_texts[x-1][y].set("" if mines.cell_indication[x-1][y] == 0 else mines.cell_indication[x-1][y])
                    button_list[x-1][y].configure( state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y].set(mines.cell_indication[x-1][y])
                    
                if(y+1<=9):
                    btn_texts[x-1][y+1].set("" if mines.cell_indication[x-1][y+1] == 0 else mines.cell_indication[x-1][y+1])
                    button_list[x-1][y+1].configure( state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y+1].set(mines.cell_indication[x-1][y+1])
                   



            if(x>=0 and x<=9):
                if(y-1 >=0):
                    btn_texts[x][y-1].set("" if mines.cell_indication[x][y-1] == 0 else mines.cell_indication[x][y-1])
                    button_list[x][y-1].configure( state= 'disabled', bg = 'lightgrey')
                   # btn_texts[x][y-1].set(mines.cell_indication[x][y-1])
                   
                if(y+1<=9):
                    btn_texts[x][y+1].set("" if mines.cell_indication[x][y+1] == 0 else mines.cell_indication[x][y+1])
                    button_list[x][y+1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x][y+1].set(mines.cell_indication[x][y+1])
                    



            if(x+1 <= 9):
                if(y-1 >=0):
                    btn_texts[x+1][y-1].set("" if mines.cell_indication[x+1][y-1] == 0 else mines.cell_indication[x+1][y-1])
                    button_list[x+1][y-1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y-1].set(mines.cell_indication[x+1][y-1])
                  
                if(y>=0 and y<=9):
                    btn_texts[x+1][y].set("" if mines.cell_indication[x+1][y] == 0 else mines.cell_indication[x+1][y])
                    button_list[x+1][y].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y].set(mines.cell_indication[x+1][y])
                    
                if(y+1<=9):
                    btn_texts[x+1][y+1].set("" if mines.cell_indication[x+1][y+1] ==0 else mines.cell_indication[x+1][y+1])
                    button_list[x+1][y+1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y+1].set(mines.cell_indication[x+1][y+1])
                    
            
            
   
    print(zero_list)
    print(len(zero_list))
        
#         if(mines.cell_indication[x-1][y-1] == 0):
#             zero_list.append([x-1,y-1])
#         if(mines.cell_indication[x-1][y] == 0):
#             zero_list.append([x-1,y])
#         if(mines.cell_indication[x-1][y+1] == 0):
#             zero_list.append([x-1,y+1])
        
#         if(mines.cell_indication[x][y-1] == 0):
#             zero_list.append([x,y-1])
#         if(mines.cell_indication[x][y+1] == 0):
#             zero_list.append([x,y+1])
        
#         if(mines.cell_indication[x+1][y-1] == 0):
#             zero_list.append([x+1,y-1])
#         if(mines.cell_indication[x+1][y] == 0):
#             zero_list.append([x+1,y])
#         if(mines.cell_indication[x+1][y+1] == 0):
#             zero_list.append([x+1,y+1])
#     except:
#         pass
    
    

#     if (mines.mines_matrix[x][y] == 0):
#         if(x==0):
#             if(y==0):
#                 btn_texts[x][y].set(mines.mines_matrix[x][y+1] + mines.mines_matrix[x+1][y+1] + mines.mines_matrix[x+1][y])
#             elif(y>0 and y<9):
#                 btn_texts[x][y].set(mines.mines_matrix[x][y-1] + mines.mines_matrix[x][y+1] + 
#                                     mines.mines_matrix[x+1][y-1] + mines.mines_matrix[x+1][y] + mines.mines_matrix[x+1][y+1])
#             elif(y==9):
#                 btn_texts[x][y].set(mines.mines_matrix[x][y-1] + 
#                                     mines.mines_matrix[x+1][y-1] + mines.mines_matrix[x+1][y])
#         elif(x>0 and x<9):
#             if(y==0):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y] + mines.mines_matrix[x-1][y+1] + 
#                                     mines.mines_matrix[x][y+1] +
#                                     mines.mines_matrix[x+1][y] + mines.mines_matrix[x+1][y+1] )
#             elif(y>0 and y<9):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y-1] + mines.mines_matrix[x-1][y] + mines.mines_matrix[x-1][y+1] +
#                                     mines.mines_matrix[x][y-1] + mines.mines_matrix[x][y+1] +
#                                     mines.mines_matrix[x+1][y-1] + mines.mines_matrix[x+1][y] + mines.mines_matrix[x+1][y+1]) 
                                    
#             elif(y==9):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y-1] + mines.mines_matrix[x-1][y] + 
#                                     mines.mines_matrix[x][y-1] + 
#                                     mines.mines_matrix[x+1][y-1] + mines.mines_matrix[x+1][y])
#         elif(x==9):
#             if(y==0):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y] + mines.mines_matrix[x-1][y+1]
#                                     + mines.mines_matrix[x][y+1])
                                    
#             elif(y>0 and y<9):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y-1] + mines.mines_matrix[x-1][y] + mines.mines_matrix[x-1][y+1]+
#                                     mines.mines_matrix[x][y-1]  + mines.mines_matrix[x][y+1])                                  
                                    
#             elif(y==9):
#                 btn_texts[x][y].set(mines.mines_matrix[x-1][y-1] + mines.mines_matrix[x-1][y] +
#                                     mines.mines_matrix[x][y-1] )
#     else:
#         btn_texts[x][y].set('*')     


# In[5]:


def displayUI():
    main_window.mainloop()


# In[6]:


displayUI()


# In[ ]:





# In[ ]:




