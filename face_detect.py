'''
시트 2와 같은 방법으로 구현한 DB 전송 코드 (Rasberry에서 얼굴 인식)

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

if db.reference('flag/'+name+'/camera_on').get() == "1":
    # 연산 직전
    cal_ing_face = "1"
    ref = db.reference('flag/'+name)
    ref.update({'face': cal_ing_face}) # 얼굴 인식 중

    time.sleep(2) #연산 중

    # 연산 후
    face_id = "face1"

    cal_ing_text = "0"
    ref = db.reference('flag/'+name)
    ref.update({'face': cal_ing_text, 'current_face_id': face_id}) #연산 종료 알림, 얼굴 인식 결과 업데이트