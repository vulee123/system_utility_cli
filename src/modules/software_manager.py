# modules/software_manager.py

import os

class SoftwareManager:

    def software_management_menu(self):
        print("\nSoftware Management")
        print("1: Install Software")
        print("2: Remove Software")
        print("3: Update Software")
        print("4: Check Software Version")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            package = input("Enter package name to install: ")
            os.system(f"sudo apt install {package}")
            
        elif choice == "2":
            package = input("Enter package name to remove: ")
            os.system(f"sudo apt remove {package}")
            
        elif choice == "3":
            package = input("Enter package name to update: ")
            os.system(f"sudo apt update && sudo apt install --only-upgrade {package}")
            
        elif choice == "4":
            package = input("Enter package name to check version: ")
            os.system(f"dpkg -s {package} | grep Version")
            
        else:
            print("Invalid choice in Software Management.")
