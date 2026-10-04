entry = []
cabinet = []

num_of_inputs = int(input())
for _ in range(num_of_inputs):
    entry.append(list(map(int, input().split())))

def rozklad(num1):
    num2 = 2
    delitele = []
    while num1 > 1:
        while num1 % num2 == 0:
            delitele.append(num2)
            num1 = num1 // num2
        num2 += 1
    return(delitele)

def test():
    global cabinet
    global rozklad_vstupu
    for rozklad_kabinet in cabinet:
        for i in rozklad_kabinet:
            for n in rozklad_vstupu:
                if i == n:
                    print("NE")
                    return
    print("ANO")
    cabinet.append(rozklad_vstupu)
    return

for line in entry:
    rozklad_vstupu = rozklad(line[1])
    if line[0] == 1:
        test()
    else:
        try:
            cabinet.remove(rozklad(line[1]))
        except:
            pass
