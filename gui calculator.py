```python
import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = int(t1.get()) + int(t2.get())
        t3.delete(0, tk.END)
        t3.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def sub():
    try:
        result = int(t1.get()) - int(t2.get())
        t3.delete(0, tk.END)
        t3.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def mul():
    try:
        result = int(t1.get()) * int(t2.get())
        t3.delete(0, tk.END)
        t3.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def div():
    try:
        result = int(t1.get()) / int(t2.get())
        t3.delete(0, tk.END)
        t3.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Main Program
root = tk.Tk()
root.title("Calculator")
root.geometry("400x250")

# Row 1 - Number 1
f1 = tk.Frame(root)
f1.pack(anchor="w", pady=10)

l1 = tk.Label(f1, text="Number 1")
l1.pack(side="left", padx=5)

t1 = tk.Entry(f1)
t1.pack(side="left")

# Row 2 - Number 2
f2 = tk.Frame(root)
f2.pack(anchor="w", pady=10)

l2 = tk.Label(f2, text="Number 2")
l2.pack(side="left", padx=5)

t2 = tk.Entry(f2)
t2.pack(side="left")

# Row 3 - Result
f3 = tk.Frame(root)
f3.pack(anchor="w", pady=10)

l3 = tk.Label(f3, text="Result")
l3.pack(side="left", padx=5)

t3 = tk.Entry(f3)
t3.pack(side="left")

# Row 4 - Buttons
f4 = tk.Frame(root)
f4.pack(pady=15)

b1 = tk.Button(f4, text="Addition", command=add)
b1.pack(side="left", padx=3)

b2 = tk.Button(f4, text="Subtraction", command=sub)
b2.pack(side="left", padx=3)

b3 = tk.Button(f4, text="Multiplication", command=mul)
b3.pack(side="left", padx=3)

b4 = tk.Button(f4, text="Division", command=div)
b4.pack(side="left", padx=3)

root.mainloop()
```
