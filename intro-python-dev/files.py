
with open('numbers.txt', 'w+') as myfile:
    for x in range(25):
        myfile.write(f'Number {x+1}\n')

with open('numbers.txt', 'r') as myfile:
    print(myfile.read())
