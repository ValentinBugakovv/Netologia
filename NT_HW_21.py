from collections import Counter
import chardet
from pprint import pprint


def check_encoding(fname):
    rawdata = open(fname, "rb").read()
    result = chardet.detect(rawdata)
    return result['encoding']


def top_10(f):
    array = [line.strip().split() for line in f]
    data = []
    m = ()
    for i in range(len(array)):
        for j in range(len(array[i])):
            if len(array[i][j]) > 6:
                data.append(array[i][j])
    p = Counter(data)
    m = (p.most_common(10))
    return m


news = ["newsafr.txt", "newscy.txt", "newsfr.txt", "newsit.txt"]
# ecod = []
# for enc in news:
#     ecod.append(check_encoding(enc)) Определил кодировки

news_dict = {"newsafr.txt": "utf-8",  # руками внес в словарь, но толлько
             "newscy.txt": "ascii",  # удобства, в алгоритме не использовал
             "newsfr.txt": "ISO-8859-5",
             "newsit.txt": "windows-1251"
             }

with open("newsafr.txt", "r", encoding="utf-8") as f:
    print(*(top_10(f)))
with open("newscy.txt", "r", encoding="ascii") as f:
    print(*(top_10(f)))
with open("newsfr.txt", "r", encoding="ISO-8859-5") as f:
    print(*(top_10(f)))
with open("newsit.txt", "r", encoding="windows-1251") as f:
    pprint((top_10(f)))
