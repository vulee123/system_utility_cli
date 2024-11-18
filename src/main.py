# main.py

from modules import file_manager, system_monitor, download_manager, system_cleaner
from modules import user_manager, software_manager, help_manager, network_manager

def show_menu():
    print("\nSystem Utility CLI")
    print("1. File Manager")
    print("2. System Monitor")
    print("3. Download Manager")
    print("4. System Cleaner")
    print("5. User Management")
    print("6. Software Management")
    print("7. Help & Guide")
    print("8. Network Management")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select a function (1-9): ")

        if choice == "1":
            # Giữ lại các chức năng Quản lý Tệp tin
            print("\nFile Manager:")
            print("1: List files")
            print("2: Copy file")
            print("3: Move file")
            print("4: Delete file")
            file_choice = input("Choose an option (1-4): ")

            if file_choice == "1":
                directory = input("Enter directory path: ")
                file_manager.list_files(directory)
            elif file_choice == "2":
                src = input("Source file path: ")
                dst = input("Destination path: ")
                file_manager.copy_file(src, dst)
            elif file_choice == "3":
                src = input("Source file path: ")
                dst = input("Destination path: ")
                file_manager.move_file(src, dst)
            elif file_choice == "4":
                file = input("File path to delete: ")
                file_manager.delete_file(file)
            else:
                print("Invalid choice for File Manager.")

        elif choice == "2":
            system_monitor.display_system_info()

        elif choice == "3":
            url = input("Enter the URL of the file to download: ")
            destination = input("Enter the destination path to save the file: ")
            download_manager.download_file(url, destination)

        elif choice == "4":
            system_cleaner.clean_system()

        elif choice == "5":
            user_manager.user_management_menu()

        elif choice == "6":
            software_manager.software_management_menu()

        elif choice == "7":
            help_manager.help_menu()

        elif choice == "8":
            network_manager.network_management_menu()

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 9.")

if __name__ == "__main__":
    main()
