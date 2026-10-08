import tkinter as tk

window = tk.Tk()
window.title("Demo")
window.geometry("400x200")

# lbl = tk.Label(window, text = "Van Minh Khoi", font = ("Arial", 20))
# lbl.grid(column = 0, row = 0, padx = 10, pady = 10)
# lbl = tk.Label(window, text = "Lap trinh vien Python", font = ("Arial", 14))
# lbl.grid(column = 0, row = 1, padx = 10, pady = 10)
# lbl = tk.Label(window, text = "khoivan2605@gmail.com", font = ("Arial", 12))
# lbl.grid(column = 0, row = 2, padx = 10, pady = 10)

# count = 0
# def clicked():
#     global count
#     count += 1
#     lbl.configure(text = "Số lần đã bấm: " + str(count))

# lbl = tk.Label(window, text = "Số lần đã bấm : 0", font = ("Arial", 20))
# lbl.grid(column=0, row=0)
# btn = tk.Button(window, text = "Bấm vào đây", command = clicked, font = ("Arial", 20))
# btn.grid(column=0, row=1)

output = tk.StringVar()

def clicked():
    output.set(f"Xin chao {in_ent.get()}")

in_ent = tk.Entry(window, width = 100)
in_ent.grid(column = 0, row = 0)
in_ent.focus()

out_ent = tk.Entry(window, width=100, textvariable=output, state = "readonly")
out_ent.grid(column=0, row=3, padx=10, pady=10)

btn = tk.Button(window, text="Chao", command = clicked)
btn.grid(column=0, row=1, padx=10, pady=10)

window.mainloop()