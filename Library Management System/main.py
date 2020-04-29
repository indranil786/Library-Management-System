"""
This is a simple demonstration of Library Management System.
In this project, I have written only the Admin Panel part.
It is just a simple demonstration and I agree to the fact that the code
could e a lot simpler and could be more efficient, however this is my first try to build
a project, in the near future I hope to improvise it into a better one.

The Books are stored in the form of Individual Files created with their book name.
I have used files which are created/stored in the same directory, as that of the
Python File.(As a replacement for Data Base)

The System can perform the following functions:
1.Add Books to The Library
2.Display details of all the books present in the Library
3.Search a particular Book
4.Borrow a Book
5.Return a Book
6.See the List of Books Borrowed

"""
Books = []
Lend = {}
class Admin:
    # Adding Booking To the Library
    def add_book(self, bookname, author, publisher, isbn, quantity):

        self.bookname = bookname
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.quantity = quantity
        # testing
        # with open(f"{bookname}.txt", 'w') as fbook:

        fbook = open(f"{self.bookname}.txt", 'w')
        fbook.write(f"{self.bookname}\n{self.author}\n{self.publisher}\n{self.isbn}\n{self.quantity}")
        fbook.close()
        Books.append(self.bookname)

        print("\nDetails Added Successfully")

    # Method to Display All the Books
    @staticmethod
    def display_book():
        if len(Books) != 0:
            print("The details of the Following Books are : \n")
            # for i in range(len(Books)):
            for i in range(len(Books)):
                # f = Books[i]
                # for j in f:
                # testing
                with open(f"{Books[i]}.txt") as carry:
                    d = carry.readlines()
                print(f"Name of Book : {d[0]}")
                print(f"Author Name : {d[1]}")
                print(f"Publishers : {d[2]}")
                print(f"ISBN number : {d[3]}")
                print(f"Quantity : {d[4]}")
                print("\n\n")

        else:
            print("There are no books to display ! \n")

    # Method To Borrow a Book From the Library
    def lend_book(self, bookrequest):
        global flag
        if len(Books) != 0:
            self.bookrequest = bookrequest
            flag = False
            for i in range(len(Books)):
                f = Books[i]

                if f == self.bookrequest:
                    flag = True
                    with open(f"{self.bookrequest}.txt") as bk:
                        d = bk.readlines()
                        num = int(d[len(d) - 1])
                    if num < 1:
                        print("Sorry this book is out of stock")

                    else:
                        print("This Book is in stock.")

                        member_name = input("Please enter the name of the borrower ")
                        if (member_name, self.bookrequest) not in Lend.items():
                            Lend[member_name] = self.bookrequest
                            num = num - 1
                            # print(num)
                            with open(f"{self.bookrequest}.txt", 'r+') as bg:
                                l = bg.readlines()
                                l[len(l) - 1] = str(num)
                                bg.seek(0)
                                bg.writelines(l)
                            print("Details taken into account ")
                        else:
                            print('You have already borrowed this book ')

                    break
                else:
                    flag = False
            if flag == 0:
                print(f"The Book {self.bookrequest} is not available\n")
        else:
            print("There are no books currently sorry !")

    # Method to return a Book to the Library
    def return_book(self, bookreturn, returnname):
        self.bookreturn = bookreturn
        self.returnname = returnname

        if (self.returnname, self.bookreturn) in Lend.items():
            del Lend[self.returnname]
            with open(f"{self.bookreturn}.txt", 'r+') as bg:
                l = bg.readlines()
                num = int(l[len(l) - 1])
                num = num + 1
                l[len(l) - 1] = str(num)
                bg.seek(0)
                bg.writelines(l)
            print("Book Returned Successfully ")
        else:
            print("You have not yet borrowed this book ")

    # Method to search for the details of a particular book
    def search(self, booksearch):
        if len(Books) != 0:
            self.booksearch = booksearch
            if self.booksearch in Books:
                print("\nBook Found! The details of the searched book are : \n")
                with open(f"{self.booksearch}.txt") as carry:
                    d = carry.readlines()

                print(f"Name of Book : {d[0]}")
                print(f"Author Name : {d[1]}")
                print(f"Publishers : {d[2]}")
                print(f"ISBN number : {d[3]}")
                print()

            else:
                print("This Book is not Available in Library")
        else:
            print("No books available in the Library to search ")

    # The List of all the Books that are Borrowed
    @staticmethod
    def due_list():
        if len(Lend) != 0:
            print("\n\n***************** List  of Books that are due *****************")
            print("Books Due\t\t\tName of Borrower")
            print()
            for i in Lend:
                print(f"{Lend[i]}\t\t\t\t{i}")
            print("\n")
        else:
            print("There is no List of Books being borrowed\n")


# Main Function
if __name__ == '__main__':
    while True:
        print("\n*************************** Library Management System *******************************")
        print("Services: \n")
        print("1.Add Books to The Library")
        print("2.Display details of all the books present in the Library")
        print("3.Search a particular Book")
        print("4.Borrow a Book")
        print("5.Return a Book")
        print("6.See the List of Books Borrowed")
        print("7.To exit from the Library Management System")
        print("\nPress from 1-6 to select from the options shown\n")
        # try catch exception check in case the user gives his choice in other format than that of a integer
        try:
            n = int(input("Enter Your Choice "))
            obj = Admin()
            if n == 1:
                print()
                bookname = input("Enter The Book Name ")
                flag = 0
                for i in range(len(Books)):
                    if Books[i] == bookname:
                        flag = 1
                        break
                    else:
                        flag = 0
                if flag == 0:
                    author = input("Enter the Author Name ")
                    publisher = input("Enter the Publishers Name ")
                    isbn = input("Enter the Isbn Name ")
                    quantity = input("Enter the Quantity ")
                    obj.add_book(bookname, author, publisher, isbn, quantity)

                else:
                    print("Book is Already present in the Library\n")
            elif n == 2:
                Admin.display_book()
            elif n == 3:
                s = input("\n\nEnter the name of the book that you want to search ")
                obj.search(s)

            elif n == 4:
                booknm = input("\nEnter the book that you want to borrow ")
                obj.lend_book(booknm)
            elif n == 5:
                if len(Lend) != 0:
                    bookreturn = input("\n\nEnter The name of the Book you want to return ")
                    returnname = input("Enter Your Name ")
                    obj.return_book(bookreturn, returnname)
                else:
                    print("\nThere are no books borrowed to be returned \n")

            elif n == 6:
                Admin.due_list()
            elif n == 7:
                print("\n\nThank You For Using Our Library Management System! Have a good Day\n\n")
                break
            else:
                print("Sorry You have made an Invalid Choice\n")
        except ValueError:
            print("\nSorry! You have to Enter a Integer Number as choice!\n")

