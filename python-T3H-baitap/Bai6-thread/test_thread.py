from _thread import start_new_thread

num_threads = 0
def heron(a):
    global num_threads
    num_threads += 1

    # code has been left out, see above
    num_threads -= 1
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))

while num_threads > 0:
    pass