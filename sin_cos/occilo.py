import numpy as np
import matplotlib.pyplot as plt

# Nhập các tham số từ người dùng
f = float(input("Nhập tần số f: "))
alpha = float(input("Nhập độ lệch pha alpha (đơn vị radian): "))
beta = float(input("Nhập độ lệch pha beta (đơn vị radian): "))
t_min = float(input("Nhập giá trị t tối thiểu: "))
t_max = float(input("Nhập giá trị t tối đa: "))
num_points = int(input("Nhập số điểm tính toán: "))

# Tạo vector thời gian
t = np.linspace(t_min, t_max, num_points)

# Định nghĩa các hàm số
x = np.sin(2 * np.pi * f * t + alpha)
y = np.cos(2 * np.pi * f * t + beta)

# Tìm các điểm giao nhau
dx = np.diff(x)
dy = np.diff(y)
t_intersect = []

for i in range(len(dx) - 1):
    if np.sign(dx[i]) != np.sign(dx[i + 1]) and np.sign(dy[i]) != np.sign(dy[i + 1]):
        t_intersect.append(t[i])

# Tính toán các điểm giao nhau
x_intersect = np.sin(2 * np.pi * f * np.array(t_intersect) + alpha)
y_intersect = np.cos(2 * np.pi * f * np.array(t_intersect) + beta)

# Vẽ các đồ thị riêng biệt
plt.figure(figsize=(15, 5))

# Đồ thị 1: x(t)
plt.subplot(1, 3, 1)
plt.plot(t, x, 'b', label='x(t) = sin(2πft + α)')
plt.title('x(t) = sin(2πft + α)')
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend()

# Đồ thị 2: y(t)
plt.subplot(1, 3, 2)
plt.plot(t, y, 'r', label='y(t) = cos(2πft + β)')
plt.title('y(t) = cos(2πft + β)')
plt.xlabel('Time t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()

# Đồ thị 3: Các điểm giao nhau và hình từ các điểm giao nhau
plt.subplot(1, 3, 3)
plt.scatter(t_intersect, x_intersect, color='black', zorder=5, label='Intersections')
plt.plot(x_intersect, y_intersect, 'go-', label='Intersection Shape')
plt.title('Intersection Points and Shape')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()

# Hiển thị các đồ thị
plt.tight_layout()
plt.show()
