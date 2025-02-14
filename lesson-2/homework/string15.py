n=input("Enter a sentence: ")
print("The acronym is",''.join([i[0].upper() for i in n.split()]))