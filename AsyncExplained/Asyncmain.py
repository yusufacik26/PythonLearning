import asyncio  # asenkron çalıştırma kütüphanesi


async def birinciFonksiyon():
    print("Birinci Fonksiyon başladı ")
    await asyncio.sleep(5)  # non blocking delay simulasyonu iki fonksiyonu da çalışmasını sağlar
    print("Birinci Fonksiyon bitti")
    return 5


async def ikinciFonksiyon():
    print("İkinci Fonksiyon başladı")
    await asyncio.sleep(5)  # non blocking delay simulasyonu iki fonksiyonu da çalışmasını sağlar
    print("İkinci Fonksiyon bitti")
    return 10





async def main():
    task1 = asyncio.create_task(birinciFonksiyon())
    task2 = asyncio.create_task(ikinciFonksiyon())
    x = await task1
    y = await task2
    print(x)
    print(y)


if __name__ == "__main__":
    asyncio.run(main())
