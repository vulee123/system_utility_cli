# modules/system_cleaner.py
import os

class SystemCleaner:

    # Dọn dẹp tệp tạm trong thư mục /tmp
    def clean_temp_files(self, directory="/tmp"):
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Error: {e}")

    # Dọn dẹp tệp log trong thư mục /var/log
    def clean_log_files(self, directory="/var/log"):
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith(".log") or file.endswith(".old"):
                        os.remove(file_path)
                        print(f"Deleted log file {file_path}")
        except Exception as e:
            print(f"Error: {e}")

    # Dọn dẹp cache ứng dụng
    def clean_cache(self, directory="~/.cache"):
        try:
            directory = os.path.expanduser(directory)  # Mở rộng dấu ~ thành đường dẫn đầy đủ
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted cache file {file_path}")
        except Exception as e:
            print(f"Error: {e}")

    # Thực hiện dọn dẹp hệ thống
    def clean_system(self):
        print("Cleaning temporary files...")
        self.clean_temp_files()

        print("Cleaning log files...")
        self.clean_log_files()

        print("Cleaning cache files...")
        self.clean_cache()

        print("System cleaning completed.")
