# Created by Abdurasul Rakhmatullayev
# Telegram: https://t.me/noname_091

# loading required libraries 
from tkinter import ttk 
import tkinter as tk

# creating a window
window = tk.Tk()
window.config(width=1100,  height=600, padx=40, pady=40,)
window.title(string="Diagram") # window title text

diagram = tk.Canvas(master=window, background='RoyalBlue', width=900, height=400)
diagram.create_rectangle(40, 150, 200, 250, outline="white", width=4)
diagram.create_text((120, 200), text="Сбор образцов", font="Centaury", fill='white')
diagram.create_line(200, 200, 240, 200, fill='white', width=4, arrow="last")
diagram.create_rectangle(240, 150, 400, 250, outline="white", width=4)
diagram.create_text((320, 175), text="Выделение", font="Centaury", fill='white')
diagram.create_text((320, 200), text="образцов/ПЦР", font="Centaury", fill='white')
diagram.create_text((320, 225), text="(EGFR)", font="Centaury", fill='white')

diagram.create_line(400, 200, 440, 100, fill='white', width=2, arrow="last")
diagram.create_line(400, 200, 440, 300, fill='white', width=2, arrow="last")

diagram.create_rectangle(440, 50, 600, 150, outline="white", width=4)
diagram.create_text((520, 100), text="Да (56)", font="Centaury", fill='white')
diagram.create_line(600, 100, 640, 75, fill='white', width=2, arrow="last")
diagram.create_line(600, 100, 640, 200, fill='white', width=2, arrow="last")

diagram.create_rectangle(440, 250, 600, 350, outline="white", width=4)
diagram.create_text((520, 300), text="Нет (39)", font="Centaury", fill='white')
diagram.create_line(600, 300, 640, 325, fill='white', width=2, arrow="last")

diagram.create_rectangle(640, 25, 800, 125, outline="white", width=4)
diagram.create_text((720, 65), text="Статистическая", font="Centaury", fill='white')
diagram.create_text((720, 80), text="обработка данных", font="Centaury", fill='white')
diagram.create_rectangle(640, 150, 800, 250, outline="white", width=4)
diagram.create_text((720, 170), text="Ассоциативный", font="Centaury", fill='white')
diagram.create_text((720, 190), text="анализ с", font="Centaury", fill='white')
diagram.create_text((720, 210), text="биохимическими", font="Centaury", fill='white')
diagram.create_text((720, 230), text="маркерами", font="Centaury", fill='white')
diagram.create_rectangle(640, 275, 800, 375, outline="white", width=4)
diagram.create_text((720, 310), text="NGS (Рандоммные", font="Centaury", fill='white')
diagram.create_text((720, 345), text="-N10)", font="Centaury", fill='white')
diagram.pack()

# run
window.mainloop()