import threading

class ThrTest:

    class TestThread(threading.Thread):

        def __init__(self, num):
            self.num = num
            threading.Thread.__init__ (self)

        def run(self):
            print 'Test ' + str(self.num)

        def getName(self):
            return self.num

    def testing(self):
        threads_array = []
        for i in xrange(10):
            threads_array.append(ThrTest.TestThread(i))
            threads_array[i].start()
            print threading.enumerate()
        print threading.enumerate()

test = ThrTest()
test.testing()