import csv

'''
Доп задание заключалось в том, что если у меня в строке есть несколько фамилий, а именно в n-количестве, то записать
 в рейтинг эти фамилии как отдельные с таким же балом как в строке
Пример:
ВХОД:	Орлов,Ямковий,Шабанов,90,80,70,90,88,TRUE

ВЫХОД:
	Орлов:85
	Ямковий:85
	Шабанов:85
'''

file = open('students.csv', newline='')
reader = csv.reader(file)
header = next(reader)
data = []
data_marks = []
mid = 0
globalmid = 0
for row in reader:
    mid = 0
    data_names = []
    kontrakt = row[6]
    if kontrakt == 'FALSE':
        continue
    row.pop()
    for i in row:
        if not i.isdigit():
            data_names.append(i)
        else:
            mid += round(int(i) / 5)
            globalmid += mid
    for i in data_names:
        data.append([i, mid])
print(data)
data = sorted(data, key=lambda mark: mark[1])
someint = round(len(data) * 40 / 100)
data = data[someint:]
minimum = str(data[0][1])
print(minimum)


def writer():
    with open('rating.csv', mode='w') as rating:
        rating_writer = csv.writer(rating, delimiter=':')
        rating.write('Мінімільний бал для виходу на стипендію:' + minimum + '\n' * 2)
        for i in range(len(data)):
            rating_writer.writerow(data[i])


writer()
