ask = 'Y'

while ask == 'Y':
    number = int(input('input number > '))
    base = [128, 64, 32, 16, 8, 4, 2, 1]
    binary =[]
    for index in range(len(base)):
        if number >= base[index]:
            number -= base[index]
            binary.append(1)
        elif  number < base[index]:
            binary.append(0)
    print(binary)
    userInput = input('convert another number Y/N > ')
    if userInput.upper() == 'N':
        ask = 'N'
        