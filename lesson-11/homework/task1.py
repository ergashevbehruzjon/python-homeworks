import sqlite3

conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

cursor.execute('create table if not exists Roster(name text, species text, age int);')

entries = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
cursor.executemany('insert into Roster (name, species, age) values (?, ?, ?)', entries)

cursor.execute('update Roster set name = ? where name = ?', ('Ezri Dax', 'Jadzia Dax'))

cursor.execute('select name, age from Roster where species = ?', ('Bajoran',))
bajoran_characters = cursor.fetchall()
print("Bajoran species:")
for character in bajoran_characters:
    print(f"Name: {character[0]}, Age: {character[1]}")

cursor.execute('delete from Roster where age > 100')

cursor.execute('alter table Roster add column rank text')

ranks = [
    ('Benjamin Sisko', 'Captain'),
    ('Ezri Dax', 'Lieutenant'),
    ('Kira Nerys', 'Major')
]
for name, rank in ranks:
    cursor.execute('update Roster set rank = ? where name = ?', (rank, name))

cursor.execute('select * from Roster order by age desc')
sorted_characters = cursor.fetchall()
print("\nCharacters sorted by Age (descending):")
for character in sorted_characters:
    print(f"Name: {character[0]}, Species: {character[1]}, Age: {character[2]}, Rank: {character[3]}")

conn.close()