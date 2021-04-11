import pathlib
import sys


fotos_sample = [".JPEG", ".PNG", ".JPG", ".SVG"]
video_sample = [".AVI", ".MP4", ".MOV", ".MKV"]
documents_samle = [".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"]
music_sample = [".MP3", ".OGG", ".WAV", ".AMR"]
archive_sample = [".ZIP", ".GZ", ".TAR"]

fotos = []
video = []
documents = []
music = []
archive = []
unknown = []


def scan_folder(path_folder_to_scan):

    if path_folder_to_scan.is_dir():
        for obj in path_folder_to_scan.iterdir():
            if obj.is_dir():
                scan_folder(obj)
            else:
                if obj.suffix.upper() in fotos_sample:
                    fotos.append(obj.name)
                elif obj.suffix.upper() in video_sample:
                    video.append(obj.name)
                elif obj.suffix.upper() in documents_samle:
                    documents.append(obj.name)
                elif obj.suffix.upper() in music_sample:
                    music.append(obj.name)
                elif obj.suffix.upper() in archive_sample:
                    archive.append(obj.name)
                else:
                    unknown.append(obj.name)
    else:
        print(f"{path_folder_to_scan} is file.")
    return f"The following files were found as a result of scanning ->\n" \
           f"FOTOS:{fotos},\n" \
           f"VIDEO:{video},\n" \
           f"DOCUMENTS:{documents},\n" \
           f"MUSIC:{music},\n" \
           f"ARCHIVES:{archive},\n" \
           f"UNKNOWN FILES:{unknown}"


def main():
    if len(sys.argv) > 1:
        input_arg = sys.argv[1]
    else:
        input_arg = pathlib.Path.cwd()
    path_folder_to_scan = pathlib.Path(input_arg)
    if path_folder_to_scan.exists():
        print(scan_folder(path_folder_to_scan))
    else:
        print(f"path {path_folder_to_scan.absolute()} not exist")


if __name__ == "__main__":
    main()