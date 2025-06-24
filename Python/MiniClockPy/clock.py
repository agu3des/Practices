from tkinter import *
from datetime import datetime

color1 = '#1D1316'#black
color2 = '#fafcff'#white
color3 = '#C12B63'#pink
color4 = '#eb463b'#salmon
color5 = '#E486B3'#baby pink
color6 = '#FFFFFF'#white

window = Tk()
window.title('')
window.geometry('400x180')
window.resizable(width=FALSE, height=FALSE)
window.configure(background=color1)

def upgradeClock():
    time = datetime.now()
    hour = time.strftime('%H:%M:%S')
    weekDay = time.strftime('%A')
    day = time.day
    month =  time.strftime('%b')
    year = time.strftime('%Y')
    
    l1.config(text=hour)
    l2.config(text=f'{weekDay}\u00a0 {day}/{month}/{year}')

    l1.after(200, upgradeClock)

l1 = Label(window, text='10:05:05', font=('Times New Roman', 70), bg=color1, fg=color3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(window, font=('Times New Roman', 20), bg=color1, fg=color5)
l2.grid(row=1, column=0, sticky=NW, padx=5)

upgradeClock()

window.mainloop()