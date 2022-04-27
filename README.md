# **Приложение блокнот на ЯП *Python***
___
> По сей день большую популярность имеет метод планирования. Люди пользуются блокнотами, заметками, ежедневником не зависимо от возраста.  
___
## ***Что из себя представляет приложение***?
* _Создание нового файла для записи_
* _Сохранение файлов на устройстве_
* _Открытие сохраненных записей_

![python](https://kbfblog.com/wp-content/uploads/2021/10/article-03440000002019214749270.jpg)


### **Используемые библиотеки**:
`Tkinter (от англ. Tk interface) — кросс-платформенная событийно-ориентированная графическая библиотека на основе средств Tk (широко распространённая в мире GNU/Linux и других UNIX‐подобных систем, портирована также и на Microsoft Windows), написанная Стином Лумхольтом (Steen Lumholt) и Гвидо ван Россумом. Входит в стандартную библиотеку Python.`



 + [Подробнее](https://ru.wikipedia.org/wiki/Tkinter)
   ____

   **Алгоритм:**
   1. Импорт библиотек
   2. Создать окно
   3. Создать функции и меню:
      1. Функция создания нового файла
      2. Функция сохранения файла
      3. Функция открытия файла
  ____
```python
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

root = Tk()  #создаем окно
root.title("Заметки")
root.geometry("800x800")

root.mainloop()
```



```PYTHON
menu_bar = Menu(root)  #создание MENUBAR
file_menu = Menu(menu_bar)

file_menu.add_command(label="Создать новый файл", command=new_file)
file_menu.add_command(label="Открыть файл", command=open_file)
file_menu.add_command(label="Сохранить файл как", command=save_as)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)
```
____
# **Что такое menubar?**
Полоска меню, линейка меню
горизонтальная полоска в верхней части окна, содержащая элементы выбора (пункты меню), доступные в активном приложении

[Menu bar](https://computers_en_ru.academic.ru/9297/menu_bar)
_____

## *Мои данные*
<a href = "i.s.r_01@mail.ru"> Почта</a>