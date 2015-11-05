import threading

class FileProcess(threading.Thread):

    def __init__(self, queue):
        self.queue = queue
        threading.Thread.__init__ (self)

    def write(self, path, data):
        print 'Test'