searched_book = input()
searched_books = 0

while True:
    book = input()

    if book == searched_book:
        print(f"You checked {searched_books} books and found it.")
        break

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {searched_books} books.")
    break
searched_books += 1
