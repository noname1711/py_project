import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(function, phase_shift, zoom_factor=1.0):
    # Tạo dữ liệu cho trục x từ -2π đến 2π với 1000 điểm
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    # Tính toán giá trị y dựa trên hàm và lệch pha
    if function == 'sin':
        y = np.sin(x + phase_shift)
        function_label = 'sin(x)'
    elif function == 'cos':
        y = np.cos(x + phase_shift)
        function_label = 'cos(x)'
    else:
        print("Hàm không hợp lệ. Chỉ hỗ trợ 'sin' hoặc 'cos'.")
        return
    
    # Áp dụng phóng to/thu nhỏ
    x_zoomed = x / zoom_factor
    y_zoomed = y * zoom_factor
    
    # Vẽ đồ thị
    plt.plot(x_zoomed, y_zoomed, label=f'{function_label} với lệch pha {phase_shift}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Đồ thị của {function_label}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Nhập hàm và lệch pha từ người dùng
function = input("Nhập hàm (sin hoặc cos): ")
phase_shift = float(input("Nhập lệch pha: "))

# Nhập hệ số phóng to/thu nhỏ
zoom_factor = float(input("Nhập hệ số phóng to/thu nhỏ (1.0 cho đồ thị gốc): "))

# Vẽ đồ thị
plot_waveform(function, phase_shift, zoom_factor)
