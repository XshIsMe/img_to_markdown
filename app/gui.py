import time
import tkinter
from tkinter import filedialog
import img_to_md as tools


class App:

    def __init__(self):
        self.folder_path = None
        self.height = 200
        self.width = 600
        self.tk = tkinter.Tk()
        self.init_folder_path_choose_button()
        self.tk.geometry('{width}x{height}'.format(
            height=self.height,
            width=self.width
        ))
        self.tk.mainloop()

    def get_folder_path(self):
        self.folder_path = filedialog.askdirectory()
        self.folder_path = self.folder_path.replace('/', '\\') + '\\'
        if None != self.folder_path and '' != self.folder_path:
            self.init_img_to_md_button()

    def img_to_md(self):
        if not hasattr(self, 'list_box'):
            self.text_index = 0
            self.list_box = tkinter.Listbox(self.tk, width=self.width)
        self.text_index += 1
        self.list_box.insert(0, '【{index}】{time}'.format(
            index=str(self.text_index),
            time=time.asctime(time.localtime(time.time()))
        ))
        try:
            result = tools.img_to_md(self.folder_path)
        except:
            result = ['剪贴板中没有截图', '请重试']
        self.list_box.insert(1, '')
        self.list_box.insert(2, result[0])
        self.list_box.insert(3, result[1])
        self.list_box.insert(4, '')
        self.list_box.pack()

    def init_folder_path_choose_button(self):
        self.folder_path_choose_button = tkinter.Button(
            text='选择图片保存目录',
            height=self.height,
            width=self.width,
            command=self.get_folder_path
        )
        self.folder_path_choose_button.pack()

    def init_img_to_md_button(self):
        self.folder_path_choose_button.pack_forget()
        self.img_to_md_button = tkinter.Button(
            text='将剪贴板中的图片转换为markdown',
            width=self.width,
            command=self.img_to_md
        )
        self.img_to_md_button.pack()


app = App()
