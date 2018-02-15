import requests
import time
import json

api_version = "5.71"
url_vk = 'https://api.vk.com/method/'
api_token = "9373e080ca76cc6ebefc89d5e82b872d0a557a4362042eb8a1f9623dd04bec15425dd7100228b8f5c2a44"


class API:
    last_access_time = time.time()
    MAX_REQUESTS_PER_SECOND = 1.5

    @classmethod
    def throttle(cls):
        current_time = time.time()
        time_diff = current_time - cls.last_access_time
        if time_diff < 1 / cls.MAX_REQUESTS_PER_SECOND:
            time.sleep(1 / cls.MAX_REQUESTS_PER_SECOND - time_diff)
        cls.last_access_time = time.time()


class Entity:
    common_params = {
        'v': api_version,
        'access_token': api_token
    }

    def get_name(self):
        raise NotImplementedError("get_name")

    @classmethod
    def get_data(cls, method, params):
        params.update(cls.common_params)
        response = requests.get(url=url_vk + method, params=params, timeout=1)
        response.raise_for_status()
        response = response.json()
        if "error" in response:
            raise ValueError(response["error"]["error_msg"])
        API.throttle()
        return response


class User(Entity):
    def __init__(self, user_id):
        self.id = user_id
        if type(user_id) is str:
            self.id = User.get_id(user_id)

    @classmethod
    def get_id(cls, user_id):
        response = cls.get_data("users.get", params={"user_ids": [user_id]})
        return response["response"][0].get("id")

    def get_friends(self):
        response = User.get_data("friends.get", params={"user_id": self.id})
        result = []
        for user_id in response["response"].get('items'):
            result.append(User(user_id))
        return result

    def get_groups(self):
        response = User.get_data('groups.get', params={"user_id": self.id})
        return [Group(id) for id in response['response']['items']]

    def get_name(self):
        response = self.get_data("users.get", params={"user_ids": [self.id]})
        return f"{response['response'][0].get('first_name')} {response['response'][0].get('last_name')}"


class Group(Entity):
    def __init__(self, group_id):
        self.id = group_id

    def get_name(self):
        response = self.get_data("groups.getById", params={"group_id": [self.id]})
        return f"{response['response'][0].get('name')}"

    def get_members_counts(self):
        response = self.get_data("groups.getMembers", params={"group_id": [self.id], "count": 0})
        return response["response"].get("count")

    def to_json(self):
        return {"name": self.get_name(), "gid": self.id, "members_count": self.get_members_counts()}

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.id


class VKEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Group):
            return {"name": obj.get_name(), "gid": obj.id, "members_count": obj.get_members_counts()}
        return super().default(obj)


def main():
    user_id = str(input("input Id\n"))
    user = User(user_id)
    friends = user.get_friends()
    groups = set(user.get_groups())
    print("<", end="", flush=True)
    for friend in friends:

        print("-", end="", flush=True)
        try:
            friend_groups = set(friend.get_groups())
            groups -= friend_groups
        except ValueError as err:
            print(err)
    print(">", end="", flush=True)
    groups = list(groups)
    with open("results.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(groups, cls=VKEncoder, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
