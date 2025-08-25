import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Tạo DB và bảng nếu chưa có ---
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')
conn.commit()

# --- Hàm xử lý ---
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, title FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]}. {row[1]}")

def add_task():
    task = entry.get().strip()
    if task:
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Cảnh báo", "Nội dung không được để trống!")

def delete_task():
    selection = listbox.curselection()
    if selection:
        task_text = listbox.get(selection[0])
        task_id = task_text.split(".")[0]
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Cảnh báo", "Hãy chọn một công việc để xoá!")

# --- Giao diện Tkinter ---
root = tk.Tk()
root.title("To-Do List (SQLite) - Nhẹ <1MB")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=5)

btn_add = tk.Button(frame, text="Thêm", command=add_task)
btn_add.grid(row=0, column=1)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

btn_delete = tk.Button(root, text="Xoá", command=delete_task)
btn_delete.pack(pady=5)

# Load dữ liệu ban đầu
load_tasks()

root.mainloop()

# Đóng kết nối khi tắt app
conn.close()
