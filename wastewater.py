"""There ia the main app"""
# Import Tkinter module and others
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Import functions:
import ww_calculations as cal

# Version of current release:
VERSION = "0.35"

# Create the Main Window of the app:


class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Создаем заголовок главного окна
        slogan = tk.Label(self,
                          text = "Расчет дождевого стока по СП 32.13330.2012"
                          )
        slogan.grid(row = 0,
                    column = 0,
                    sticky = W)

        # Add the Tabs in the Main Window:
        notebook = ttk.Notebook(self)

        # Add the Tab N1:
        notebook.add(cal.Tab1(notebook), text = "п.7.2. Определение среднегодовых объемов поверхностных сточных вод"
                                                "\n"
                     )

        # Add the Tab N2:
        notebook.add(cal.Tab2(notebook), text = "п.7.3. Определение расчетных объемов поверхностных сточных вод "
                                                "\nпри отведении на очистку"
                     )

        notebook.grid(row = 1,
                      column = 0,
                      sticky = W)

        # Creates the function for QUIT with an option to cancel:

        def callback():
            if messagebox.askyesno('Внимание!', 'Точно выйти?'):
                exit()

        # Creates the button for command QUIT

        quit_button = tk.Button(self,
                                text = "ВЫХОД",
                                fg = "red",
                                command = callback
                                )
        quit_button.grid(row = 5, column = 0, sticky = E)

        # Создаем функцию для вызова текстового файла справки
        def write_faq():
            faq_window = Tk()
            faq_window.title("Справка:")
            faq_text_window = Text(faq_window, height = 20, width = 100)

            s_bar = Scrollbar(faq_window)
            s_bar.pack(side = RIGHT, fill = Y)
            s_bar.config(command = faq_text_window.yview)

            faq_text_window.config(yscrollcommand = s_bar.set)
            faq_text_window.pack()

            # Открывает файл, считывает текст, закрывает файл
            faq_file = open('FAQ.txt', 'r')
            faq_text = faq_file.read()
            faq_file.close()
            faq_text_window.insert(END, faq_text)

        # Creates the button for FAQ file
        faq_button = tk.Button(self,
                               text = "Справка",
                               command = write_faq,
                               fg = "black"
                               )
        faq_button.grid(row = 0, column = 0, sticky = E)

# Запуск главного окна


root = tk.Tk()
root.title("Расчет дождевого стока  v." + VERSION)
MainWindow(root).pack()
root.mainloop()
