import subprocess
import re

class NetworkManager:

    def is_valid_ip(self, ip):
        """Kiểm tra tính hợp lệ của một địa chỉ IP."""
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return pattern.match(ip) is not None

    def display_network_info(self):
        """Hiển thị thông tin mạng."""
        subprocess.run(["ip", "a"])

    def ping_test(self, target):
        """Thực hiện kiểm tra ping tới một mục tiêu."""
        subprocess.run(["ping", "-c", "4", target])

    def network_management_menu(self):
        """Hiển thị menu quản lý mạng."""
        print("\nNetwork Management")
        print("1: Display Network Info")
        print("2: Ping Test")
        
        choice = input("Choose an option (1-2): ")
        
        if choice == "1":
            self.display_network_info()
        
        elif choice == "2":
            target = input("Enter IP address or domain to ping: ")
            self.ping_test(target)
        
        else:
            print("Invalid choice in Network Management.")
