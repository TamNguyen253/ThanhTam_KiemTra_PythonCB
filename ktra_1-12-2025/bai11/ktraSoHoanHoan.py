def isSHH(x):
    tongUoc = 0
    for i in range(1, x):
        if x % i == 0:
            tongUoc += i
    if tongUoc == x:
        print(f'{x} là số hoàn hảo')
    else:
        print(f'{x} ko phải số hoàn hảo')
