Задача#

В этом домашнем задании вы должны объединить результаты вашей работы на предыдущих домашних работах. Основная задача -- это завершить скрипт разбора папки. Основное нововведение -- это добавление функций, которые будут отвечать за обработку каждого типа файлов.

Кроме того, все файлы и папки нужно переименовать удалив из названия все потенциально приводящие к проблемам символы. Для этого надо применить к именам файлов функцию normalize из предыдущего домашнего задания. Следует помнить, что переименовать файлы нужно так, чтобы не изменить расширения файлов.

Условия для обработки:

    изображения переносим в папку images
    документы переносим в папку documents
    аудио файлы переносим в audio
    видео файлы в video
    архивы распаковываются и их содержимое переносится в папку archives

Критерии приёма задания#

    все файлы и папки переименовываются при помощи функции normalize из предыдущего задания.
    расширения файлов не изменяются после переименования.
    пустые папки удаляются
    скрипт игнорирует папки archives, video, audio, documents, images;
    распакованное содержимое архива переносится в папку archives в подпапку названную точно так же, как и архив, но без расширения в конце;
    файлы, расширения которых не известны, остаются без изменений.
