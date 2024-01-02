import threading

lock_obj = threading.Lock()

print('Acquaire 1st time')
lock_obj.acquire()

print('Acquaire 2nd time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()

