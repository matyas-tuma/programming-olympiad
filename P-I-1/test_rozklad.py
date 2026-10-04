def rozklad(num1):
    num2 = 2
    delitele = []
    while num1 > 1:
        while num1 % num2 == 0:
            delitele.append(num2)
            num1 = num1 // num2
        num2 += 1
    print(delitele)

rozklad(5645014502568777777777777777897864564144)
