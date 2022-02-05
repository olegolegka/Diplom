import requests
from bs4 import BeautifulSoup
import csv
import time
from tkinter import ttk, Frame
from ttkthemes import ThemedTk
block_ulrs = []


class Parser(Frame):
    def __init__(self):
        self.InitUi ()
        super ().__init__ ()


    def InitUi(self):
        self.window = ThemedTk (theme='yaru')
        self.window.geometry ("1200x600")
        self.window.wm_iconbitmap ('myicon.ico')
        self.window.title ("Парсер данных")
        self.Link_label = ttk.Label (self.window, text="Ссылка")
        self.Link_label.grid (column=0, row=0, padx=20, pady=20)
        self.Link_txt = ttk.Entry (self.window, width=80)
        self.Link_txt.grid (column=1, row=0)
        self.Sep_txt = ttk.Entry (self.window, width=5)
        self.Sep_txt.grid (column=2, row=0)
        self.delay_combobox = ttk.Combobox (self.window, width=4, values=[0, 3, 5, 10, 15])
        self.delay_combobox.current (0)
        self.delay_combobox.grid (column=3, row=0, )
        self.Link_label = ttk.Label (self.window, text="Класс")
        self.Link_label.grid (column=0, row=1, padx=20, pady=20)
        self.Class_txt = ttk.Entry (self.window, width=80)
        self.Class_txt.grid (column=1, row=1)
        self.Run_btn = ttk.Button (self.window, text="Клик!", command=self.clicked)
        self.Run_btn.grid (column=4, row=0)
        self.window.mainloop ()
    def clicked(self):
        '''
        Функция обработчик кнопки получения всех ссылок на товары
        '''
        print(self.Sep_txt.get())
        separator = int(self.Sep_txt.get ())
        delay = int (self.delay_combobox.get ())
        for i in range (0, separator, 1):
            time.sleep (delay)
            url = self.Link_txt.get () + str (i + 1)
            print (url)
            q = requests.get (url)
            result = q.content
            soup = BeautifulSoup (result, 'lxml')
            blocks = soup.find_all (class_=self.Class_txt.get ())

            for block in blocks:
                block_url = block.get ('href')
                block_ulrs.append (block_url)

        with open ('test.csv', 'w') as file:
            for line in block_ulrs:
                file.write (f'{line}\n')
def main():
    app = Parser()

if __name__ == '__main__':
    main()