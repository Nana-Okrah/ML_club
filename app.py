#from flask import Flask, render_template, request, current_app as app
from pycoral.utils.dataset import read_label_file
import vision
import time

print('This is the "Scan and Shop" for ecommerce')
time.sleep(3)
print('position your item in the frame of the camera; having a plane background helps')
time.sleep(4)
print(' starting in 5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print("1")
time.sleep(1)
print('scaning begins')
time.sleep(.5)


classifier = vision.Classifier(vision.CLASSIFICATION_MODEL)
# Run a loop to get images and process them in real-time
for frame in vision.get_frames():
    classes = classifier.get_classes(frame)
    # Get list of all recognized objects in the frame
    label_id = classes[0].id# list of id
    score = classes[0].score# confidence score 
    labels = read_label_file(vision.CLASSIFICATION_LABELS)
    label = labels.get(label_id)# getting the labels id
    #print(label, score)
    
    kite ="https://www.amazon.com/gp/bestsellers/toys-and-games/1234183011"
    baseball="https://www.amazon.com/SKLZ-Reduced-Impact-Safety-Baseballs/dp/B003D6FEYA/ref=sr_1_3?dchild=1&keywords=baseball&qid=1623078332&s=toys-and-games&sr=1-3"
    ipod="https://www.bestbuy.com/site/searchpage.jsp?st=ipod+touch&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
    bathtowel="https://www.amazon.com/bath-towels/s?k=bath+towels"
    swimming_cap="https://www.walmart.com/browse/sports-outdoors/swim-caps/4125_4161_7400852_4861391"
    coffeemug="https://www.amazon.com/s?k=mug&ref=nb_sb_noss_1"
    c_mouse ="https://www.bestbuy.com/site/mice-keyboards/mice/pcmcat338200050008.c?id=pcmcat338200050008"
    water_bottle ="https://www.amazon.com/water-bottle/s?k=water+bottle" 
    bath_towel= "https://www.amazon.com/s?k=bath+towel&ref=nb_sb_noss_1"
    Basketball ="https://www.amazon.com/s?k=Basketball&ref=nb_sb_noss_2"
    running_shoes ="https://www.footlocker.com/category/sport/running/shoes.html"
    alt=" \n if link is not underlined or fully underlined, highlight the link, copy and paste into browser."
    
    if score >= float(0.60) and label == 'kite':
        print(kite + "/n" + alt)
        time.sleep(10)
    elif score >= float(0.60) and label == 'baseball':
        print(baseball + "/n" + alt )
        time.sleep(10)
    elif score >= float(0.6) and label =='coffee mug':
        print(coffeemug + "/n" + alt)
        time.sleep(10)
    elif score >= float(0.60) and label == 'ipod':
        print(ipod + "/n" + alt)
        time.sleep(10)
    elif score >= float(0.6) and label == 'mouse, computer mouse':
        print(c_mouse + "\n" + alt)
        time.sleep(10)
    elif score>= float(0.60) and label == 'water bottle':
        print(water_bottle + "\n" + alt)
        time.sleep(10)
    elif score >= float(0.6) and label == 'bath towel':
        print(bath_towel + "\n" + alt)
        time.sleep(10)
    elif score >= float(0.6) and label == 'basketball':
        print(Basketball)
        time.sleep(10)
    elif score >= float(0.6) and label == 'running shoes':
        print(running_shoes + "\n" + alt)
        time.sleep(10)
    
                        



