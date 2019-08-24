#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from placingMines import cell_indication, mines_matrix, mines_index
import mineSweeperUI as ui


# In[4]:


def showGrid(x,y):
    row1 = ui.button_list[x][y].grid_info()['row']      # Row of the button
    column1 = ui.button_list[x][y].grid_info()['column']   # grid_info will return dictionary with all grid elements (row, column, ipadx, ipday, sticky, rowspan and columnspan)
    print("Grid position of 'btn': {} {}".format(row1, column1))
    #print(mines_matrix[x][y])
    ui.btn_texts[x][y].set(str(x)+','+str(y))
    ui.btn_texts[x][y].set(cell_indication[x][y])
    zero_list = []

    if(cell_indication[x][y] == '*'):
        for a in mines_index:
            x = a[0]
            y = a[1]
            ui.btn_texts[x][y].set(cell_indication[x][y])
            ui.button_list[x][y].configure(bg = 'red')

        for x in range(10):
            for y in range(10):
                ui.button_list[x][y].configure(state = 'disabled')




    if(cell_indication[x][y] == 0 and [x,y] not in zero_list):
        zero_list.append([x,y])
        for a in zero_list:
            x = a[0]
            y = a[1]

            if(x-1 >= 0):
                if(y-1 >=0):
                    if(cell_indication[x-1][y-1] == 0 and [x-1,y-1] not in zero_list):
                        zero_list.append([x-1,y-1])
                if(y>=0 and y<=9):
                    if(cell_indication[x-1][y] == 0 and [x-1,y] not in zero_list):
                        zero_list.append([x-1,y])
                if(y+1<=9):
                    if(cell_indication[x-1][y+1] == 0 and [x-1,y+1] not in zero_list):
                        zero_list.append([x-1,y+1])




            if(x>=0 and x<=9):
                if(y-1 >=0):
                    if(cell_indication[x][y-1] == 0 and [x,y-1] not in zero_list):
                        zero_list.append([x,y-1])
                if(y+1<=9):
                    if(cell_indication[x][y+1] == 0 and [x,y+1] not in zero_list):
                        zero_list.append([x,y+1])



            if(x+1 <= 9):
                if(y-1 >=0):
                    if(cell_indication[x+1][y-1] == 0 and [x+1,y-1] not in zero_list):
                        zero_list.append([x+1,y-1])
                if(y>=0 and y<=9):
                    if(cell_indication[x+1][y] == 0 and [x+1,y] not in zero_list):
                        zero_list.append([x+1,y])
                if(y+1<=9):
                    if(cell_indication[x+1][y+1] == 0 and [x+1,y+1] not in zero_list):
                        zero_list.append([x+1,y+1])


        for a in zero_list:
            x = a[0]
            y = a[1]
            if(x-1 >= 0):
                if(y-1 >=0):
                    ui.btn_texts[x-1][y-1].set("" if cell_indication[x-1][y-1]==0 else cell_indication[x-1][y-1])
                    ui.button_list[x-1][y-1].configure( state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y-1].set(cell_indication[x-1][y-1])

                if(y>=0 and y<=9):
                    ui.btn_texts[x-1][y].set("" if cell_indication[x-1][y] == 0 else cell_indication[x-1][y])
                    ui.button_list[x-1][y].configure(state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y].set(cell_indication[x-1][y])

                if(y+1<=9):
                    ui.btn_texts[x-1][y+1].set("" if cell_indication[x-1][y+1] == 0 else cell_indication[x-1][y+1])
                    ui.button_list[x-1][y+1].configure( state= 'disabled', bg = 'lightgrey')
#                     btn_texts[x-1][y+1].set(cell_indication[x-1][y+1])




            if(x>=0 and x<=9):
                if(y-1 >=0):
                    ui.btn_texts[x][y-1].set("" if cell_indication[x][y-1] == 0 else cell_indication[x][y-1])
                    ui.button_list[x][y-1].configure( state= 'disabled', bg = 'lightgrey')
                   # btn_texts[x][y-1].set(cell_indication[x][y-1])

                if(y+1<=9):
                    ui.btn_texts[x][y+1].set("" if cell_indication[x][y+1] == 0 else cell_indication[x][y+1])
                    ui.button_list[x][y+1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x][y+1].set(cell_indication[x][y+1])




            if(x+1 <= 9):
                if(y-1 >=0):
                    ui.btn_texts[x+1][y-1].set("" if cell_indication[x+1][y-1] == 0 else cell_indication[x+1][y-1])
                    ui.button_list[x+1][y-1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y-1].set(cell_indication[x+1][y-1])

                if(y>=0 and y<=9):
                    ui.btn_texts[x+1][y].set("" if cell_indication[x+1][y] == 0 else cell_indication[x+1][y])
                    ui.button_list[x+1][y].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y].set(cell_indication[x+1][y])

                if(y+1<=9):
                    ui.btn_texts[x+1][y+1].set("" if cell_indication[x+1][y+1] ==0 else cell_indication[x+1][y+1])
                    ui.button_list[x+1][y+1].configure( state= 'disabled', bg = 'lightgrey')
                    #btn_texts[x+1][y+1].set(cell_indication[x+1][y+1])

    #print(zero_list)
    #print(len(zero_list))




# In[ ]:





# In[ ]:





# In[ ]:
