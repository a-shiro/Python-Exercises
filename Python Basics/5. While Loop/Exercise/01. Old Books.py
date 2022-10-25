searched_book = input()


command = input()
book_count = 0
book_found = False

while command != "No More Books":
    if command == searched_book:
        book_found = True
        break

    book_count += 1
    command = input()

if not book_found:
   print("The book you search is not here!")
   print(f"You checked {book_count} books.")

else:
    print(f"You checked {book_count} books and found it.")