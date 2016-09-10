# -*- coding: utf-8 -*-
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
from time import sleep
import time
from random import randint

def spam():
    token = "token_" #Insert access token here.  
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    vid = "page_id" # page id
    query = str(vid) + "/posts?fields=id&limit=100"
    r = graph1.get(query)
    
    
    
    idlist = [x['id'] for x in r['data']]
    # idlist.reverse()
    print("There are "+ str(len(idlist)) +" spammable posts.")

    char1 = raw_input("Do you want to spam? (y/n) ")
    count = 0
    if char1 == 'y':
        nos = input("Enter number of posts to be spammed with comments: ")
        mess = " your spammy message "
        # mess = raw_input("Test comment")
        if nos <= len(idlist):
            for indid in (idlist[(len(idlist) - nos):]):
                millis = int(round(time.time()))
                print facebook.publish(cat = "comments", id = indid, message = str(randint(1, 10000)) + (mess)+' - '+str(millis) ) #Comments on each post
                # facebook.publish(cat = "likes", id = indid) #Likes each post
                count += 1
                print("Notification number: " + str(count) + " on www.facebook.com/" + str(indid).split('_')[0] 
                  + "/posts/" + str(indid).split('_')[1])
                sleep(randint(5,10))
        else: 
          print("Not that many spammable posts available. No spam happening.")
    else :
      print("No spam happening then.")

spam()

