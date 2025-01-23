import tkinter as tk
from tkinter import filedialog

# 创建主窗口
root = tk.Tk()
root.title("读取文本文件工具")

# 设置窗口大小
root.geometry("600x400")

# 显示文本的框
text_box = tk.Text(root, wrap=tk.WORD, height=15, width=70)
text_box.pack(padx=10, pady=10)

# 选择文件的函数
def open_file():
    file_path = filedialog.askopenfilename(
        title="选择文本文件", filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                text_box.delete(1.0, tk.END)  # 清空文本框
                text_box.insert(tk.END, file_content)  # 显示文件内容
        except Exception as e:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, f"文件读取错误: {str(e)}")

# 添加按钮来打开文件
open_button = tk.Button(root, text="打开文本文件", command=open_file)
open_button.pack(pady=10)

# 启动主事件循环
root.mainloop()
