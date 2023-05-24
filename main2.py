'''
시트 2와 같은 방법으로 구현한 DB 전송 코드 (서버에서 립리딩)

참고(시트): https://docs.google.com/spreadsheets/d/1HqJbM_TcvBodEGOaOuBdgZ0X3h86_WhdqoY1hccEutc/edit?usp=sharing
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time


#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('./firebase_json/newlipchat-firebase-adminsdk-qjh2u-086df0f3dd.json')
firebase_admin.initialize_app(cred,
                              {"databaseURL": 'https://newlipchat-default-rtdb.firebaseio.com/'})
# 유저 uid를 받아오기
name = 'dbtest'

# 연산 직전
cal_ing_text = 1
ref = db.reference('flag/'+name)
ref.update({'text': cal_ing_text}) # 텍스트 연산 중
face_id = db.reference('flag/'+name+'/current_face_id').get() #face_id 가져오기

time.sleep(2) #연산 중

# 연산 후
timestr = time.strftime('%Y-%m-%d %H:%M:%S')
text = "안녕하세요?"

cal_ing_text = 0
ref = db.reference('result')
ref.push({'uid': name,
          'text': text,
          'face_id': face_id,
          'time': timestr})

ref = db.reference('flag/'+name)
ref.update({'text': cal_ing_text}) #연산 종료 알림




