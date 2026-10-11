entry = []
cabinet = []

num_of_inputs = int(input())
for _ in range(num_of_inputs):
    entry.append(list(map(int, input().split())))

def nsd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return(nsd(num2, num1 % num2))

def check(num1, cabinet):
    for item in cabinet:
        if line[1] > item:
            if nsd(num1, item) > 1:
                print("NE")
                return
        else:
            if nsd(item, num1) > 1:
                print("NE")
                return

    print("ANO")
    cabinet.append(num1)

for line in entry:
    if line[0] == 1:
        check(line[1], cabinet)
    else:
        try:
            cabinet.remove(line[1])
        except:
            pass
