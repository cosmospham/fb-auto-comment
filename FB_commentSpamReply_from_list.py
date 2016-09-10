# -*- coding: utf-8 -*-
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
from time import sleep
import time
from random import randint

def spam():
    token = "EAACEdEose0cBAOq5obWKjR5oCcKOwcujHKIDSMnwAffWXsRUyMxP4FKZBTh9sufG63SkzsVUPYulpln4xJv6GWa7D9qx58PLhn6ZCvEfx40MixdlAdyU4WgZCuUuEmsiZAK5f1M0ZAwFipUqms8FnYpCWVHtYtVbOnNJs24a0sAZDZD" #Insert access token here.  
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)

    vid = "1038404499588346" # page id
    idlist = []
    fname = 'assets/list.txt'
    with open(fname) as f:
        content = f.readlines()
        for line in content:
            if (len(line.strip())):
                idlist.append(vid+'_'+line.strip())

    print("There are "+ str(len(idlist)) +" spammable posts.")

    char1 = raw_input("Do you want to spam? (y/n) ")
    count = 0
    if char1 == 'y':
        nos = input("Enter number of posts to be spammed with comments: ")
        mess = " your spammy x y z by list 111 "

        if nos <= len(idlist):
            for indid in (idlist[(len(idlist) - nos):]):
                query_comment = str(indid)+'/comments?fields=id&limit=10'
                r_comment = graph1.get(query_comment)
                idlist_comment = [x['id'] for x in r_comment['data']]

                for comment_id in idlist_comment:
                    try:
                        millis = int(round(time.time()))
                        res = facebook.publish(cat = "comments", id = comment_id, message = str(randint(1, 10000)) + (mess)+' - '+str(millis) ) #Comments on each post
                        count += 1
                        print res
                        print("Notification number: " + str(count) + " on www.facebook.com/" + str(indid).split('_')[0] 
                          + "/posts/" + str(indid).split('_')[1]) + '?comment_id=' + str(res['id'].split('_')[1])
                    except Exception, e:
                        print e
                    else:
                        pass
                    finally:
                        sleep(randint(5, 10))
        else: 
          print("Not that many spammable posts available. No spam happening.")
    else :
      print("No spam happening then.")

spam()

