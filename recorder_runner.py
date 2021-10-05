from recorders.mouse_recorder import MouseRecorder
import time

rec = MouseRecorder()
time.sleep(4)
rec.stop()
rec.print_mock_db()