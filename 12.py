import tkinter as tk
from tkinter import ttk

pizzas = ["Margherita", "Pepperoni"]
pizza_prices = [80000, 95000, 100000, 120000]

extras = ["Pho mai", "Nam", "Ot", "O Liu"]
extra_prices = [10000, 8000, 5000, 7000]

root = tk.Tk()
root.title("Pizza")
root.geometry("400x350")

pizza_var = tk.IntVar(value=0)
extra_vars = []

tk.Label(root, text="Chon loai Pizza:").pack(anchor="w", padx = 10, pady = 5)

for i in range(len(pizzas)):
    tk.Radiobutton(
        root,
        text=pizzas[i],
        variable=pizza_var,
        value=i,
        command=lambda: tinh_tien()
    ).pack(anchor="w", padx=20)

tk.Label(root, text="Them Topping:").pack(anchor="w", padx=10, pady = 5)

for i in range(len(extras)):
    var = tk.BooleanVar(value = False)
    extra_vars.append(var)

    tk.Checkbutton(
        root,
        text=extras[i],
        variable=var,
        command=lambda: tinh_tien()
    ).pack(anchor="w", padx=20)

kq = tk.Label(root, text="", font=("Arial", 11))
kq.pack(anchor="w", padx=10, pady=10)

def tinh_tien():
    vi_tri = pizza_var.get()

    tong_tien = pizza_prices[vi_tri]
    ten_da_chon = [pizzas[vi_tri]]

    for i in range(len(extras)):
        if extra_vars[i].get():
            tong_tien += extra_prices[i]
            ten_da_chon.append(extras[i])
    kq.config(
        text="+".join(ten_da_chon)
        + ": {:,} d".format(tong_tien)
    )

tinh_tien()

root.mainloop()