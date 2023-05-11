'''
시트 2와 같은 방법으로 구현한 DB 전송 코드

참고(시트): https://docs.google.com/spreadsheets/d/1HqJbM_TcvBodEGOaOuBdgZ0X3h86_WhdqoY1hccEutc/edit?usp=sharing
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time


#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('./firebase_json/lip-chat-firebase-adminsdk-xxjbl-0b990acfb6.json')
firebase_admin.initialize_app(cred,
                              {"databaseURL": 'https://lip-chat-default-rtdb.firebaseio.com/'})
# 유저 uid를 받아오기
name = 'dbtest'

# 연산 직전
cal_ing_text = 1
cal_ing_face = 1
ref = db.reference('cal_ing/'+name)
ref.update({'text': cal_ing_text,
            'face': cal_ing_face})

time.sleep(2) #연산 중

# 연산 후
timestr = time.strftime('%Y-%m-%d %H:%M:%S')
text = "안녕하세요?"
face_id = 0

cal_ing_text = 0
cal_ing_face = 0
ref = db.reference('result')
ref.push({'uid': name,
          'text': text,
          'face_id': face_id,
          'time': timestr})

ref = db.reference('cal_ing/'+name)
ref.update({'text': cal_ing_text,
            'face': cal_ing_face})




