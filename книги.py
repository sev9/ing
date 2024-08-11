file=open('/Users/anastasiasoboleva/Desktop/инжинириум/2.txt')
main=[]

for line in file:
    line=line.replace('\n','')
    line=int(line)
    main.append(line)

count=0
for i in main:
    if i%100==42:
        count+=1

count0=0
for i in main:
    if 50<=i%100<=80:
        count0+=1

print(f'Книг с заклинаниями: {count}')
print(f'Книг с историей Древнего Рима: {count0}')