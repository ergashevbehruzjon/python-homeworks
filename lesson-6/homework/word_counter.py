try:
    file=open("sample.txt","r")
except FileNotFoundError:
    file=open("sample.txt","w+")
    while True:
        line = input("Enter a line (you can enter paragpraph line by line) (empty string to exit): ")
        if not line:
            break
        file.write(line+"\n")
    file.seek(0)

# words = file.read().lower().split()
# words=set()
freq={}
total=0
for word in file.read().lower().split():
    word=word.strip('.').strip(',')
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
        # words.add(word)
    total+=1

num=int(input("How many top common words should be displayed: "))
file2=open("word_count_report.txt","w")
file2.write("Word Count Report\n")

print("-"*50)
print("Total words:", total)
file2.write(f"Total Words: {total}\n")


freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
# print(freq)
freq_k = list(freq.keys())
if num<len(freq):
    print(f"Top {num} common words:")
    file2.write(f"Top {num} Words:\n")
    for i in range(num):
        print(f"{freq_k[i]} - {freq[freq_k[i]]}","times" if freq[freq_k[i]]>1 else "time")
        file2.write(f"{freq_k[i]} - {freq[freq_k[i]]}\n")
else:
    print(f"Top {len(freq)} common words:")
    file2.write(f"Top {len(freq)} Words:\n")
    for i in freq_k:
        print(f"{i} - {freq[i]}","times" if freq[i]>1 else "time")
        file2.write(f"{i} - {freq[i]}\n")
file.close()
file2.close()