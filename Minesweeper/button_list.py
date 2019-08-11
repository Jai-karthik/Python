#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[2]:


main_window = tk.Tk()
main_window.title('Minesweeper')
button_frame = tk.Frame(main_window)
button_frame.pack()


# In[3]:


button_names = []
btn_texts = [""]*100
for i in range(1,101,1):
    button_names.append("b"+str(i))
    btn_texts[i-1] = tk.StringVar()
    btn_texts[i-1].set("")
    #btn_texts[i-1].set("b"+str(i))


# In[4]:


temp_list = []
button_list = [[0]*10 for y in range(10)]
x = 0
for button in range(len(button_names)):
    button_names[button] = tk.Button(button_frame, textvariable=btn_texts[button], width=3,height = 1,borderwidth=1, state = 'normal')    
    temp_list.append(button_names[button])
    
for i in range(10):
    for j in range(10):
        button_list[i][j] = temp_list[x]
        x +=1


# In[5]:


for i in range(10):
    for j in range(10):
        button_list[i][j].grid(row =i, column = j)


# In[6]:


#main_window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




