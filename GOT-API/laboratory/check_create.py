import tkinter as tk

my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window

c_v1 = tk.IntVar()
c1 = tk.Checkbutton(my_w, text='PHP', variable=c_v1,
                    onvalue=1, offvalue=0)
c1.grid(row=2, column=2)

my_w.mainloop()  # Keep the window open

