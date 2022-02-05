import requests
from bs4 import BeautifulSoup
import csv
import time
from tkinter import ttk
from ttkthemes import ThemedTk
block_ulrs = []
def clicked():
    separator = int(Sep_txt.get())
    delay = int(delay_combobox.get())
    for i in range (0, separator, 1):
        time.sleep(delay)
        url = Link_txt.get()+str(i)
        print(url)
        q = requests.get (url)
        result = q.content
        soup = BeautifulSoup (result, 'lxml')
        blocks = soup.find_all (class_=Class_txt.get())

        for block in blocks:
            block_url = block.get ('href')
            block_ulrs.append ( block_url)

    with open ('test.csv', 'w') as file:
        for line in block_ulrs:
            file.write (f'{line}\n')


window = ThemedTk(theme = 'yaru')
window.geometry("1200x600")
window.wm_iconbitmap('myicon.ico')
window.title("Парсер данных")
Link_label = ttk.Label(window, text="Ссылка")
Link_label.grid(column=0, row=0,padx =20,pady=20 )
Link_txt = ttk.Entry(window,width=80)
Link_txt.grid(column=1, row=0)
Sep_txt = ttk.Entry(window, width=5)
Sep_txt.grid(column=2,row=0)
delay_combobox = ttk.Combobox(window,width = 4,values = [0,3,5,10,15])
delay_combobox.current(0)
delay_combobox.grid(column=3,row=0,)
Link_label = ttk.Label(window, text="Класс")
Link_label.grid(column=0, row=1,padx =20,pady=20 )
Class_txt = ttk.Entry(window,width=80)
Class_txt.grid(column=1, row=1)
Run_btn = ttk.Button(window, text="Клик!", command=clicked)
Run_btn.grid(column=4, row=0)
window.mainloop()