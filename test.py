import matplotlib.pyplot as plt
from skimage import color

# Đọc ảnh (Sử dụng 'r' để tránh lỗi path trên Windows)
test_image = plt.imread(r'C:\Users\Admin\Documents\Python\VA_T9557.JPG')

def show_image(image, title='Image', cmap_type='gray'):
    plt.figure(figsize=(8, 6)) # Thêm kích thước khung hình cho rõ nét
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Chuyển sang ảnh xám
gray_test_image = color.rgb2gray(test_image)

# Sử dụng hàm đã tạo để hiển thị
show_image(gray_test_image, "Anh xam sau khi chuyen doi")