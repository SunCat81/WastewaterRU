"""there are functions for calculations"""
# Import Tkinter module and others
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Create the Tab N1:


class Tab1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the label for an initial data for calculation:
        mylist = ["Исходные данные для расчета:",
                  "F - Площадь стока коллектора, га",  # f_sq
                  "Fм - Площадь твердых покрытий, подвергающихся мойке, га",  # f_msq
                  "Fу - Площадь очищаемая от снега , га",  # f_sn
                  "      (включая крыши с внутренними водостоками)",
                  "hд - слой осадков теплого перида года, мм",  # h_d
                  "hт - слой осадков холодного периода года, мм",  # h_t
                  "Uд - общий коэффициент стока дождевых вод (по умолчанию 0,95)",  # u_d
                  "Uт - общий коэффициент стока талых вод (0,5-0,7)",  # u_t
                  "m - удельный расход воды на мойку, принимается",  # m
                  "      0,5 для ручной и 1,2-1,5 л/м2 для механизированной мойки",
                  "k - среднее количество моек в году (100-150)",  # k
                  "Uм - коэффициент стока поливомоечных вод (0,5)"]  # u_m
        # Создаем переменную для сдвига
        shift = len(mylist)
        # Пробегаем по списку мойлист и создаем много-много текста
        for i in range(len(mylist)):
            self.label = tk.Label(self, text = '' + mylist[i])
            self.label.grid(row = i, column = 0, sticky = W)

        # Create the Entry: Переписать это все в цикл!
        self.f_sq_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.f_sq_e.grid(row = 1, column = 1, sticky = W)
        self.f_sq_e.insert(END, 10)

        self.f_msq_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.f_msq_e.grid(row = 2, column = 1, sticky = W)
        self.f_msq_e.insert(END, 0)

        self.f_sn_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.f_sn_e.grid(row = 3, column = 1, sticky = W)
        self.f_sn_e.insert(END, 0)

        self.h_d_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.h_d_e.grid(row = 5, column = 1, sticky = W)
        self.h_d_e.insert(END, 0)

        self.h_t_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.h_t_e.grid(row = 6, column = 1, sticky = W)
        self.h_t_e.insert(END, 0)

        self.u_t_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.u_t_e.grid(row = 8, column = 1, sticky = W)
        self.u_t_e.insert(END, 0.5)

        self.m_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.m_e.grid(row = 9, column = 1, sticky = W)
        self.m_e.insert(END, 1.2)

        self.k_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.k_e.grid(row = 11, column = 1, sticky = W)
        self.k_e.insert(END, 100)

        self.u_m_e = ttk.Entry(self, justify = CENTER, width = 10)
        self.u_m_e.grid(row = 12, column = 1, sticky = W)
        self.u_m_e.insert(END, 0.5)

        # Create button for u_d:
        self.u_d_button = tk.Button(self,
                                    text = "Рассчитать",
                                    fg = "blue",
                                    command = self.on_show_ud
                                    )
        self.u_d_button.grid(row = 7, column = 1, sticky = W)

        # Create the main command button:
        self.solve_button = tk.Button(self,
                                      text = "ВЫПОЛНИТЬ РАСЧЕТ",
                                      fg = "blue",
                                      command = self.solve_rain
                                      )
        self.solve_button.grid(row = shift + 1, column = 4, sticky = W)

        # Create the entries to output data:
        # Шаг - создаем смещение для корректного размещения полей ввода
        step = 1

        # Среднегодовой объем поверхностных сточных вод
        self.raine_l1 = tk.Label(self, text = 'Среднегодовой объем ')
        self.raine_l2 = tk.Label(self, text = 'поверхностных сточных вод')
        self.raine_l1.grid(row = step + 1, column = 4, sticky = W)
        self.raine_l2.grid(row = step + 2, column = 4, sticky = W)
        self.rain_e = ttk.Entry(self, justify = CENTER, width = 15)
        self.rain_e.grid(row = step + 2, column = 5, sticky = W)
        self.raine_l3 = tk.Label(self, text = 'м3/год')
        self.raine_l3.grid(row = step + 2, column = 6, sticky = W)

        self.l3 = tk.Label(self, text = '      ')
        self.l3.grid(row = 0, column = 2, sticky = W)

        # Среднегодовой объем дождевых вод
        self.wdrain_l1 = tk.Label(self, text = 'Среднегодовой объем ')
        self.wdrain_l2 = tk.Label(self, text = 'дождевых вод')
        self.wdrain_l1.grid(row = step + 4, column = 4, sticky = W)
        self.wdrain_l2.grid(row = step + 5, column = 4, sticky = W)
        self.wdrain_e = ttk.Entry(self, justify = CENTER, width = 12)
        self.wdrain_e.grid(row = step + 5, column = 5, sticky = E)
        self.wdrain_l3 = tk.Label(self, text = 'м3/год')
        self.wdrain_l3.grid(row = step + 5, column = 6, sticky = W)

        # Среднегодовой объем талых вод
        self.wtsnow_l1 = tk.Label(self, text = 'Среднегодовой объем ')
        self.wtsnow_l2 = tk.Label(self, text = 'талых вод')
        self.wtsnow_l1.grid(row = step + 7, column = 4, sticky = W)
        self.wtsnow_l2.grid(row = step + 8, column = 4, sticky = W)
        self.wtsnow_e = ttk.Entry(self, justify = CENTER, width = 12)
        self.wtsnow_e.grid(row = step + 8, column = 5, sticky = E)
        self.wtsnow_l3 = tk.Label(self, text = 'м3/год')
        self.wtsnow_l3.grid(row = step + 8, column = 6, sticky = W)

        # Среднегодовой объем поливмоечных вод
        self.wmwash_l1 = tk.Label(self, text = 'Среднегодовой объем ')
        self.wmwash_l2 = tk.Label(self, text = 'поливмоечных вод')
        self.wmwash_l1.grid(row = step + 10, column = 4, sticky = W)
        self.wmwash_l2.grid(row = step + 11, column = 4, sticky = W)
        self.wmwash_e = ttk.Entry(self, justify = CENTER, width = 12)
        self.wmwash_e.grid(row = step + 11, column = 5, sticky = E)
        self.wmwash_l3 = tk.Label(self, text = 'м3/год')
        self.wmwash_l3.grid(row = step + 11, column = 6, sticky = W)

        # Create the function for select all text in the entries:
        self.f_sq_e.bind('<Button-1>', self.selectall)
        self.f_msq_e.bind('<Button-1>', self.selectall)
        self.f_sn_e.bind('<Button-1>', self.selectall)
        self.h_d_e.bind('<Button-1>', self.selectall)
        self.h_t_e.bind('<Button-1>', self.selectall)
        self.u_t_e.bind('<Button-1>', self.selectall)
        self.m_e.bind('<Button-1>', self.selectall)
        self.k_e.bind('<Button-1>', self.selectall)
        self.u_m_e.bind('<Button-1>', self.selectall)
        self.rain_e.bind('<Button-1>', self.selectall)
        self.wtsnow_e.bind('<Button-1>', self.selectall)
        self.wdrain_e.bind('<Button-1>', self.selectall)
        self.wmwash_e.bind('<Button-1>', self.selectall)

    # доп функция для выбора текста в ячейке
    def selectall(self, event):
        self.after(10, self.select_all, event.widget)

    # и оно для того же
    @staticmethod
    def select_all(widget):
        widget.selection_range(0, END)

    # Считем дождь и выводим в ячейку
    def wd_rain(self):
        f_sq = float(self.f_sq_e.get())
        u_d = float(Ud.u_d_rain)
        h_d = float(self.h_d_e.get())
        wdrain = 10 * h_d * u_d * f_sq
        self.wdrain_e.delete(0, END)
        self.wdrain_e.insert(0, str(round(wdrain, 2)))
        self.u_d_button.config(text = "" + str(round(u_d, 2)), width = 10)
        return wdrain

    # Считаем снег и выводим в ячейку
    def wt_snow(self):
        f_sq = float(self.f_sq_e.get())
        f_sn = float(self.f_sn_e.get())
        h_t = float(self.h_t_e.get())
        u_t = float(self.u_t_e.get())
        k_y = 1 - f_sn / f_sq
        wtsnow = 10 * h_t * k_y * u_t * f_sq
        self.wtsnow_e.delete(0, END)
        self.wtsnow_e.insert(0, str(round(wtsnow, 2)))
        return wtsnow

    # Считаем мойку и выводим в ячейку
    def wm_wash(self):
        f_msq = float(self.f_msq_e.get())
        m = float(self.m_e.get())
        k = float(self.k_e.get())
        u_m = float(self.u_m_e.get())
        wmwash = 10 * m * k * u_m * f_msq
        self.wmwash_e.delete(0, END)
        self.wmwash_e.insert(0, str(round(wmwash, 2)))
        return wmwash

    # суммируем это все и выводим в ячейку
    def solve_rain(self):
        allrain = self.wd_rain() + self.wt_snow() + self.wm_wash()
        self.rain_e.delete(0, END)
        self.rain_e.insert(0, str(round(allrain, 2)))
        return

    # Создаем новое окно для расчета коэффициента
    @staticmethod
    def on_show_ud():
        Ud()


