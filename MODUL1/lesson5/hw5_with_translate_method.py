def transliterate(string):
    """
    Transliterates the Cyrillic alphabet into Latin.
    Replaces all characters except Latin letters, numbers with '_'.
    """
    cyr_alfabet_str = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    lat_alfabet_str = "_ABVGDEEGZIYKLMNOPRSTUFHC4SC_I_EYAabvgdeegziyklmnoprstufhc4sc_i_eya"
    my_table = string.maketrans(cyr_alfabet_str, lat_alfabet_str, "!\"#$%&'()*\+,-./:;<=>?@[\\]^_`{|}~")
    translit_string = string.translate(my_table)

    return translit_string


string = input("Input string for normalize: ")
print(transliterate(string))