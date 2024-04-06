from tkinter import *
from main import characters, continents

colors = {'black': "black", 'grey': "grey", 'white': "white", 'green': "#4C796A"}


class App:

    def __init__(self):

        self.__all_characters = dict()
        self.__all_continents = dict()

        self.__continent_values = False
        self.__characters_values = False

        self.window = Tk()
        self.window.title('GOT-API')
        self.window.geometry("800x600+400+100")
        self.window.resizable(False, False)
        self.window.config(bg=colors['green'], bd=15)

        f_head = Frame(self.window, bg=colors['green'], bd=8)

        advanced_list = ["All", "Character", "Continent"]

        sf_search = Frame(f_head, bg=colors['white'], bd=1)
        self.string_advanced = StringVar(self.window)
        self.string_advanced.set('Advanced Search')

        self.advanced_options = OptionMenu(sf_search, self.string_advanced, *advanced_list)
        self.advanced_options.config(bg=colors['grey'], state=NORMAL, width=20, bd=3)
        self.advanced_options.pack(side=LEFT)

        self.entry_search = Entry(sf_search, bg=colors['white'], bd=8, width=30)
        self.entry_search.pack(side=LEFT)

        self.button_search = Button(sf_search, text="search", bg=colors['grey'], bd=3, command=self.search)
        self.button_search.pack(side=LEFT)
        sf_search.pack()

        f_head.pack(side=TOP)

        f_left = Frame(self.window, bg=colors['green'], bd=8)

        self.check_dict = {"all characters": None, "all continents": None}

        sf_listbox = Frame(f_left, bg=colors['white'], bd=2)
        checks_field = Frame(sf_listbox, bg=colors['white'], bd=2)
        for i in self.check_dict:
            self.check_dict[i] = BooleanVar(value=False)
            checkbutton = Checkbutton(checks_field, text=i, command=lambda: self.process())
            checkbutton.config(variable=self.check_dict[i], onvalue=True, offvalue=False, font=('Times', 9, 'bold'))
            checkbutton.pack(side=LEFT)
        checks_field.grid(row=0, column=1)

        self.listbox = Listbox(sf_listbox, bg=colors['white'], width=40, height=28, bd=5)
        y_list_left = Scrollbar(sf_listbox, orient=VERTICAL, command=self.listbox.yview, bd=5)
        y_list_left.grid(row=1, column=0, sticky=N + S)
        self.listbox.grid(row=1, column=1)
        self.listbox.config(yscrollcommand=y_list_left.set)
        sf_listbox.grid(row=1, column=1)

        buttons_field = Frame(sf_listbox)
        quant = 11
        cont = 0
        while cont <= quant:
            Button(buttons_field, state=DISABLED,
                   text='', bg=colors['white'],
                   bd=1, width=8, height=2).grid(column=0, row=cont)
            cont += 1

        self.but_select = Button(buttons_field, state=NORMAL, text='Select', bd=3, width=8, height=2)
        self.but_select.config(bg=colors['white'], command=self.do_select)
        self.but_select.grid(column=0, row=1)
        buttons_field.grid(row=1, column=2)

        f_left.pack(side=LEFT)

        f_right = Frame(self.window, bg=colors['green'], bd=8)

        sf_text = Frame(f_right, bg=colors['white'], bd=3)
        self.text = Text(sf_text, font=("Consolas", 10, "bold"), bg=colors['grey'], width=50, height=31, bd=15)
        y_text_right = Scrollbar(sf_text, orient=VERTICAL, command=self.text.yview, bd=5)
        y_text_right.grid(row=1, column=1, sticky=N + S)
        self.text.grid(row=1, column=0)
        self.text.config(yscrollcommand=y_text_right.set)
        sf_text.pack()

        f_right.pack(side=RIGHT)

        f_foot = Frame(self.window, bg=colors['black'])
        pass
        f_foot.pack(side=BOTTOM)

        self.window.mainloop()

    def search(self):

        advanced = self.string_advanced.get()
        searched = self.entry_search.get()

        print("Advanced:{}\nSearch:{}".format(advanced, searched))

    def _show_characters(self):

        for i in characters:
            string = f"{i['firstName']} {i['lastName']}"
            self.__all_characters[string] = i

            self.listbox.insert(END, string)

    def _show_continents(self):

        for i in continents:
            string = f"{i['name']}"
            self.__all_continents[string] = i

            self.listbox.insert(END, string)

    def eraser_list(self):
        self.listbox.delete(0, END)

    def do_checks(self):

        self.eraser_list()

        self.__characters_values = self.check_dict["all characters"].get()
        self.__continent_values = self.check_dict["all continents"].get()

    def process(self):

        self.do_checks()

        if self.__continent_values:
            self._show_continents()
        if self.__characters_values:
            self._show_characters()

    def do_select(self):

        self.text.delete(1.0, END)

        selected = self.listbox.get(ANCHOR)

        if selected in self.__all_continents:
            continent_selected = self.__all_continents[selected]
            self.text.insert(1.0, f"*Continent: (({selected}))\n\n\n\n")

            for i in continent_selected:
                title = i.title()
                data = continent_selected[i]

                string = f"{title.title()}: {data}\n\n"
                self.text.insert(END, string)

        elif selected in self.__all_characters:
            character_selected = self.__all_characters[selected]
            self.text.insert(1.0, f"*Character: (({selected})):\n\n\n\n")

            for i in character_selected:
                title = i.title()
                data = character_selected[i]

                string = f"{title.title()}: {data}\n\n"
                self.text.insert(END, string)


App()
