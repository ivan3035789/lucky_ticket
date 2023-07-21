a, b, c, d, e, f = input()
if len(a + b + c + d + e + f) == 6:
    if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
        print('Счастливый')
    else:
        print('Обычный')
