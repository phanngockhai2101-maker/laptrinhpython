import math

chinh_phuong = lambda n: int(math.sqrt(n))**2 == n
hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print("Số chính phương từ 1 đến 10000:")
print([n for n in range(1, 10001) if chinh_phuong(n)])

print("\nSố hoàn thiện từ 1 đến 10000:")
print([n for n in range(1, 10001) if hoan_thien(n)])