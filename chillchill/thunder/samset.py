import pygame
import random

# Khởi tạo pygame
pygame.init()
pygame.mixer.init() # Khởi tạo âm thanh
# Tải âm thanh
a1 = pygame.mixer.Sound(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\thunder_os_1-89682.mp3")
# Linh tải: https://pixabay.com/vi/sound-effects/thunder-os-1-89682/
# Lưu ý: Nhớ tải âm thanh về, chỉnh lại đường dẫn
# Kích thước cửa sổ
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) # Tạo cửa sổ
pygame.display.set_caption("Hiệu ứng Sấm sét")
# Màu sắc
WHITE = (255, 255, 0) 
BLACK = (0, 0, 0)

# Hàm tạo sấm sét
def draw_lightning():
    for _ in range(10): # Số lượng tia sét
        start_x = random.randint(400, 400) # Tọa độ ban đầu
        start_y = 0 # Độ cao bắt đầu
        points = [(start_x, start_y)] # Tạo mảng tọa độ các điểm trong sấm sét
        length = random.randint(10, 50) # Tạo chiều dài sấm sét
        
        # Tạo sấm sét
        for _ in range(length):
            # Tạo tọa độ điểm tiếp theo
            next_x = points[-1][0] + random.randint(-10, 10) # Tham số cộng phía sau là góc nghiêng của tia sét
            next_y = points[-1][1] + random.randint(5, 20) # Tham số cộng phía sau là độ dài của tia sét
            points.append((next_x, next_y)) # Thêm vào mảng tọa độ điểm
        
        # Vẽ sấm sét lên màn hình
        pygame.draw.lines(screen, WHITE, False, points, 2) # Độ dày của tia sét
        a1.play()  # Phát âm thanh lên khi tia sét xuất hiện
        a1.set_volume(5) # Chỉnh âm lượng
        pygame.display.flip()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Tạo sấm sét khi nhấn SPACE
                    draw_lightning()
                    
    screen.fill(BLACK) # Xóa màn hình
    
    # Tạo sấm sét khi nhấn chuột
    if pygame.mouse.get_pressed()[0] == 1:
        draw_lightning()
    pygame.display.update() # Cập nhật màn hình
    
pygame.quit() # Kết thúc pygame