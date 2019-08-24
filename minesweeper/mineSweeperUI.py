import tkinter as tk
import placingMines as mines
import mainFunction as mf

main_window = tk.Tk()
main_window.title('Minesweeper')
button_frame = tk.Frame(main_window)
button_frame.pack()
button_list = [[""]*10 for y in range(10)]
btn_texts = [[""]*10 for y in range(10)]

#Adding butons to UI    
for i in range(10):
    for j in range(10):
        btn_texts[i][j] = tk.StringVar()
        btn_texts[i][j].set("")
        button_list[i][j] = tk.Button(button_frame, textvariable=btn_texts[i][j], width=3,height = 1,borderwidth=1,
                                      state = 'normal', bg = 'lightgreen', command= lambda i=i , j=j: mf.showGrid(i,j))
        button_list[i][j].grid(row =i, column = j)
