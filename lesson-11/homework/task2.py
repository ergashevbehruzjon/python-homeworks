import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('create table if not exists Books (Title text, Author text, Year_Published int, Genre text);')

entries = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]
cursor.executemany('insert into Books (Title, Author, Year_Published, Genre) values (?, ?, ?, ?)', entries)

cursor.execute('update Books set Year_Published = ? where Title = ?', (1950, '1984'))

cursor.execute('select Title, Author from Books where Genre = ?', ('Dystopian',))
dystopian_books = cursor.fetchall()
print("Dystopian Books:")
for book in dystopian_books:
    print(f"Title: {book[0]}, Author: {book[1]}")

cursor.execute('delete from Books where Year_Published < 1950')

cursor.execute('alter table Books add column Rating real')

ratings = [
    ('To Kill a Mockingbird', 4.8),
    ('1984', 4.7),
    ('The Great Gatsby', 4.5)
]
for title, rating in ratings:
    cursor.execute('update Books set Rating = ? where Title = ?', (rating, title))

cursor.execute('select * from Books order by Year_Published asc')
sorted_books = cursor.fetchall()
print("\nBooks sorted by Year Published (ascending):")
for book in sorted_books:
    print(f"Title: {book[0]}, Author: {book[1]}, Year Published: {book[2]}, Genre: {book[3]}, Rating: {book[4]}")

conn.close()