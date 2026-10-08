import tkinter as tk

window = tk.Tk()
window.title("Label Demo")

lbl = tk.Label(window, text = "Hello")
lbl.grid(column = 0, row = 0)

window.mainloop()