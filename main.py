import tkinter as tk
from tkinter import messagebox
import pyodbc

def add_to_database(student_id, full_name, class_name, school_name ):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=ADMIN-PC\SQLEXPRESS;'
                              'DATABASE=ManagementClass;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Student (student_id, full_name, class_name, school_name) VALUES (?, ?, ?, ?)',
                        (student_id, full_name, class_name, school_name))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm dữ liệu: {str(e)}")

def validate_entry():
    student_id = entry1.get()
    full_name = entry2.get().upper()
    class_name = entry3.get()
    school_name = entry4.get().upper()

    if student_id and len(student_id) == 8 and student_id.isdigit():
        messagebox.showinfo("Thông báo", "Nhập mã số thành công!")
    else:
        messagebox.showerror("Lỗi", "Mã số phải có 8 chữ số!")

    if full_name.isalpha():
        messagebox.showinfo("Thông báo", f"Họ tên: {full_name}")
    else:
        messagebox.showerror("Lỗi", "Họ tên phải là chuỗi chữ!")

    if class_name.isalnum():
        messagebox.showinfo("Thông báo", f"Lớp: {class_name}")
    else:
        messagebox.showerror("Lỗi", "Lớp phải bao gồm chữ hoa và số!")

    if school_name.isalpha():
        messagebox.showinfo("Thông báo", f"Trường: {school_name}")
    else:
        messagebox.showerror("Lỗi", "Trường phải viết hoa!")

window = tk.Tk()
window.geometry("600x400")
window.title("Form Thông Tin Sinh Viên")
def validate_and_add():
    validate_entry()
    add_to_database(entry1.get(), entry2.get().upper(), entry3.get(), entry4.get().upper())

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

center_window(window, 600, 400)

hello_label = tk.Label(
    text="Chào mừng bạn đến với Form Thông Tin Sinh Viên",
    font=("Arial", 16),
    width=55,
    height=3,
    background="red",
    foreground="white"
)
hello_label.pack()

# Ô input 1
input_label1 = tk.Label(text="Mã Sinh Viên:", font=("Helvetica", 11))
input_label1.place(x=50, y=100)
entry1 = tk.Entry(font=("Helvetica", 11), width=30)
entry1.place(x=160, y=95, height=30)

# Ô input 2
input_label2 = tk.Label(text="Họ Tên: ", font=("Helvetica", 11))
input_label2.place(x=50, y=150)
entry2 = tk.Entry(font=("Helvetica", 11), width=30)
entry2.place(x=160, y=150, height=30)

# Ô input 3
input_label3 = tk.Label(text="Lớp: ", font=("Helvetica", 11))
input_label3.place(x=50, y=200)
entry3 = tk.Entry(font=("Helvetica", 11), width=30)
entry3.place(x=160, y=200, height=30)

# Ô input 4
input_label4 = tk.Label(text="Trường: ", font=("Helvetica", 11))
input_label4.place(x=50, y=250)
entry4 = tk.Entry(font=("Helvetica", 11), width=30)
entry4.place(x=160, y=250, height=30)

# Button
validate_button = tk.Button(text="THÊM VÀO", 
                            command=validate_and_add, 
                            width=15,
                            height=2,
                            background="green",
                            bd=0)
validate_button.place(x=300, y=300)

window.mainloop()
