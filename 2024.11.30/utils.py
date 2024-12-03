import shutil

def important_message(txt: str) -> str:
    """ Функция important_message принимает обязательным позиционно-ключевым аргументом текст сообщения в виде объекта str.
        Функция important_message возвращает объект str. 
        Задача этой функции — сгенерировать строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'. 
        Ширина рамки определяется текущей шириной окна терминала. 
        Пустое пространство внутри рамки заполняется пробелами. 
        Между верхней границей рамки и первой строчкой текста должен быть отступ одна строчка. 
        Между последней строчкой текста и нижней границей рамки должен быть отступ одна строчка. 
        Текст внутри рамки выравнивается по центру.
        Между боковыми границами рамки и текстом должен быть минимальный отступ два пробела. """
        
    len_txt = len(txt)
    parts_txt = []
    txt_point_start = 0
    width_window = shutil.get_terminal_size()[0]
    width_string = width_window - 6
    
    # Создание списка подстрок для вставки в сообщение без разрыва слов
    while True:
        txt_point_end = txt[:width_string+txt_point_start].rfind(' ')
        if len_txt > width_string:
            parts_txt.append(txt[txt_point_start:txt_point_end])
        else:
            parts_txt.append(txt[txt_point_start:])
            len_txt = 0
        if len_txt < 1:
            break
        len_txt -= (txt_point_end - txt_point_start)
        txt_point_start = txt_point_end
        
    height_window = 4 + len(parts_txt)
    string = "\n"
    for i in range(height_window):
        for j in range(width_window):
            if j == 0 or j == width_window-1:
                string += '#'
            elif i == 0 or i == height_window-1:
                string += '='
            elif i == 1 or i == height_window-2:
                string += ' '
            else:
                string += "  " + parts_txt[i-2].center(width_string) + "  #"
                break
    return string
    