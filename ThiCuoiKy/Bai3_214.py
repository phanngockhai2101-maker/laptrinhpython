import math

la_chinh_phuong = lambda n: int(math.sqrt(n))**2 == n

def phan_loai_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Không hợp lệ"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Không phải tam giác"
    if a == b == c:
        return "Tam giác đều"
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Tam giác vuông"
    if a == b or b == c or a == c:
        return "Tam giác cân"
    return "Tam giác thường"

la_tam_giac = lambda a, b, c: phan_loai_tam_giac(a, b, c)

n = int(input("Nhập n để kiểm tra số chính phương: "))
print(f"{n} {'là' if la_chinh_phuong(n) else 'không phải'} số chính phương")

a, b, c = map(int, input("Nhập 3 cạnh a b c (cách nhau bằng dấu cách): ").split())
print(la_tam_giac(a, b, c))