import tkinter as tk


window = tk.Tk()
window.minsize(400, 400)

def kontrol():
    if not weight_entry.get() or not height_entry.get():
        outcome.config(text="Lütfen Bilgilerinizi eksiksiz giriniz.")
    else:
        calculate()
def calculate():
    w = int(weight_entry.get())
    h = int(height_entry.get())
    bmı = 10000 * (w / h ** 2)
    last_bmı = round(bmı, 2)
    if last_bmı > 25:
        outcome.config(text=f"Vücut kitle endeksiniz {last_bmı}. Kilonuz normal seviyenin üstünde")
    elif last_bmı < 25 and last_bmı > 20:
        outcome.config(text=f"Vücut kitle endeksiniz {last_bmı}. Kilonuz normal seviyesinde")
    elif last_bmı < 20:
        outcome.config(text=f"Vücut kitle endeksiniz {last_bmı}. Kilonuz normal seviyenin altında")


weight_label = tk.Label(text="Kilonuzu girin")
weight_label.pack()

weight_entry = tk.Entry()
weight_entry.pack()

height_label = tk.Label(text="Boyunuzu Girin")
height_label.pack()

height_entry = tk.Entry()
height_entry.pack()

calculate_button = tk.Button(text="Calculate", command=kontrol)
calculate_button.pack()

outcome = tk.Label(text="")
outcome.pack()


tk.mainloop()