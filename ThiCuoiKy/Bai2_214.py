def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    if is_prime(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải số nguyên tố")

def dem_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    count = sum(1 for i in range(2, n) if is_prime(i))
    print(f"Số lượng số nguyên tố < {n}: {count}")

def uoc_nguyen_to():
    n = int(input("Nhập n: "))
    uoc_nt = [i for i in range(1, n+1) if n % i == 0 and is_prime(i)]
    print(f"Các ước số của {n}, vừa là số nguyên tố: {', '.join(map(str, uoc_nt))}")

kiem_tra_nguyen_to()
dem_nguyen_to()
uoc_nguyen_to()