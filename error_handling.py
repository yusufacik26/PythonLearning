while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))

        print(a / b)
    except ZeroDivisionError:
        print("b sayısı sıfır olamaz")
    except ValueError:
        print("Sadece sayısal değerler girin")
    else:
        print("İşlem tamamlandı")
    
    
