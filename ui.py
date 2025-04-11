import tkinter as tk
from tkinter import ttk

class UIManager:
    def __init__(self, task_manager):
        self.task_manager = task_manager

        self.window = tk.Tk()
        self.window.title('ToDo List')
        self.window.config(padx=20, pady=20)

        # 新規タスク追加欄
        self.add_frame = ttk.LabelFrame(self.window, text="新規タスク追加")
        self.add_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.add_frame, text="タイトル:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = ttk.Entry(self.add_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.add_frame, text="内容:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.content_entry = ttk.Entry(self.add_frame)
        self.content_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.add_button = ttk.Button(self.add_frame, text="追加", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        self.add_frame.columnconfigure(1, weight=1)

        # タスク一覧
        self.list_frame = ttk.LabelFrame(self.window, text="タスク一覧")
        self.list_frame.pack(padx=30, pady=30, fill="both", expand=True)

        self.task_canvas = tk.Canvas(self.list_frame)
        self.task_canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.task_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.task_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.task_canvas.bind('<Configure>', lambda e: self.task_canvas.configure(scrollregion = self.task_canvas.bbox("all")))

        self.task_list_inner_frame = ttk.Frame(self.task_canvas)
        self.task_canvas.create_window((0, 0), window=self.task_list_inner_frame, anchor="nw")

        self.update_task_list()
        self.window.mainloop()

    def add_task(self):
        title = self.title_entry.get()
        content = self.content_entry.get()
        if title and content:
            new_task_data = {"title": title, "content": content}
            self.task_manager.add_task(new_task_data)
            self.title_entry.delete(0, tk.END)
            self.content_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            tk.messagebox.showwarning("入力エラー", "タイトルと内容を入力してください。")

    def delete_task(self, task):
        self.task_manager.delete_task(task)
        self.update_task_list()

    def update_task_list(self):
        for widget in self.task_list_inner_frame.winfo_children():
            widget.destroy()

        # タスク表示、削除ボタン設置
        for i, task in enumerate(self.task_manager.tasks):
            task_frame = ttk.Frame(self.task_list_inner_frame, padding=5)
            task_frame.pack(fill="x", pady=2)

            title_label = ttk.Label(task_frame, text=f"タイトル: {task.title}", anchor="w")
            title_label.pack(fill="x")

            content_label = ttk.Label(task_frame, text=f"内容: {task.content}", anchor="w")
            content_label.pack(fill="x")

            delete_button = ttk.Button(task_frame, text="削除", command=lambda t=task: self.delete_task(t))
            delete_button.pack(side="right", padx=5)

            separator = ttk.Separator(self.task_list_inner_frame, orient="horizontal")
            separator.pack(fill="x", pady=2)

        # スクロール領域の更新
        self.task_list_inner_frame.update_idletasks()
        self.task_canvas.config(scrollregion=self.task_canvas.bbox("all"))
