# ex02_file.py

f = open("test.txt", "w", encoding="utf-8")
students = ["공주","재원","또리","봄이"]
scores = [90,80,77,65]
for i in range(4):
    data = "%s님은 %s점입니다. \n" %(students[i],scores[i])
    f.write(data)
f.close()


d = open("test.txt", "r", encoding="utf-8")
readData = d.readlines()
for i in readData:
    print(i)
d.close()
