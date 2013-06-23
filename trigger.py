#!/usr/bin/python

import pyinotify

class NotifierCustom (pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "CREATED HERE"
    def process_IN_MOVED_FROM(self, event):
        print "MOVED FROM"
    def process_IN_MOVE_SELF(self, event):
        print "MOVED INSIDE"
    def process_IN_MOVED_TO(self, event):
        print "MOVED TO"
 


def main():
    watchManager = pyinotify.WatchManager()
    watchManager.add_watch('/home/dhamodaran/Desktop/Python/SuperChopper/Images', pyinotify.ALL_EVENTS, rec=True)
    notifierCustomObject = NotifierCustom()
    notifier = pyinotify.Notifier(watchManager, notifierCustomObject)
    notifier.loop()

if __name__ == '__main__':
    main()




