import unittest
from src.modules.system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def test_cpu_usage(self):
        # Thêm logic kiểm thử cụ thể tại đây
        self.assertGreater(90, 50)  # Replace with actual test logic

if __name__ == "__main__":
    unittest.main()
