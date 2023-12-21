#zad 2

def bin2dec(nhood_list):
    return sum([b*2**(2-i) for i, b in enumerate(nhood_list)])

rule_table = {7: 0, 6: 1, 5: 1, 4: 0, 3: 1, 2: 1, 1: 1, 0: 0}

WIDTH, HEIGHT = 100, 100

grid = [[0]* WIDTH for _ in range(HEIGHT)]

grid[0][WIDTH//2] = 1


for i in range(HEIGHT - 1):
    for j in range(1, WIDTH - 1):
        nhood = grid[i][j-1:j+2]
        dziesietna = bin2dec(nhood)
        grid[i+1][j] = rule_table[dziesietna]

#print(grid)

# TODO: Zapisz grid do pliku w formacie .ppm (wystarczy poprzedzić go odpowiednim nagłówkiem)

with open("evolution_ca110.ppm","w") as ppm_file:
    ppm_file.write("P1\n{} {}\n".format(WIDTH, HEIGHT))
    for row in grid:
        ppm_file.write(" ".join(map(str,row)) + "\n")
