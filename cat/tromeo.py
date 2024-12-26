import cv2
import numpy as np

# Chuỗi đại diện cho mức sáng
ASCII_STR = "Ngoc"

def frame_to_ascii(frame, width=50):
    """Chuyển đổi khung hình thành ASCII art với ký tự từ chuỗi 'Ngoc'."""
    height, original_width = frame.shape
    aspect_ratio = original_width / height
    new_width = width
    new_height = int(width / aspect_ratio * 0.55)

    # Resize khung hình
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Chuyển khung hình thành ASCII
    ascii_frame = []
    for row in resized_frame:
        ascii_row = "".join(ASCII_STR[min(pixel // (256 // len(ASCII_STR)), len(ASCII_STR) - 1)] for pixel in row)
        ascii_frame.append(ascii_row)
    return ascii_frame

def ascii_to_image(ascii_frame, font_scale=0.5, font_thickness=1, output_size=(1920, 1080)):
    """Chuyển ASCII art thành hình ảnh với các ký tự phóng to sao cho kín nền."""
    image = np.zeros((output_size[1], output_size[0], 3), dtype=np.uint8)  # Tạo ảnh nền đen
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    x_offset, y_offset = 10, 30

    # Tính toán tỉ lệ font để phóng to ký tự sao cho kín nền
    font_height = int(output_size[1] / len(ascii_frame))  # Phóng to sao cho dòng ASCII chiếm toàn bộ chiều cao
    font_scale = font_height / 20  # Điều chỉnh tỉ lệ font (theo chiều cao dòng)

    # Vẽ từng dòng ASCII lên ảnh
    for y, line in enumerate(ascii_frame):
        y_position = y_offset + y * font_height
        cv2.putText(image, line, (x_offset, y_position), font, font_scale, (255, 255, 255), font_thickness)
    
    return image

# Đọc video gốc
input_video_path = "Download.mp4"
cap = cv2.VideoCapture(input_video_path)

# Thông số video đầu ra
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = 640  # Kích thước nhỏ hơn
frame_height = 480  # Kích thước nhỏ hơn
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Codec MJPEG đơn giản
output_video_path = "ngoc_output.avi"  # Định dạng AVI
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển khung hình sang grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Chuyển đổi khung hình sang ASCII
    ascii_frame = frame_to_ascii(gray_frame, width=80)

    # Chuyển ASCII art thành hình ảnh với các ký tự phóng to sao cho kín nền
    ascii_image = ascii_to_image(ascii_frame, font_scale=0.6, output_size=(frame_width, frame_height))

    # Ghi khung ASCII vào video
    out.write(ascii_image)

cap.release()
out.release()
cv2.destroyAllWindows()
