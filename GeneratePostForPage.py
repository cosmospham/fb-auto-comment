# -*- coding: utf-8 -*-
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
from time import sleep
import time
from random import randint
import sys, traceback

def spam():
    token = "EAACEdEose0cBADwSeMC3ZCLr7UMV9c6xWvXSfQHAkedsNIRVbVZBoTyiXncXgUke4d7repFvN7x67bTkDuWbbrsU8oomFspo8uPMyjITCjQwTF64nUPpKQABpPZBlslZA3cGkG6ZCX4WBZA6TJbsN9VbIgpm9QW1clZCFiMK8ZAMsbtwtb5cHrab" #Insert access token here.  
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
                    try:
                        print line
                        millis = int(round(time.time()))
                        print facebook.publish(cat = "feed", id = query, message = line+str(millis) )
                    except Exception, e:
                       print e
                    else:
                        pass
                    finally:
                        sleep(randint(30, 60))
                    
                    # sys.exit(0)
    else :
        print("No spam happening then.")

spam()

