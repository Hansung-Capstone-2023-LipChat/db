'''
flag/uid/camera_on 값을 1로 해주는 테스트용 코드
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time


#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('./firebase_json/newlipchat-firebase-adminsdk-qjh2u-086df0f3dd.json')
firebase_admin.initialize_app(cred,
                              {"databaseURL": 'https://newlipchat-default-rtdb.firebaseio.com/'})
name = 'dbtest'

# 연산 직전
cal_ing_text = 1
ref = db.reference('flag/'+name)
ref.update({'camera_on': 1})
