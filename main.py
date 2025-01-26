from lab5_1 import Window1
from lab5_2 import Window2
import tkinter

task_list = {
    "1": (Window1, "Zubov_Yevgeniy Lab5.1", "1024x768"),
    "2": (Window2, "Zubov_Yevgeniy Lab5.2", "1024x768")

}

choice = input("Оберіть завдання 1-2 (0-EXIT): ")
while choice != "0":
    # якщо даний ключ є у словнику
    if choice in task_list.keys():
            # Створення відповідного вікна
        application = tkinter.Tk()
        window_class, window_name, window_size = task_list.get(choice)
        window = window_class(application)
        application.geometry(window_size)
        application.title(window_name)
        application.mainloop()
    else:
        print("Неправильно обрано завдання!")
    choice = input("Оберіть завдання знову! (0-EXIT): ")
