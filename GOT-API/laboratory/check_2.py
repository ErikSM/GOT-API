import tkinter as tk


window = tk.Tk()
window.geometry("600x250")
window.title('ErikSM - Testing')

string_start = 'data'

font_checkbutton = ('times', 30, 'normal')
font_label = ('times', 22, 'normal')

music_types = {'Rock': False, 'Opera': False, 'Dance': False, 'Hiphop': False}

column = 0
for i in music_types:
    music_types[i] = tk.BooleanVar(value=music_types[i])

    checkbutton = tk.Checkbutton(window, text=i, font=font_checkbutton, command=lambda: do_test())
    checkbutton.config(variable=music_types[i], onvalue=True, offvalue=False)
    checkbutton.grid(row=0, column=column, padx=5, pady=20)

    column += 1

string_var = tk.StringVar(value=string_start)
label = tk.Label(window, textvariable=string_var, bg='beige', font=font_label)
label.grid(row=1, column=0, columnspan=column, pady=20, padx=5)


def do_test():
    temporary_list = list()

    for j in music_types:
        string = j + ':' + str(music_types[j].get())
        temporary_list.append(string)

    temporary_list = ", ".join(map(str, temporary_list))

    string_var.set(temporary_list)


window.mainloop()

