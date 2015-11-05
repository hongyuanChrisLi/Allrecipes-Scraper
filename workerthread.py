import threading
from recipepage import RecipePage

class WorkerThread(threading.Thread):

    def __init__(self, queue):
        self.queue = queue
        threading.Thread.__init__ (self)

    def run(self, func):
        while True:
            func(self.queue)
