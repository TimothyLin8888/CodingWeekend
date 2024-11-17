import tkinter as tk
import math

def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Hello World")

def button_square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_power():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + "**")

root = tk.Tk()
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

root.title("Calculator")
root.geometry("900x700")

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("C", 5, 0), ("0", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("√", 1, 0), ("^", 1, 1)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=button_equal)
    elif text == "C":
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=button_clear)
    elif text == "√":
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=button_square_root)
    elif text == "^":
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=button_power)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14),
                        command=lambda value=text: button_click(value))
    btn.grid(row=row, column=col, padx=5, pady=5)

normal_button = tk.Button(root, text="Normal Distribution", padx=120, pady=10, font=("Arial", 12),command=button_equal)
normal_button.grid(row=6, column=0, columnspan=4, pady=10)
root.mainloop()