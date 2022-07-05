notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break

    importance_of_task, to_do = command.split("-")
    index_in_notes = int(importance_of_task) - 1
    notes.pop(index_in_notes)
    notes.insert(index_in_notes, to_do)

result = [el for el in notes if not el == 0]
print(result)


