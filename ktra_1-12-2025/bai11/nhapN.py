def nhapN():
    while True:
        try:
            n = int(input('Nhập số: '))
            if n > 0:
                return n
        except ValueError:
            print('Nhập sai kiểu dữ liệu!')