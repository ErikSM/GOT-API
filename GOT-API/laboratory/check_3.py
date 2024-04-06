import tkinter as tk


window = tk.Tk()
window.geometry('400x200')
window.title("----")


def do_check(*args):
    approved = False

    print(check_string.get())

    if len(entry.get()) < 3:
        approved = True

    if check_string.get() != 'Yes':
        approved = True

    if not approved:
        button.config(state='normal', bg='green')
    else:
        button.config(state='disabled', bg='white')


label = tk.Label(window, text='Name', font=20)
label.grid(row=0, column=0, padx=10, pady=10)

string_entry = tk.StringVar()
entry = tk.Entry(window, bg='beige', font=20, textvariable=string_entry)
entry.grid(row=0, column=1)
string_entry.trace('w', do_check)

check_string = tk.StringVar(window)
check_string.set('')
check_button = tk.Checkbutton(window, text='I agree', variable=check_string,  onvalue='Yes', offvalue='hhl',
                              command=do_check, font=24)
check_button.grid(row=1, column=1, sticky='w')

button = tk.Button(window, text='Submit', bg='white', font=20, state='disabled')
button.grid(row=2, column=1, padx=10, pady=5)

window.mainloop()
