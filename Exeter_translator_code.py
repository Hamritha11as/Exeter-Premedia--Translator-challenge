import csv
import time
start=time.time()
d={}
sym=",'_-!@.\\\;<<:?*"
stream=open("C:/Users/Dell/Desktop/Exeter Premedia/frequency.csv","w")
with open("C:/Users/Dell/Desktop/Exeter Premedia/french_dictionary.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        d[row[0]] = row[1]
wordfile=open("C:/Users/Dell/Desktop/Exeter Premedia/find_words.txt")
parafile=open("C:/Users/Dell/Desktop/Exeter Premedia/t8.shakespeare.txt")
l=[]
l2=[]

for i in parafile:
    l.append(i)
l=str(l).split()
for i in range(len(l)):
    for j in sym:
        l[i]=l[i].replace(j,"")
t=[]
temp=[]
for i in d:
    if i in l:
        temp.append(i)
        temp.append(d[i])
        temp.append(l.count(i))
        t.append(temp)
        temp=[]
for i in t:
    stream.write(str(i))
    stream.write("\n")

for i in range(len(t)):
    fin = open("C:/Users/Dell/Desktop/Exeter Premedia/t8.shakespeare.txt","rt")
    data=fin.read()
    data=data.replace(t[i][0],t[i][1])
    fin.close()
    fout=open("C:/Users/Dell/Desktop/Exeter Premedia/t8.shakespeare.translate.txt","wt")
    fout.write(data)
    fout.close()
end=time.time()
textout=open("C:/Users/Dell/Desktop/Exeter Premedia/performance.txt","w")
textout.write("Processing Time ")
textout.write(str(end-start))

