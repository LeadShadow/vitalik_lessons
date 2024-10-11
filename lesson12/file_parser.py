import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

OTHER = []
ARCHIVES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
CSV_DOCUMENTS = []
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
    'MP4': MP4_VIDEO,
    'MKV': MKV_VIDEO,
    'MOV': MOV_VIDEO,
    'AVI': AVI_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'CSV': CSV_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
}
# .py -> PY
# .txt -> TXT

# C:\Users\pc\Desktop\заняття\vitalik_lessons\lesson10\task1
# '.py'[1:] -> py
# 'py'.upper() -> 'PY'


def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


# task.txt
def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            # перевіряємо щоб ця папка не була тою в яку ми складаємо файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHERS'):
                FOLDERS.append(item)
                # скануємо вложену папку(рекурсія)
                scan(item)
            continue

        # Пішла робота з файлом
        ext = get_extensions(item.name)
        fullname = folder / item.name
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                # намагайся взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folder_for_scan = sys.argv[1]
    # python file_parser.py <path_to_dir>
    # sys.argv -> sys.argv[0] -> file_parser.py
    print(f'Start in folder: {folder_for_scan}')
    scan(Path(folder_for_scan))
    print(F'TXT DOCUMENTS: {TXT_DOCUMENTS}')
    print(F'OTHER: {OTHER}')
