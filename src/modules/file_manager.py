# modules/file_manager.py
import os
import shutil

class FileManager:

    # Liệt kê các tệp trong thư mục
    def list_files(self, directory):
        try:
            if os.path.exists(directory):
                for filename in os.listdir(directory):
                    print(filename)
            else:
                print(f"The directory {directory} does not exist.")
        except Exception as e:
            print(f"Error: {e}")

    # Sao chép tệp từ nguồn đến đích
    def copy_file(self, source, destination):
        try:
            shutil.copy(source, destination)
            print(f"Copied {source} to {destination}")
        except Exception as e:
            print(f"Error: {e}")

    # Di chuyển tệp từ nguồn đến đích
    def move_file(self, source, destination):
        try:
            shutil.move(source, destination)
            print(f"Moved {source} to {destination}")
        except Exception as e:
            print(f"Error: {e}")

    # Xóa tệp
    def delete_file(self, filename):
        try:
            os.remove(filename)
            print(f"Deleted {filename}")
        except Exception as e:
            print(f"Error: {e}")
