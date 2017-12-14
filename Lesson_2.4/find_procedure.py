import os

migration = os.listdir("Migrations")
candidates = set(filter(lambda x: x.endswith('.sql'), migration))
while True:
    word = input("Введите строку для поиска: ").lower()
    candidates_copy = candidates.copy()
    for current_file_name in candidates:
        with open(os.path.join('Migrations', current_file_name)) as current_file:
            data = current_file.read().lower()
            if word not in current_file_name.lower() and word not in data:
                candidates_copy.remove(current_file_name)
    candidates = candidates_copy.copy()
    print(str(len(candidates)) + ' files were found')
    print(candidates)

