import os
import base64
import requests
from tqdm import tqdm

class DownloadManager:

    def download_file(self, url, destination):
        try:
            # Kiểm tra xem URL có phải là hình ảnh mã hóa Base64 không
            if url.startswith("data:image"):
                # Lấy dữ liệu Base64 từ URL
                base64_data = url.split(",")[1]  # Lấy phần dữ liệu sau 'base64,'
                img_data = base64.b64decode(base64_data)

                # Ghi dữ liệu ảnh đã giải mã vào tệp đích
                with open(destination, 'wb') as file:
                    file.write(img_data)
                print(f"Đã lưu hình ảnh vào {destination}")
            
            else:
                # Xử lý tải xuống từ URL thông thường
                response = requests.get(url, stream=True)
                response.raise_for_status()  # Kiểm tra lỗi trong yêu cầu

                # Kiểm tra xem URL có phải là hình ảnh không dựa trên Content-Type
                content_type = response.headers.get('Content-Type')
                if 'image' not in content_type:
                    print(f"Cảnh báo: URL này không phải là hình ảnh. Content-Type: {content_type}")
                    return

                # Đặt tên tệp đích từ URL nếu không chỉ định sẵn
                if not destination:
                    destination = url.split("/")[-1]

                # Ghi dữ liệu ảnh vào tệp với tiến trình tải xuống
                with open(destination, 'wb') as file:
                    total_size = int(response.headers.get('Content-Length', 0))
                    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            progress_bar.update(len(chunk))

                    progress_bar.close()
                    print(f"Tải xuống hoàn tất: {destination}")

        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi tải xuống: {e}")
