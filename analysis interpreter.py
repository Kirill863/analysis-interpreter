import tkinter as tk
from tkinter import scrolledtext
import re

def extract_indicators(text):
    """Функция для извлечения показателей из текста"""
    # Паттерн для поиска пар "название показателя – значение"
    pattern = r'([^\d–]+)\s*–\s*([\d.,]+)'
    
    matches = re.findall(pattern, text)
    indicators = {}
    
    for match in matches:
        name = match[0].strip()  # Название показателя
        value = match[1].replace(',', '.')  # Значение (заменяем запятую на точку)
        try:
            indicators[name] = float(value)  # Преобразуем значение в число
        except ValueError:
            indicators[name] = value  # Если не удается преобразовать, оставляем как строку
    
    return indicators

def process_text():
    """Функция для обработки введенного текста"""
    user_input = text_area.get("1.0", tk.END).strip()  # Получаем текст из текстового поля
    
    if user_input:
        indicators = extract_indicators(user_input)  # Извлекаем показатели
        
        # Формируем вывод
        result_text = "Извлеченные показатели:\n"
        for name, value in indicators.items():
            result_text += f"{name}: {value}\n"
        
        result_label.config(text=result_text)
    else:
        result_label.config(text="Текст не введен!")

# Создание основного окна
root = tk.Tk()
root.title("Анализ медицинских данных")
root.geometry("600x500")

# Создание метки с инструкцией
instruction_label = tk.Label(root, text="Введите данные анализов:")
instruction_label.pack(pady=10)

# Создание текстового поля для ввода
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text_area.pack(padx=10, pady=5)

# Кнопка для отправки текста на обработку
submit_button = tk.Button(root, text="Анализировать", command=process_text)
submit_button.pack(pady=10)

# Метка для вывода результата
result_label = tk.Label(root, text="", justify=tk.LEFT, anchor="w", wraplength=550)
result_label.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()