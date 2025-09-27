def hesapla():
    print("Toplama için +, Çıkarma için -, Çarpma için *, Bölme için /")
    s1 = float(input("Birinci sayı: "))
    s2 = float(input("İkinci sayı: "))
    op = input("İşlem: ")
    if op == '+': print(s1 + s2)
    elif op == '-': print(s1 - s2)
    elif op == '*': print(s1 * s2)
    elif op == '/': print(s1 / s2)
    else: print("Geçersiz işlem")

hesapla()
