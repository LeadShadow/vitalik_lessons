"""
У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати".
Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою, ви зможете настроїти цю
програму під себе, і вона виконуватиме індивідуальний сценарій, що відповідає вашим
потребам. Для цього наш додаток буде перевіряти розширення файлу (останні символи в
імені файлу, як правило, після крапки) і, залежно від розширення, приймати рішення,
до якої категорії віднести цей файл.

Скрипт приймає один аргумент при запуску — це ім'я папки, в якій він буде проводити
сортування. Допустимо, файл з програмою називається sort.py, тоді, щоб відсортувати
папку /user/Desktop/Мотлох, треба запустити скрипт командою
python sort.py /user/Desktop/Мотлох

Для того, щоб успішно впоратися з цим завданням, ви повинні винести логіку обробки
папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок
повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортувати всі файли по групах:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відеофайли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення.
Ви можете розширити та доповнити цей список, якщо хочете.

Після необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

Крім того, всі файли треба перейменувати, видаливши із назви всі символи, що
призводять до проблем. Для цього треба застосувати до імен файлів функцію normalize.
Слід розуміти, що перейменувати файли треба так, щоб не змінити розширень файлів,
регістр букв розширень теж не можна змінювати.

Функція normalize:
# борщ.jpg -> borsсh.jpg
Проводить транслітерацію кириличного алфавіту на латинський.
Замінює всі символи, крім латинських літер та цифр, на '_'.
Вимоги до функції normalize:

приймає на вхід рядок та повертає рядок;
проводить транслітерацію кириличних символів на латиницю;
замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
транслітерація може не відповідати стандарту, але бути читабельною;
великі літери залишаються великими, а маленькі — маленькими після транслітерації.
Умови для обробки:
зображення переносимо до папки images
документи переносимо до папки documents
аудіо файли переносимо до audio
відео файли до video
архіви розпаковуються, та їх вміст переноситься до папки archives
файли з невідомими розширеннями скласти в папку other
Критерії прийому завдання
всі файли перейменовуються за допомогою функції normalize.
розширення файлів не змінюється після перейменування.
порожні папки видаляються
скрипт ігнорує папки archives, video, audio, documents, images, others;
розпакований вміст архіву переноситься до папки archives у підпапку, названу так само,
як і архів, але без розширення у кінці. Зламані архіви, які не розпаковуються, треба видалити;
В результатах роботи повинні бути:

Список файлів у кожній категорії (музика, відео, фото та ін.)
Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
Перелік всіх розширень, які скрипту невідомі.
Цей результат або вивести в консоль, або зберегти в файл.
"""
from pathlib import Path
import shutil
import sys
from normalize import normalize
import file_parser as parser

# C:/Users/pc/Desktop/заняття/економіка


def handler(filename: Path, target_folder: Path):
    # створення папки
    target_folder.mkdir(exist_ok=True, parents=True)
    # заміняємо шлях до файлу + перетворюємо кирилицю на латиницю
    filename.replace(target_folder / normalize(filename.name))
    # C:/Users/pc/Desktop/заняття/економіка.txt -> C:/Users/pc/Desktop/заняття/TXT/ekonomika.txt


def handler_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не вдалось видалити папку {folder.name}')


def handler_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    # створить папку і розпакувать туди архів
    # беремо суфікс у файла і забираємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # створюємо папку для архіву з іменем файлу
    folder_for_file.mkdir(exist_ok=True, parents=True)

    try:
        shutil.unpack_archive(str(filename), str(folder_for_file))
    except shutil.ReadError():
        print(f'Це не архів, або непідтримуваний формат архіву! {filename.name}')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def main(folder: Path):
    parser.scan(folder)

    for file in parser.JPEG_IMAGES:
        handler(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handler(file, folder / 'images' / 'JPG')
    for file in parser.SVG_IMAGES:
        handler(file, folder / 'images' / 'SVG')
    for file in parser.PNG_IMAGES:
        handler(file, folder / 'images' / 'PNG')

    for file in parser.PPTX_DOCUMENTS:
        handler(file, folder / 'documents' / 'PPTX')
    for file in parser.TXT_DOCUMENTS:
        handler(file, folder / 'documents' / 'TXT')
    for file in parser.DOC_DOCUMENTS:
        handler(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handler(file, folder / 'documents' / 'DOCX')
    for file in parser.CSV_DOCUMENTS:
        handler(file, folder / 'documents' / 'CSV')
    for file in parser.PDF_DOCUMENTS:
        handler(file, folder / 'documents' / 'PDF')

    for file in parser.OTHER:
        handler(file, folder / 'OTHERS')

    for file in parser.ARCHIVES:
        handler_archive(file, folder / 'ARCHIVES')

    for folder in parser.FOLDERS[::-1]:
        handler_folders(folder)


if __name__ == "__main__":
    print(sys.argv)
    folders_for_scan = Path(sys.argv[1])
    print(f'Start in folder: {folders_for_scan}')
    main(folders_for_scan)

# C:\Users\pc\Desktop\заняття\vitalik_lessons\lesson12\test_dir
