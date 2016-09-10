# -*- coding: utf-8 -*-
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
from time import sleep
import time
from random import randint
import sys, traceback

def spam():
    token = "EAACEdEose0cBAEdGMv3RHKunWMnPxm1dLfRl3bqdXDYnZBHbDkUhM4DhRuumfaQzHheDINMZAsgCZC3ZAR4ZC7uJ9WyWLa7PpNJboo8ln3vsS1rHqIshPhloJ9YCzv3KbCZBZAVmzMLowokOF9XrkdlIr2HzIKo6B9wtKXLTpZAzlRWwgJZBmuigH" #Insert access token here.  
    facebook = fb.graph.api(token)
    # graph1 = GraphAPI(token)

    vid = "1038404499588346" # page id
    query = str(vid) 

    char1 = 'y' # raw_input("Do you want to spam? (y/n) ")
    fname = 'assets/string.txt'
    if char1 == 'y':
        with open(fname) as f:
            content = f.readlines()
            for line in content:
                if (len(line.strip())):
                    print line
                    millis = int(round(time.time()))
                    print facebook.publish(cat = "feed", id = query, message = line+str(millis) ) #Comments on each post
                    sleep(randint(50, 100))
                    # sys.exit(0)
    else :
        print("No spam happening then.")

spam()

