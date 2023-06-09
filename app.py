from flask import Flask, request,render_template
from datetime import date, datetime
import mysql.connector

sql = "INSERT INTO tblhr_candidate_meetings (user_id, username, date,sign_in_time, sign_out_time, video_cam_on, video_cam_off,mic_on, mic_off, screen_share_on, screen_share_off) VALUES (%s, %s, %s,%s, %s,%s,%s, %s,%s, %s, %s )"

class MeetUser:
  def __init__(self, userid="", username="", signout="", videoon=[], videooff=[], micon=[], micoff=[], screenon=[], screenoff=[]):
    self.userid = userid
    self.username = username
    self.date = date.today().strftime("%d/%m/%Y")
    self.signin = datetime.now().strftime("%H:%M:%S")
    self.signout = signout
    self.videoon = videoon
    self.videooff = videooff
    self.micon = micon
    self.micoff = micoff
    self.screenon = screenon
    self.screenoff = screenoff

UserList =[]

app = Flask(__name__)


# load the front-end
@app.route('/')
def home():
  return render_template('index.html')


##### Handling Post Requests
@app.route('/meet-start', methods=['POST'])
def meet_on():
  if request.method == 'POST':
    data = request.get_json()
    if len(UserList):
      for user in UserList:
        if user.username == data['displayName']:
          break
        UserList.append(MeetUser(data['roomName'], data['displayName']))
    else:
        UserList.append(MeetUser(data['roomName'], data['displayName']))


    return "MESSAGE RECEIVED: Meeting Started "

@app.route('/meet-end', methods=['POST'])
def meet_off():
  if request.method == 'POST':
    data = request.get_json()

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shruti@lenovo",
    database="cbdns"
    )
    mycursor = mydb.cursor()
    for user in UserList:
      if user.userid == data['roomName']:
        user.signout = datetime.now().strftime("%H:%M:%S")
      videoon = ' '.join(user.videoon)
      videooff = ' '.join(user.videooff)
      micon = ' '.join(user.micon)
      micoff = ' '.join(user.micoff)
      screenon = ' '.join(user.screenon)
      screenoff = ' '.join(user.screenoff)

      val = (user.userid, user.username, user.date, user.signin, user.signout, videoon, videooff, micon, micoff, screenon, screenoff)
      mycursor.execute(sql, val)
    
    mydb.commit()
    return "MESSAGE RECEIVED: Meeting Ended "

@app.route('/video-on', methods=['POST'])
def vid_on():
  if request.method == 'POST':    
    data = request.get_json()
    
    for user in UserList:
      if user.userid == data['roomName']:
        user.videoon.append(datetime.now().strftime("%H:%M:%S"))
        break
    return "MESSAGE RECEIVED: Video Switched on"

@app.route('/video-off', methods=['POST'])
def vid_off():
  if request.method == 'POST':
    
    data = request.get_json()
    for user in UserList:
      if user.userid == data['roomName']:
        user.videooff.append(datetime.now().strftime("%H:%M:%S"))
        break

    return "MESSAGE RECEIVED: Video Switched Off"


@app.route('/audio-on', methods=['POST'])
def mic_on():
  if request.method == 'POST':
    
    data = request.get_json()
    for user in UserList:
      if user.userid == data['roomName']:
        user.micon.append(datetime.now().strftime("%H:%M:%S"))
        break
    

    return "MESSAGE RECEIVED: Audio Switched On"

@app.route('/audio-off', methods=['POST'])
def mic_off():
  if request.method == 'POST':
    
    data = request.get_json()
    for user in UserList:
      if user.userid == data['roomName']:
        user.micoff.append(datetime.now().strftime("%H:%M:%S"))
        break

    return "MESSAGE RECEIVED: Audio Switched Off"

@app.route('/screen-on', methods=['POST'])
def screen_share_on():
  if request.method =='POST':
    
    data = request.get_json()
  
    for user in UserList:
      if user.userid == data['roomName']:
        user.screenon.append(datetime.now().strftime("%H:%M:%S"))
        break
    

    return "MESSAGE RECEIVED: screen share Switched on"

@app.route('/screen-off', methods=['POST'])
def screen_share_off():
  if request.method =='POST':
    
    data = request.get_json()

    for user in UserList:
      if user.userid == data['roomName']:
        user.screenoff.append(datetime.now().strftime("%H:%M:%S"))
        break

    return "MESSAGE RECEIVED: screen shared switched off"



app.run(port=5500, debug =True)