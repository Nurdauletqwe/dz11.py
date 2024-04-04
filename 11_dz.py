'''1'''

# import json
# import requests
# import os

# # Получение данных с сайта
# url = "https://jsonplaceholder.typicode.com/todos/"
# response = requests.get(url)
# data = response.json()

# # Создание JSON файла и заполнение его данными
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# # Чтение JSON файла в массив python-словарей
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)

# # Запись каждого словаря в отдельный JSON файл
# if not os.path.exists('individual_files'):
#     os.makedirs('individual_files')

# for idx, item in enumerate(data, start=1):
#     filename = f'individual_files/{idx}.json'
#     with open(filename, 'w') as json_file:
#         json.dump(item, json_file, indent=4)

# print("Файлы были успешно созданы.")


'''2'''
# from docx import Document
# from docx.shared import Pt

# doc = Document()
# doc.add_paragraph("Hello Python")
# doc.save("hello_python.docx")

# doc = Document("hello_python.docx")
# bold_text = [p.text for p in doc.paragraphs if any(run.bold for run in p.runs)]
# bold_text = ' '.join(bold_text)
# print("Жирный текст из файла:", bold_text)

# new_doc = Document()
# paragraph = new_doc.add_paragraph("This is a new paragraph.")
# run = paragraph.runs[0]
# run.bold = True
# run.font.name = 'Arial'
# run.font.size = Pt(14)

# new_doc.save("new_file.docx")
# print("Новый файл успешно создан.")
