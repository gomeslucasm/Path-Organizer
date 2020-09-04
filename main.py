import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from organize import Organize_dir
from pathlib import Path
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
from getopt import getopt
import sys

# cmd inputs
argv = sys.argv[1:]

# get cmd options
opts, args = getopt(argv,[],['path=','exlude=','type='])

exc_type = []
inc_type = []

for opt,arg in opts:
    if '--path' in opt:
        watchDirectory_input = Path.home() / arg
        watchDirectory = str( Path.home() / arg)
    if '--exclude' in opt:
        exc_type.append(arg)
    if '--type' in opt:
        inc_type.append(arg)


Organize_dir(watchDirectory_input,inc_type,exc_type) 


class OnMyWatch: 
    # Set the directory on watch 
    def __init__(self): 
        self.observer = Observer() 
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(1) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
  
class Handler(FileSystemEventHandler): 
  
    @staticmethod
    def on_any_event(event): 
        try:
            Organize_dir(watchDirectory_input,inc_type,exc_type) 
        except:
            print('Não deu ')

if __name__ == '__main__': 
    watch = OnMyWatch() 
    watch.run() 
