# modules/system_monitor.py
import psutil

class SystemMonitor:

# Hiển thị thông tin hệ thống (CPU, RAM, Disk)
 def display_system_info():
     try:
         print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
         print("RAM Usage:", psutil.virtual_memory().percent, "%")
         print("Disk Usage:", psutil.disk_usage('/').percent, "%")
     except Exception as e:
         print(f"Error: {e}")
