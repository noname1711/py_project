import cv2
import numpy as np

# Bảng ký tự ASCII theo độ sáng
ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, width=100):
    """Chuyển đổi khung hình thành ASCII art."""
    # Tính tỷ lệ khung hình
    height, original_width = frame.shape
    aspect_ratio = original_width / height
    new_width = width
    new_height = int(width / aspect_ratio * 0.55)  # Điều chỉnh tỷ lệ

    # Resize khung hình
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Chuyển khung hình thành ASCII
    ascii_frame = []
    for row in resized_frame:
        ascii_row = "".join(ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))] for pixel in row)
        ascii_frame.append(ascii_row)
    return ascii_frame

def ascii_to_image(ascii_frame, font_scale=0.5, font_thickness=1, output_size=(1920, 1080)):
    """Chuyển ASCII art thành hình ảnh."""
    # Tạo nền đen
    image = np.zeros((output_size[1], output_size[0], 3), dtype=np.uint8)
    image.fill(0)  # Màu đen

    font = cv2.FONT_HERSHEY_SIMPLEX
    x_offset, y_offset = 20, 20  # Khoảng cách từ mép ảnh

    for y, line in enumerate(ascii_frame):
        y_position = y_offset + y * int(20 * font_scale)
        cv2.putText(image, line, (x_offset, y_position), font, font_scale, (255, 255, 255), font_thickness)
    return image

# Đọc video gốc
input_video_path = "Download.mp4"
cap = cv2.VideoCapture(input_video_path)

# Thông số video đầu ra
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = 1920
frame_height = 1080
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_path = "ascii_output.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển khung hình sang grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Chuyển đổi khung hình sang ASCII
    ascii_frame = frame_to_ascii(gray_frame, width=120)

    # Chuyển ASCII art thành hình ảnh
    ascii_image = ascii_to_image(ascii_frame, font_scale=0.5, output_size=(frame_width, frame_height))

    # Ghi khung ASCII vào video
    out.write(ascii_image)

cap.release()
out.release()
cv2.destroyAllWindows()
