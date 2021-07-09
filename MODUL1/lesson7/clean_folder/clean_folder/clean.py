import sys
from pathlib import *
from shutil import rmtree, unpack_archive


images_sample = [".JPEG", ".PNG", ".JPG", ".SVG"]
video_sample = [".AVI", ".MP4", ".MOV", ".MKV"]
documents_sample = [".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"]
music_sample = [".MP3", ".OGG", ".WAV", ".AMR"]
archive_sample = [".ZIP", ".GZ", ".TAR"]

working_dir = ("documents", "images", "audio", "video", "archives", "unknown")


def creating_directories(directory_to_scan):
    """
        Creating working directories
    """
    Path(directory_to_scan/"documents").mkdir(exist_ok=True)
    Path(directory_to_scan/"images").mkdir(exist_ok=True)
    Path(directory_to_scan/"audio").mkdir(exist_ok=True)
    Path(directory_to_scan/"video").mkdir(exist_ok=True)
    Path(directory_to_scan/"archives").mkdir(exist_ok=True)
    Path(directory_to_scan/"unknown").mkdir(exist_ok=True)


def normalize(directory_to_scan):
    """
        Transliterates files names from the Cyrillic alphabet into Latin.
    """
    pth = Path(directory_to_scan)
    for item in pth.iterdir():
        if item.is_dir():
            normalize(item)
        else:
            if item.is_file():
                file_normalized = transliterate(item.stem)
                suffix = item.suffix
                Path(item).rename(Path(Path(item.parent) / (file_normalized + suffix)))


def removing_empty_directories(directory_to_scan):

    pth = Path(directory_to_scan)
    list_dir = reversed(list(pth.glob("*/")))
    for item in list_dir:                           # iterate directories from leaves to root (psevdorecursion)
        if item.name in working_dir:
            continue
        else:
            rmtree(item, ignore_errors=True)


def sorting_files(directory_to_scan, root):
    """
        Replacing the file paths. An alternative to moving files.
        Only use the library pathlib.
    """
    pth = Path(directory_to_scan)
    for item in pth.iterdir():
        if item.is_dir() and item.name in working_dir:
            continue
        elif item.is_dir():
            sorting_files(item, root)
        else:
            if item.name == "hw6_v3_pathlib_only.py":
                pass
            elif item.is_file() and item.suffix.upper() in documents_sample:
                Path(item).rename(Path(Path(root) / "documents" / item.name))
            elif item.is_file() and item.suffix.upper() in images_sample:
                Path(item).rename(Path(Path(root) / "images" / item.name))
            elif item.is_file() and item.suffix.upper() in video_sample:
                Path(item).rename(Path(Path(root) / "video" / item.name))
            elif item.is_file() and item.suffix.upper() in music_sample:
                Path(item).rename(Path(Path(root) / "music" / item.name))
            elif item.is_file() and item.suffix.upper() in archive_sample:
                Path(Path(root) / "archives" / item.stem).mkdir(exist_ok=True)
                unpack_archive(item, Path(root) / "archives" / item.stem)       # unpacking archives
                item.unlink()                                                   # working directories
            else:
                Path(item).rename(Path(Path(root) / "unknown" / item.name))


def transliterate(string):
    """
        Transliterates the Cyrillic alphabet into Latin.
        Replaces all characters except Latin letters, numbers with '_'.
    """
    capital_letters = {'А': 'A',
                       'Б': 'B',
                       'В': 'V',
                       'Г': 'G',
                       'Д': 'D',
                       'Е': 'E',
                       'Ё': 'E',
                       'Ж': 'Zh',
                       'З': 'Z',
                       'И': 'I',
                       'Й': 'Y',
                       'К': 'K',
                       'Л': 'L',
                       'М': 'M',
                       'Н': 'N',
                       'О': 'O',
                       'П': 'P',
                       'Р': 'R',
                       'С': 'S',
                       'Т': 'T',
                       'У': 'U',
                       'Ф': 'F',
                       'Х': 'H',
                       'Ц': 'Ts',
                       'Ч': 'Ch',
                       'Ш': 'Sh',
                       'Щ': 'Sch',
                       'Ъ': '',
                       'Ы': 'Y',
                       'Ь': '',
                       'Э': 'E',
                       'Ю': 'Y',
                       'Я': 'Ya', }

    lower_case_letters = {'а': 'a',
                          'б': 'b',
                          'в': 'v',
                          'г': 'g',
                          'д': 'd',
                          'е': 'e',
                          'ё': 'e',
                          'ж': 'zh',
                          'з': 'z',
                          'и': 'i',
                          'й': 'y',
                          'к': 'k',
                          'л': 'l',
                          'м': 'm',
                          'н': 'n',
                          'о': 'o',
                          'п': 'p',
                          'р': 'r',
                          'с': 's',
                          'т': 't',
                          'у': 'u',
                          'ф': 'f',
                          'х': 'h',
                          'ц': 'ts',
                          'ч': 'ch',
                          'ш': 'sh',
                          'щ': 'sch',
                          'ъ': '',
                          'ы': 'y',
                          'ь': '',
                          'э': 'e',
                          'ю': 'y',
                          'я': 'ya', }

    translit_string = ""

    for char in string:
        if char in r"!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~":
            continue
        elif char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
        elif char.isdigit() or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            char = char
        else:
            char = "_"
        translit_string += char
    return translit_string


def main():

    global input_arg
    if len(sys.argv) > 1:
        input_arg = sys.argv[1]
        directory_to_scan = Path(input_arg)
    else:
        input_arg = "."
        directory_to_scan = Path.cwd()

    if directory_to_scan.exists():
        normalize(directory_to_scan)
        creating_directories(directory_to_scan)
        sorting_files(directory_to_scan, input_arg)
        removing_empty_directories(directory_to_scan)
    else:
        print(f"path {directory_to_scan.absolute()} not exist")


if __name__ == "__main__":
    main()
