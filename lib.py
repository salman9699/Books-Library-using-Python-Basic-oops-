class Library:
    def __init__(self, lst, name):
        self.book_list = lst
        self.name = name
        self.lendDict = {}

    def display_Books(self):
        print(f"List of books in our library : {self.name}")
        for book in self.book_list:
            print(book)

    def display_LentBooks(self):
        if len(self.lendDict) == 0:
            print("No book has been lent!!")
        else:
            for book, user in self.lendDict.items():
                print(f"Book :'{book}' is taken by User : '{user}'")

    def lend_Book(self, user, book):
        if book in self.book_list:
            self.book_list.remove(book)
            self.lendDict.update({book: user})
            print("Lender-book has been updated ...You can take the book now!")
        elif book in self.lendDict.keys():
            print(f"Book is currently not available, it is already taken by user : {self.lendDict[book]}")
        else:
            print(f"This Book is not available in {self.name} Library ")

    def add_Book(self, book):
        self.book_list.append(book)
        print("Book has been added successfully!")

    def return_Book(self, book):
        if book in self.lendDict:
            self.add_Book(book)
            self.lendDict.pop(book)
            print("Book successfully returned to library!!")
        else:
            print(f"Book:'{book}' does not belongs to this library")


if __name__ == '__main__':
    sallu = Library(['Python', 'Best Daddy', 'Rich Dad Poor Dad', 'C++', 'Harry Potter', 'Life Rangers'], "Ranger-Book")

    while (True):
        print(f"Welcome to the {sallu.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Display Lent Books")
        print("3. Lend a Book")
        print("4. Add a Book")
        print("5. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option!!")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            sallu.display_Books()

        elif user_choice == 2:
            sallu.display_LentBooks()

        elif user_choice == 3:
            book = input("Enter a name of book you want to lend : ")
            user = input("Enter your name : ")
            sallu.lend_Book(user, book)

        elif user_choice == 4:
            book = input("Enter a name of the book you want to add : ")
            sallu.add_Book(book)

        elif user_choice == 5:
            book = input("Enter a name of the book you want to return : ")
            sallu.return_Book(book)

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
