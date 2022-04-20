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

   
```python
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

root = Tk()  #создаем окно
root.title("Заметки")
root.geometry("800x800")

root.mainloop()
```


## *Мои данные*
<a href = "i.s.r_01@mail.ru"> Почта</a>