```python
import tkinter as tk
from tkinter import messagebox

def clear():
    t1.delete(0, tk.END)
    t2.delete(0, tk.END)

def login():
    username = t1.get()
    password = t2.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror(
            "Login",
            "Invalid Username or Password"
        )

# Main Program
root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")

# Row 1 - Heading
f1 = tk.Frame(root)
f1.pack(anchor="w", pady=10)

label_title = tk.Label(
    f1,
    text="Login Form",
    font=("Arial", 16, "bold")
)
label_title.pack(pady=10)

# Row 2 - Username
f2 = tk.Frame(root)
f2.pack(anchor="w", pady=10)

l1 = tk.Label(f2, text="Username")
l1.pack(side="left", padx=5)

t1 = tk.Entry(f2)
t1.pack(side="left")

# Row 3 - Password
f3 = tk.Frame(root)
f3.pack(anchor="w", pady=10)

l2 = tk.Label(f3, text="Password")
l2.pack(side="left", padx=5)

t2 = tk.Entry(f3, show="*")
t2.pack(side="left")

# Row 4 - Buttons
f4 = tk.Frame(root)
f4.pack(pady=15)

b1 = tk.Button(f4, text="Login", command=login)
b1.pack(side="left", padx=10)

b2 = tk.Button(f4, text="Clear", command=clear)
b2.pack(side="left", padx=10)

root.mainloop()
```