# Класс для нового окна для расчета коэффициента стока


class Ud(tk.Toplevel):

    # переменная для передачи во вне
    u_d_rain = 0.95

    def __init__(self):
        super().__init__()
        # Титул  окна
        self.title("Расчет общего коэффициента стока дождевых вод")
        # поясняющий текст для второй колонки
        slogan2 = tk.Label(self, text = "Значение")
        slogan2.grid(row = 0, column = 1, sticky = W)
        # Поясняющий текст для третей колоки
        slogan3 = tk.Label(self, text = "Площадь, га")
        slogan3.grid(row = 0, column = 2, sticky = W)
        # Поясняющий текст для четвертой колоки
        slogan4 = tk.Label(self, text = "Коэфициент")
        slogan4.grid(row = 0, column = 3, sticky = W)
        # Список для хранения названий ячеек
        ulist = ['Кровли и асфальтобетонные покрытия — (0,6 - 0,7):',
                 'Булыжные или щебёночные мостовые — (0,4 - 0,5):',
                 'Кварталы без дорожных покрытий, скверы, бульвары — (0,2 - 0,3):',
                 'Газоны — (0,1):',
                 'Кварталы с современной застройкой — (0,4 - 0,5):',
                 'Средние города — (0,4 - 0,5):',
                 'Небольшие города и поселки — (0,3 - 0,4):',
                 'Для промышленных предприятий и производств:',
                 '—    для водонепроницаемых покрытий — (0,6 - 0,8):',
                 '—    для грунтовых поверхностей — (0,2):',
                 '—    для газонов — (0,1):'
                 ]
        # Список для хранения значений ячеек по умолчанию
        mlist = [0.6, 0.4, 0.2, 0.1, 0.4, 0.4, 0.3, 0.6, 0.2, 0.1]

        # автоматически создаем кучу текса
        ft = len(ulist)

        for i in range(ft):
            self.ud_wi = tk.Label(self, text = '' + ulist[i])
            self.ud_wi.grid(row = i + 1, column = 0, sticky = W)
        # лист для хранения названий полей ввода
        self.tlist = ['rt1', 'rt2', 'rt3', 'rt4', 'rt5', 'rt6', 'rt7', 'rt8', 'rt9', 'rt10']
        # лист для хранения полей ввода первой колонки
        self.entry = {}
        # лист для хранения полей вовда второй колонки
        self.entry1 = {}
        # лист для хранения полей вовда третей колонки
        self.entry2 = {}
        # погнали цикл создания сразу двух колонок полей ввода
        ik = 0
        im = 0
        for name in self.tlist:
            # убираем лишние поля ввода
            if ik == 7:
                ik += 1
            # первая колонка с коэффициентами
            self.e = Entry(self, justify = CENTER, width = 10)
            self.e.grid(row = ik + 1, column = 1, sticky = W)
            self.e.insert(END, mlist[im])
            self.e.bind('<Button-1>', self.selectall)
            self.entry[name] = self.e
            # вторая колонка с площадями
            self.e1 = Entry(self, justify = CENTER, width = 11)
            self.e1.grid(row = ik + 1, column = 2, sticky = W)
            self.e1.insert(END, 0)
            self.e1.bind('<Button-1>', self.selectall)
            self.entry1[name] = self.e1

            # третья колонка с площадями х коэф.
            self.e2 = Entry(self, justify = CENTER, width = 11)
            self.e2.grid(row = ik + 1, column = 3, sticky = W)
            self.e2.insert(END, 0)
            self.e2.bind('<Button-1>', self.selectall)
            self.entry2[name] = self.e2

            ik += 1
            im += 1

        # кнопка для активации расчета коэффициента
        self.ud_button = tk.Button(self,
                                   text = "ВЫПОЛНИТЬ РАСЧЕТ",
                                   fg = "blue",
                                   command = self.check_all_entries
                                   )
        self.ud_button.grid(row = ik + 1, column = 2, sticky = W)

        # Поясняющий текст для вывода расчетного значения
        slogan5 = tk.Label(self, text = "Общий коэффициент стока дождевых вод:")
        slogan5.grid(row = ik + 1, column = 0, sticky = E)

        # кнопка для активации расчета коэффициента
        self.u_re = Entry(self, justify = CENTER, width = 10)
        self.u_re.grid(row = ik + 1, column = 1, sticky = W)
        self.u_re.insert(END, str(round(Ud.u_d_rain, 2)))
        self.u_re.bind('<Button-1>', self.selectall)

    # выгружаем значения из полей ввода и сразу делаем расчет

    def check_all_entries(self):
        f_all = 0.0
        u_all = 0.0
        for name1 in self.entry1:
            f_all += float(self.entry1[name1].get())
        for name2 in self.entry and self.entry1 and self.entry2:
            u_all += (float(self.entry[name2].get()) * float(self.entry1[name2].get()))
            tranzit = float(self.entry[name2].get()) * float(self.entry1[name2].get())
            self.entry2[name2].delete(0, END)
            self.entry2[name2].insert(0, str(round(tranzit, 2)))
        u_middle = u_all / f_all
        Ud.u_d_rain = u_middle
        self.u_re.delete(0, END)
        self.u_re.insert(0, str(round(u_middle, 2)))
        return u_middle

    # опять выделение
    def selectall(self, event):
        self.after(10, self.select_all, event.widget)

    # и снова оно
    @staticmethod
    def select_all(widget):
        widget.selection_range(0, END)


# Create the Tab N2:


class Tab2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the label for an initial data for calculation:
        username = StringVar()
        self.name = ttk.Entry(self, textvariable = username)
        self.name.grid(row = 1,
                       column = 1,
                       sticky = W)

        # Create the Separator:
        self.sep = ttk.Separator(self, orient = HORIZONTAL)
        self.sep.grid(row = 0)

        # Create the Combobox:
        countryvar = 1
        self.country = ttk.Combobox(self, textvariable = countryvar)
        self.country.bind('<<ComboboxSelected>>')
        self.country['values'] = ('USA', 'Canada', 'Australia')
        self.country.grid(row = 2, column = 2, sticky = W)
