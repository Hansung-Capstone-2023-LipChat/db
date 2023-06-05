'''
앱에서 성공한 형태로 디비 올려주는 코드
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate('./firebase_json/newlipchat-firebase-adminsdk-qjh2u-086df0f3dd.json')
firebase_admin.initialize_app(cred,
                              {"databaseURL": 'https://newlipchat-default-rtdb.firebaseio.com/'})

# 유저 uid를 받아오기
name = 'dbtest'
# 연산 직전
cal_ing_text = "1"
ref = db.reference('flag/'+name)
ref.update({'text': cal_ing_text}) # 텍스트 연산 중
face_id = db.reference('flag/'+name+'/current_face_id').get() #face_id 가져오기

time.sleep(2) #연산 중

# 연산 후
text = "안녕하세요?"

cal_ing_text = "0"
ref = db.reference('result/'+face_id+'/Result')
ref.update({"text": text})

ref = db.reference('flag/'+name)
ref.update({'text': cal_ing_text}) #연산 종료 알림
