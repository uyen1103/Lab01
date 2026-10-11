import os

import cv2

INPUT_PATH = "data/anh.jpg"
OUTPUT_DIR = "outputs/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def out(name):
    return os.path.join(OUTPUT_DIR, name)


# Bước 2: đọc, hiển thị, lưu ảnh
img = cv2.imread(INPUT_PATH)
if img is None:
    raise FileNotFoundError(f"Không đọc được ảnh: {INPUT_PATH}")
cv2.imshow("Anh goc", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(out("anh_moi.png"), img)

# Bước 3: đổi không gian màu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imwrite(out("gray.png"), gray)
cv2.imwrite(out("hsv.png"), hsv)
cv2.imwrite(out("lab.png"), lab)

# Bước 4: cắt và đổi kích thước
crop = img[100:400, 100:400]
nho = cv2.resize(img, (300, 300))
cv2.imwrite(out("crop.png"), crop)
cv2.imwrite(out("resize.png"), nho)

# Bước 5: vẽ hình và thêm chữ
cv2.line(img, (50, 50), (300, 50), (255, 0, 0), 3)
cv2.rectangle(img, (100, 100), (300, 250), (0, 255, 0), 2)
cv2.circle(img, (400, 200), 60, (0, 0, 255), 3)
cv2.putText(img, "Computer Vision", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imwrite(out("ve_hinh.png"), img)
