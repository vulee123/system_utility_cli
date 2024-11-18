import os

class UserManager:

 def user_management_menu():
     print("\nUser Management")
     print("1: Add User")
     print("2: Modify User")
     print("3: Delete User")
     print("4: Check User Info")
     print("5: Change User Password")
    
     choice = input("Choose an option (1-5): ")
    
     if choice == "1":
         username = input("Enter username to add: ")
         result = os.system(f"sudo useradd {username}")
         if result == 0:
             print(f"User '{username}' has been added successfully.")
         else:
             print(f"Failed to add user '{username}'.")

     elif choice == "2":
         username = input("Enter username to modify: ")
         result = os.system(f"sudo usermod {username}")
         if result == 0:
             print(f"User '{username}' has been modified successfully.")
         else:
             print(f"Failed to modify user '{username}'.")

     elif choice == "3":
         username = input("Enter username to delete: ")
         result = os.system(f"sudo userdel {username}")
         if result == 0:
             print(f"User '{username}' has been deleted successfully.")
         else:
             print(f"Failed to delete user '{username}'.")

     elif choice == "4":
         username = input("Enter username to check info: ")
         result = os.system(f"id {username}")
         if result == 0:
             print(f"Information for user '{username}' displayed successfully.")
         else:
             print(f"Failed to retrieve information for user '{username}'.")

     elif choice == "5":
         username = input("Enter username to change password: ")
        
         # Yêu cầu nhập mật khẩu cũ để xác thực
         print("Please authenticate by entering the current password.")
         auth_result = os.system(f"sudo -k passwd --status {username}")
        
         if auth_result == 0:
             # Nếu xác thực thành công, cho phép đổi mật khẩu
             print("Authentication successful. You can now change the password.")
             result = os.system(f"sudo passwd {username}")
             if result == 0:
                 print(f"Password for user '{username}' has been changed successfully.")
             else:
                 print(f"Failed to change password for user '{username}'.")
         else:
             print("Authentication failed. Incorrect current password.")

     else:
         print("Invalid choice in User Management.")
