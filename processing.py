import threading
import time
import sys


class ProcessThread:
    def __init__(self):
        self.work_ended = False
        self.thread = None

    def process(self):
        while not self.work_ended:
            self.flush("|")
            self.flush("/")
            self.flush("-")
            self.flush("\\")
        sys.stdout.write("\b" + "done\n")
        sys.stdout.flush()

    def flush(self, char):
        sys.stdout.write("\b" + char)
        sys.stdout.flush()
        time.sleep(0.12)

    def start(self):
        self.redo()
        self.thread = threading.Thread(target=self.process)
        self.thread.start()

    def done(self):
        self.work_ended = True
        self.thread.join()

    def redo(self):
        self.work_ended = False


if __name__ == "__main__":
    test = ProcessThread()
    test.start()
    time.sleep(3)
    test.done()

