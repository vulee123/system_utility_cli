**System Utility CLI
System Utility CLI là một công cụ dòng lệnh (CLI) mạnh mẽ để quản lý tài nguyên hệ thống, giúp người dùng thực hiện các tác vụ phổ biến như giám sát hệ thống, quản lý tệp, dọn dẹp hệ thống, quản lý mạng, và nhiều hơn nữa.

Các tính năng
1.File Manager

-Quản lý tệp và thư mục (tạo, xóa, sao chép, di chuyển).
-Chức năng tìm kiếm tệp.
2.System Monitor

-Giám sát CPU, RAM, và dung lượng ổ cứng.
-Cung cấp báo cáo tình trạng hệ thống.
3.Download Manager

-Quản lý và tăng tốc tải xuống.
-Hỗ trợ tạm dừng và tiếp tục tải.
4.System Cleaner

-Dọn dẹp tệp tạm thời, tệp rác.
-Tăng hiệu suất hệ thống.
5.User Manager

-Quản lý người dùng (tạo, sửa, xóa).
-Kiểm tra quyền truy cập.
6.Software Manager

-Cài đặt, gỡ cài đặt phần mềm.
-Kiểm tra các phiên bản đã cài đặt.
7.Help Manager

-Cung cấp hướng dẫn chi tiết cho từng chức năng.
-Trợ giúp người dùng giải quyết lỗi thường gặp.
8.Network Manager

-Quản lý kết nối mạng.
-Kiểm tra tốc độ mạng và cấu hình mạng.
## **CÁCH SỬ DỤNG**
Chạy công cụ từ dòng lệnh:
bash
Sao chép mã
cd system_utility_cli 
python3 src/main.py
Cách kiểm thử
1. Chạy kiểm thử với unittest
System Utility CLI đi kèm các file kiểm thử được xây dựng bằng unittest. Để chạy tất cả kiểm thử:

bash
Sao chép mã
python3 -m unittest discover -s tests -p "test_*.py"
2. Chạy kiểm thử với pytest
Bạn cũng có thể sử dụng pytest để kiểm thử:

bash
Sao chép mã
pytest tests/
Lưu ý:
Đảm bảo thêm thư mục src vào PYTHONPATH nếu cần:
bash
Sao chép mã
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
Hoặc chỉnh sửa file pytest.ini để tự động nhận diện src:
ini
Sao chép mã
[pytest]
testpaths = tests
pythonpath = src
3. Kiểm thử từng module
Bạn có thể kiểm thử một module cụ thể, ví dụ:

bash
Sao chép mã
pytest tests/test_file_manager.py
