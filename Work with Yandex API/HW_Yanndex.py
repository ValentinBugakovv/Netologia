import requests


def translate_it(text, first_lang):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20171207T124103Z.7702fdc505d040fe.ef594f9cff61c5bfc1b92345ee7db29f38bce79b'

    params = {
        'key': key,
        'lang': ''.join((first_lang, '-', "ru")),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


main_dir = {"De.txt": "de",
            "ES.txt": "es",
            "FR.txt": "fr"
            }


def translate(file, first_lang, new_file):
    with open(file) as f:
        file = f.readlines()
        a = translate_it(file, first_lang)
    with open(new_file, 'w') as w:
        w.write(a)
    return a


#print(translate('DE.txt', 'de',"DE-RU.txt"))
#print(translate("ES.txt","es", "ES-RU.txt"))
print(translate("FR.txt", "fr","FR-RU.txt"))
