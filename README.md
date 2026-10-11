# Lab 01

Dự án thực hành môn Xử lý ảnh và thị giác máy tính bằng Python và OpenCV, tập trung vào các thao tác cơ bản: đọc/ghi ảnh, chuyển đổi không gian màu, cắt và đổi kích thước ảnh, vẽ hình và thêm chữ lên ảnh. Mã nguồn nằm trong `src/lab1.py`, ảnh gốc đặt trong `data/` và các kết quả được lưu vào `outputs/`.

## Mục tiêu

- Đọc, hiển thị và lưu ảnh bằng OpenCV.
- Chuyển đổi ảnh giữa các không gian màu: BGR, Grayscale, HSV, LAB.
- Cắt vùng ảnh (crop) và thay đổi kích thước ảnh (resize).
- Vẽ các hình cơ bản (đường thẳng, hình chữ nhật, hình tròn) và chèn văn bản lên ảnh.
- Lưu các kết quả ra thư mục `outputs/` để quan sát trực quan.

## Nội dung thực hiện

### 1. Đọc, hiển thị và lưu ảnh

- `cv2.imread(...)`: đọc ảnh `data/anh.jpg` (OpenCV đọc theo thứ tự kênh màu BGR).
- `cv2.imshow(...)` và `cv2.waitKey(0)`: hiển thị ảnh gốc, chờ nhấn phím để tiếp tục.
- `cv2.imwrite(...)`: lưu ảnh sang định dạng PNG vào `outputs/`.

### 2. Chuyển đổi không gian màu

| Không gian màu | Hàm sử dụng | Tệp kết quả |
| --- | --- | --- |
| Grayscale | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` | `gray.png` |
| HSV | `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)` | `hsv.png` |
| LAB | `cv2.cvtColor(img, cv2.COLOR_BGR2LAB)` | `lab.png` |

### 3. Cắt và đổi kích thước ảnh

- Cắt ảnh bằng slicing của NumPy: `crop = img[100:400, 100:400]` (vùng 300x300 pixel) -> `crop.png`.
- Đổi kích thước ảnh về 300x300 bằng `cv2.resize(img, (300, 300))` -> `resize.png`.

### 4. Vẽ hình và thêm chữ

- `cv2.line`: vẽ đường thẳng màu xanh dương.
- `cv2.rectangle`: vẽ hình chữ nhật màu xanh lá.
- `cv2.circle`: vẽ hình tròn màu đỏ.
- `cv2.putText`: chèn dòng chữ "Computer Vision" màu trắng.
- Kết quả được lưu vào `ve_hinh.png`.

## Cấu trúc thư mục

```
Lab01/
├── data/
│   └── anh.jpg
├── outputs/
│   ├── anh_moi.png
│   ├── gray.png
│   ├── hsv.png
│   ├── lab.png
│   ├── crop.png
│   ├── resize.png
│   └── ve_hinh.png
├── src/
│   └── lab1.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Yêu cầu môi trường

- Python 3.10+
- OpenCV
- NumPy

## Cài đặt

Từ thư mục dự án, thực hiện:

```bash
python -m venv .venv
```

Trên Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Trên macOS/Linux:

```bash
source .venv/bin/activate
```

Sau đó cài đặt các phụ thuộc:

```bash
pip install -r requirements.txt
```

## Chạy dự án

Đặt ảnh đầu vào có tên `anh.jpg` vào thư mục `data/`, sau đó chạy từ thư mục gốc của dự án:

```bash
python src/lab1.py
```

Khi cửa sổ "Anh goc" hiện ra, nhấn một phím bất kỳ để chương trình tiếp tục xử lý và lưu các kết quả.

## Kết quả đầu ra

Các kết quả xử lý được lưu trong thư mục `outputs/`:

| Tệp | Mô tả |
| --- | --- |
| `anh_moi.png` | Ảnh gốc được lưu lại ở định dạng PNG. |
| `gray.png` | Ảnh xám (1 kênh). |
| `hsv.png` | Ảnh trong không gian màu HSV. |
| `lab.png` | Ảnh trong không gian màu LAB. |
| `crop.png` | Vùng ảnh được cắt (300x300). |
| `resize.png` | Ảnh sau khi đổi kích thước về 300x300. |
| `ve_hinh.png` | Ảnh sau khi vẽ đường thẳng, hình chữ nhật, hình tròn và chèn chữ. |

## Ghi chú

- Ảnh `hsv.png` và `lab.png` có màu sắc "lạ" vì các kênh H/S/V hoặc L/a/b đang được hiển thị như kênh B/G/R. Đây là hiện tượng bình thường, không phải lỗi.
- `cv2.resize(img, (300, 300))` không giữ nguyên tỷ lệ khung hình nên ảnh kết quả bị co giãn.
- Việc cắt ảnh theo dạng `img[y1:y2, x1:x2]` (hàng trước, cột sau) khác với thứ tự tọa độ `(x, y)` khi vẽ hình.
- Các hàm vẽ (`line`, `rectangle`, `circle`, `putText`) thay đổi trực tiếp lên ảnh gốc `img`.
- `cv2.putText` chỉ hỗ trợ ký tự ASCII, nên chữ trên ảnh viết không dấu.
- Đường dẫn trong code được tính từ vị trí của `lab1.py`, nên có thể chạy từ bất kỳ thư mục nào.
- Cần có môi trường có giao diện đồ họa để `cv2.imshow` hoạt động.


