def lab9n1():
    from PIL import Image, ImageFilter
    import os

    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"

    h = [a, b, c, d]
    count = 0
    for file in h:
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.EMBOSS)
        new_img.show()
        try:
            os.mkdir("F:/photos")
        except:
            pass
        new_img.save(f"F:/photos/new_img{count}.png")


def lab9n2():
    from PIL import Image, ImageFilter
    import os

    a = "1.jpg"
    b = "2.tiff"
    c = "3.jpg"
    d = "4.jpg"

    h = [a, b, c, d]
    count = 0
    for file in h:
        if file.endswith('.jpg') or file.endswith('.png'):
            count += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("F:/photos")
            except:
                pass
            newimg.save(f"F:/photos/newimg{count}.png")

def lab9n3():
    total = 0
    with open('F:/photos/data.csv', 'r') as f:
        lines = f.readlines()
        print("Нужно купить:")
        for line in lines[1:]:
            product, quantity, price = line.strip().split(',')
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая сумма: {total} руб.")

lab9n3()