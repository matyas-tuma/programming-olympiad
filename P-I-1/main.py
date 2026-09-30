first_line = True
entry = []
cabinet = []

num_of_inputs = int(input())
for i in range(num_of_inputs):
    entry.append(list(map(int, input().split())))

for line in entry:
    if line[0] == 1:
        insertable = True
        for item in cabinet:
            for i in range(2, line[1] + 1):
                if item % i == 0 and line[1] % i == 0:
                    insertable = False
        if insertable:
            print("ANO")
            cabinet.append(line[1])
        else:
            print("NE")
    else:
        try:
            cabinet.remove(line[1])
        except:
            pass
