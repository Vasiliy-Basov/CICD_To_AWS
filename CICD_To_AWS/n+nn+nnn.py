def nnnnn():
    while True:
        n = input('Введите целое положительное число: ')
        try:
            n = int(n)
        except ValueError:
            print("Error! Это не целое число попробуйте снова.")
        else:
            if n >= 0:
                print('n+nn+nnn=', int(n)+int(str(n)+str(n))+int(str(n)+str(n)+str(n)), sep='')
                # другой вариант:
                # n1 = int("%s" % n)
                # n2 = int("%s%s" % (n, n))
                # n3 = int("%s%s%s" % (n, n, n))
                # print(n1 + n2 + n3)
                break
            else:
                print("Error! Это отрицательное число")
                continue

nnnnn()