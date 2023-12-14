#zad 3 

class LinearRegression:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.X_srednia = sum(self.X) / len(self.X)
        self.Y_srednia = sum(self.Y) / len(self.Y)

    def fit(self):
        self.suma_Xk = sum(x ** 2 for x in self.X)
        self.suma_XY = sum(x * y for x, y in zip(self.X, self.Y))
        self.suma_Y = sum(self.Y)
        self.nX = len(self.X)

        self.a = ((self.Y_srednia * self.suma_Xk) - (self.X_srednia * self.suma_XY)) / (self.suma_Xk - self.nX * self.X_srednia ** 2)
        self.b = (self.suma_XY - self.X_srednia * self.suma_Y) / (self.suma_Xk - self.nX * self.X_srednia ** 2)

    def predict(self, x):
        return self.a * x + self.b

    def calc_r_squared(self):
        predicted_values = [self.predict(x) for x in self.X]
        licznik = sum((y_pred - self.Y_srednia) ** 2 for y_pred in predicted_values)
        mianownik = sum((y - self.Y_srednia) ** 2 for y in self.Y)
        rk = licznik / mianownik
        return rk


X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

regresja = LinearRegression(X, Y)
regresja.fit()

print(f"Parametry regresji: a = {regresja.a}, b = {regresja.b}")
x_predict = 6
y_predict = regresja.predict(x_predict)
print(f"Przewidywane Y dla X={x_predict}: {y_predict}")
rk = regresja.calc_r_squared()
print(f"Współczynnik determinacji R^2: {rk}")
