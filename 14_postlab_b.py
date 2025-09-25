class Book:
    def __init__(self, title, author, price):   
        self.title = title
        self.author = author
        self.price = price
    def display_details(self):   
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)
    def apply_discount(self, discount_percent):   
        discount_amount = (self.price * discount_percent) / 100
        self.price = self.price - discount_amount
# create two book objects
book1 = Book("The Alchemist", "Paulo Coelho", 500)
book2 = Book("Wings of Fire", "A. P. J. Abdul Kalam", 400)
print("Details of Book 1:")
book1.display_details()
print()
print("Details of Book 2:")
book2.display_details()
print()
# apply 10% discount on book1
print("Applying 10% discount on Book 1...")
book1.apply_discount(10)
print("Details of Book 1 after discount:")
book1.display_details()













