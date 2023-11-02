bo_tak = []

for i in range(4):

    if i % 2 != 0:

        list_i = []

        for j in range(4):

            if j % 2 == 0:
                list_i.append(j+1)

            else:
                list_i.append(69)

        bo_tak.append(list_i)

    else:
        bo_tak.append(420)
      
print(bo_tak)

bo_tak2 = [420 if i % 2 == 0 else [j + 1 if j % 2 == 0 else 69 for j in range(4)] for i in range(4)]

print(bo_tak2)