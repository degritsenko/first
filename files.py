#считаем количество символов в файле, через совю функцию
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count = count +1
    return count

#читаем содержимое файла на файловой системе
file = input("input a filename: ")
with open(file) as f:
    text= f.read()
#print (text)
print(count_char(text, "r"))

#считаем процент символов
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))