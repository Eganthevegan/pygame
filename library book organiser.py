books = ["Matilda", "Wonder", "The Wild Robot"]

books.append("Harry Potter")           
books.remove("Wonder")                 
books.sort()                           
books.reverse()                        

print("Books List:", books)
print("Total Books:", len(books))
print("First Book:", books[0])          
print("Slice:", books[0:2])             

librarian = {"name": "Ms. Priya", "shift": "Morning"}
librarian["shift"] = "Full-Time"       
librarian["dept"] = "Children's"       

print("\nLibrarian Details:", librarian)
print("Librarian Name:", librarian["name"])

book_ids = [101, 102, 103]
book_names = ["Matilda", "The Wild Robot", "Harry Potter"]

book_directory = dict(zip(book_ids, book_names))
print("\nBook Directory:", book_directory)