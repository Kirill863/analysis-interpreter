import tkinter as tk
from tkinter import scrolledtext

def process_text():
    """Функция для обработки введенного текста"""
    user_input = text_area.get("1.0", tk.END)  # Получаем весь текст из текстового поля
    user_input = user_input.strip()  # Удаляем лишние пробелы и переносы строк
    
    if user_input:
        result_label.config(text=f"Вы ввели:\n{user_input}")
        # Здесь можно добавить логику для анализа текста
    else:
        result_label.config(text="Текст не введен!")



# Создание основного окна
root = tk.Tk()
root.title("Ввод и обработка текста")
root.geometry("400x300")

# Создание метки с инструкцией
instruction_label = tk.Label(root, text="Введите текст ниже:")
instruction_label.pack(pady=10)

# Создание текстового поля для ввода (scrolledtext для многострочного ввода)
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=5)

# Кнопка для отправки текста на обработку
submit_button = tk.Button(root, text="Обработать текст", command=process_text)
submit_button.pack(pady=10)

# Метка для вывода результата
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()