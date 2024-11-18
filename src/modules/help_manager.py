import os

class HelpManager:

    def help_menu(self):
        print("\nHelp & Guide")
        print("1: View Command Help")
        print("2: Usage Examples")
        
        choice = input("Choose an option (1-2): ")
        
        if choice == "1":
            command = input("Enter command to view help: ")
            os.system(f"man {command}")
        elif choice == "2":
            print("Examples of usage:")
            print(" - Add a user: sudo useradd <username>")
            print(" - Install software: sudo apt install <package_name>")
            print(" - Update package list: sudo apt update")
            print(" - Upgrade installed packages: sudo apt upgrade")
            print(" - Remove a package: sudo apt remove <package_name>")
            print(" - Display disk usage: df -h")
            print(" - Display free memory: free -h")
            print(" - List files in directory: ls -l <directory>")
            print(" - Copy file: cp <source_file> <destination>")
            print(" - Move file: mv <source_file> <destination>")
            print(" - Delete file: rm <file_name>")
            print(" - Create a directory: mkdir <directory_name>")
            print(" - Change permissions: chmod <permissions> <file_name>")
            print(" - Change ownership: chown <user>:<group> <file_name>")
            print(" - Display network configuration: ifconfig")
            print(" - Ping a host: ping <hostname_or_ip>")
            print(" - Check system uptime: uptime")
        else:
            print("Invalid choice in Help & Guide.")
