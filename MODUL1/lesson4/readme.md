Задача#

У многих на рабочем столе есть папка, которая называется как-то вроде "Разобрать". Как правило, разобрать эту папку руки никогда так и не доходят.

Мы с вами напишем скрипт, который разберет эту папку. В конечном итоге вы сможете настроить эту программу под себя и она будет выполнять индивидуальный сценарий соответствующий вашим нуждам. Для этого наше приложение будет проверять расширение файла (последние символы в имени файла, как правило после точки) и в зависимости от расширения принимать решение к какой категории отнести этот файл.

Скрипт принимает один аргумент при запуске — это имя папки в которой он будет проводить сортировку. Допустим файл с программой называется sort.py, тогда чтобы отсортировать папку /user/Desktop/Хлам надо запустить скрипт командой python sort.py /user/Desktop/Хлам
Критерии приёма задания#

    Для того, чтобы успешно справится с этим заданием вы должны вынести логику обработки папки в отдельную функцию.
    Чтобы скрипт мог пройти на любую глубину вложенности функция обработки папок должна рекурсивно вызывать сама себя когда ей встречаются вложенные папки.

Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам:

    изображения ('JPEG', 'PNG', 'JPG', 'SVG');
    видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
    документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
    музыка ('MP3', 'OGG', 'WAV', 'AMR');
    архивы ('ZIP', 'GZ', 'TAR');
    неизвестные расширения.

Вы можете расширить и дополнить этот список если хотите.

Скрипт выводит результаты работы в консоль.

В результатах работы должны быть:

    Список файлов в каждой категории (музыка, видео, фото и пр.)
    Перечень всех известных скрипту расширений, которые встречаются в целевой папке.
    Перечень всех расширений, которые скрипту неизвестны.
