import os

migrations = os.listdir("Migrations")
candidates = filter(lambda x: x.endswith('.sql'), migrations)
while True:
    word = input("Введите строку для поиска: ").lower()
    new_candidates = []
    for current_file_name in candidates:
        with open(os.path.join('Migrations', current_file_name)) as current_file:
            data = current_file.read().lower()
            if word in current_file_name.lower() or word in data:
                new_candidates.append(current_file_name)
    candidates = new_candidates
    print(f"{str(len(candidates))} files were found")
    print(candidates)
