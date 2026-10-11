import tkinter as tk
from tkinter import messagebox

def submit():
    result = "Roll No: " + t1.get() + \
             "\nName: " + t2.get() + \
             "\nMark: " + t3.get()

    messagebox.showinfo("Student Details", result)

def clear():
    t1.delete(0, tk.END)
    t2.delete(0, tk.END)
    t3.delete(0, tk.END)

# Main Program
root = tk.Tk()
root.title("Student Form")
root.geometry("400x300")

# Row 1 - Heading
f1 = tk.Frame(root)
f1.pack(anchor="w", pady=10)

label_title = tk.Label(
    f1,
    text="Student Registration Form",
    font=("Arial", 16)
)
label_title.pack(pady=10)

# Row 2 - Roll No
f2 = tk.Frame(root)
f2.pack(anchor="w", pady=10)

l1 = tk.Label(f2, text="Roll No")
l1.pack(side="left", pady=10)

t1 = tk.Entry(f2)
t1.pack(side="left")

# Row 3 - Name
f3 = tk.Frame(root)
f3.pack(anchor="w", pady=10)

l2 = tk.Label(f3, text="Name")
l2.pack(side="left", pady=10)

t2 = tk.Entry(f3)
t2.pack(side="left")

# Row 4 - Mark
f4 = tk.Frame(root)
f4.pack(anchor="w", pady=10)

l3 = tk.Label(f4, text="Mark")
l3.pack(side="left", padx=5)

t3 = tk.Entry(f4)
t3.pack(side="left")

# Row 5 - Buttons
f5 = tk.Frame(root)
f5.pack(pady=15)

b1 = tk.Button(f5, text="Submit", command=submit)
b1.pack(side="left", padx=10)

b2 = tk.Button(f5, text="Clear", command=clear)
b2.pack(side="left", padx=10)

root.mainloop()

