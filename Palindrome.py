def sayi_kontrol(x):
    if x==x[::-1]:
        print("sayiniz palindrome sayıdır")
    else:
        print("sayiniz palindrome sayı değildir.")
x=input("sayi girin:")
sayi_kontrol(x)
