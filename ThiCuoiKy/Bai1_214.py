dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm):>? "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm):>? "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm):>? "))
n = int(input("Số lượng số lẻ cần hiển thị:>? "))

dien_tich = dai * rong
the_tich = dai * rong * cao

print(f"Diện tích đáy hình chữ nhật = {dien_tich:.{n}f} cm\u00b2")
print(f"Thể tích hình khối= {the_tich:.{n}f} cm\u00b3")