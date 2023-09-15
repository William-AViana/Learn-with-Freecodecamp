# read file 
fhand = open('anotacoes-Docker.txt')
read_file = fhand.read()
print(read_file)

#read file with enter name file
file_name = input('Enter a name file: ')
try:
    fhand = open(file_name)
except:
    print('File cannot be opened: ', file_name)
    quit()

count = 0
for line in file_name:
    if line.startswith('ENV'):
        count = count + 1

print('There were', count, 'ENV lines in', file_name)
