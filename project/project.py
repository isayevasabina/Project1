from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Упс!","Что-то пошло не так!Файл нельзя сохранить!")


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.incert('1.0', data)


root = Tk()  #создаем окно
root.title("Заметки")
root.geometry("800x800")

text = Text(root, width=400, height=400)
text.pack()

menu_bar = Menu(root)  #создание меню бара
file_menu = Menu(menu_bar)

file_menu.add_command(label="Создать новый файл", command=new_file)
file_menu.add_command(label="Открыть файл", command=open_file)
file_menu.add_command(label="Сохранить файл как", command=save_as)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
