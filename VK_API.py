import requests

id = 6294985  # id приложения
my_id = 1786057
token = "659ce82a2b0eb6208f5698cb409234c3c6326656c2664cae74535666962871b7cf799428048c82c7394c4"


def Mutual_friends(id_1, id_2):
    params = {
        "access_token": token,
        "source_uid": id_1,  # идентификатор пользователя, чьи друзья пересекаются с друзьями пользователя
        "target_uid": id_2,  # идентификатор пользователя, с которым необходимо искать общих друзей.
        "order": "",  # порядок, в котором нужно вернуть список общих друзей.
        "count": "",  # оличество общих друзей, которое нужно вернуть.
        "offset": ""  # смещение, необходимое для выборки определенного подмножества общих друзей.

    }
    response = requests.get("https://api.vk.com/method/friends.getMutual", params)
    return (response.json())


id_1 = int(input("Введите ID первого пользователя\n"))
id_2 = int(input("Введите ID второго пользователя\n"))

print(Mutual_friends(id_1, id_2))
