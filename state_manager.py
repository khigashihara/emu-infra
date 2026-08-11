#!/bin/python3

class running:
    def __init__(self):
        print("start")

    def status(self):
        return self.__class__.__name__

    def start(self):
        print("it had already started.")
        return self

    def stop(self):
        return stopped()

class stopped:
    def __init__(self):
        print("stop")

    def status(self):
        return self.__class__.__name__

    def start(self):
        return running()

    def stop(self):
        print("it had already stopped.")
        return self


class state:
    def __init__(self,status="stopped"):
        self.status = status
    def now(self):
        return self.status

    def change_status(self,status):
        if self.status != status:
            return state(status)


