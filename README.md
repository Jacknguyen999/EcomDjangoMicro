# eCommerce Microservices - Hướng Dẫn Cài Đặt

## 🚀 Giới thiệu
Dự án eCommerce Microservices sử dụng kiến trúc microservices, gồm các service:
- **Customer Service** (MySQL)
- **Item Service** (MongoDB)
- **Cart, Order, Shipping, Paying Services** (PostgreSQL)
- **Tích hợp Cloudinary** để lưu trữ hình ảnh

## 🛠 Yêu Cầu
Trước khi chạy dự án, hãy đảm bảo bạn đã cài đặt:
- **Docker**: [Hướng dẫn cài đặt Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Hướng dẫn cài đặt Docker Compose](https://docs.docker.com/compose/install/)

## 📌 Tạo File `.env`
Bạn cần tạo file `.env` trong thư mục gốc của dự án với nội dung sau:

```ini
# MySQL Configuration
MYSQL_ROOT_PASSWORD=
MYSQL_USER=
MYSQL_PASSWORD=

# PostgreSQL Configuration
POSTGRES_USER=
POSTGRES_PASSWORD=

# MongoDB Configuration
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=
MONGO_HOST=
MONGO_DB_NAME=
# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

## 🚀 Khởi Chạy Dịch Vụ
1. **Tạo file `.env`** nếu chưa có:
   ```sh
   touch .env
   ```
2. **Sao chép nội dung trên vào file `.env`**
3. **Xây dựng và chạy Docker Compose**
   ```sh
   docker-compose up --build
   ```
4. **Kiểm tra xem các container đã chạy thành công**
   ```sh
   docker ps
   ```
