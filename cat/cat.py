import cv2
import numpy as np

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
    ascii_frame = ""
    for row in resized_frame:
        for pixel in row:
            # Đảm bảo chỉ số nằm trong giới hạn của ASCII_CHARS
            ascii_frame += ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))]
        ascii_frame += "\n"

    return ascii_frame

# Đọc video
input_video_path = "Download.mp4"
cap = cv2.VideoCapture(input_video_path)

# Xuất ASCII ra file text
output_file = "ascii_video.txt"

with open(output_file, "w") as f:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Chuyển khung hình sang grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Chuyển khung hình sang ASCII
        ascii_art = frame_to_ascii(gray_frame)

        # Ghi ASCII art vào file
        f.write(ascii_art)
        f.write("\n" + "=" * 100 + "\n")  # Phân cách giữa các khung

cap.release()
