#zad 2
def f(x):
    #2x2 - 5x + 3
    return 2*x**2 - 5*x + 3

x = 1

for i in range(1, 101):
    new_x = x - f(x)/((4/5)*x)

    if abs(new_x - x) < 0.000001:
        break

    x = new_x

print(f"Mijesce zerowe x ={new_x} znalezione w {i} iteracjach")
    
