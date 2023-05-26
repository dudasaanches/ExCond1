ano = int(input("Digite o ano que nasceu: "))

v = 2023 - ano

if v < 18:
    print("Menor de idade")
else:
    print("Maior de idade")