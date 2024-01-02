import threading

lock_obj = threading.Lock()

# print('Acquaired 1st time')
# lock_obj.acquire()
#
# print('Acquaired 2nd time')
# lock_obj.acquire()
#
# print('Releasing')
# lock_obj.release()

def reentrance():
    print('start')
    lock_obj.acquire()
    print('Acquaired')
    reentrance()

reentrance()