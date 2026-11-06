from flask import Flask,render_template,redirect,send_file
import os
import random
import pickle
videos=[]
number_of_video=0
ws=Flask(__name__)
#Start , DataBase Creator=========================================
if os.path.isfile('VideoAddress.db'):
    address_config=open('address_config.txt','r')
    folder_path=address_config.read()
    video_address=open('VideoAddress.db','rb')
    videos=pickle.loads(video_address.read())
    number_of_video=len(videos)
else:
    address_config=open('address_config.txt','r')
    folder_path=address_config.read()
    address_config.close()
    videos=os.listdir(folder_path)
    number_of_video=len(videos)
    video_address=open('VideoAddress.db','wb')
    video_address.write(pickle.dumps(videos))
    video_address.close
@ws.route("/")
def index():
    return redirect("/player")
@ws.route("/<path:url>")
def video(url=""):
    return send_file(os.path.join(folder_path,url))
@ws.route("/player")
def randomplay():
    return render_template('index.html',url=videos[random.randrange(0,number_of_video+1)])