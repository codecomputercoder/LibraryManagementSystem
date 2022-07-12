class Library:
    def __init__(self,BookList):
        self.books =BookList

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, nameofbook):
        if nameofbook in self.books:
            print(f"You have been issued {nameofbook}. Please keep it safe and return it within 30 days")
            self.books.remove(nameofbook)
            return True
        else:
            print("Sorry, This book is not available / has already been issued to someone else.")
            return False

    def returnBook(self, nameofbook):
        self.books.append(nameofbook)
        print("Thanks for returning this book!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "DataScience","Database", "Python","C++"])
    student = Student()
   
    while(True):
        displaymassage = '''\n Please choose an option:
        1. Show All Books
        2. Request a book
        3. Return a book
        4. Exit
        '''
        print(displaymassage)
        a = int(input("Enter Your choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
