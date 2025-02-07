import time

def my_function1():
    print("1.fonksiyon başlıyor")
    time.sleep(5)
    print("1.fonksiyon bitiyor")
    return 5


def my_function2():
    print("2.fonksiyon başlıyor")
    time.sleep(5)
    print("2.fonksiyon bitiyor")
    return 10


if __name__ == "__main__":
    x = my_function1()
    y = my_function2()
    print(f"my function1 çalışması sonucu x'in değeri {x}")
    print(f"my function2 çalışması sonucu x'in değeri {y}")