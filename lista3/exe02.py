#Faça um programa que mostre as tabuadas dos números de 1 a 10
for num in range(1, 11):
    print("Tabuada do", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
    print() 
