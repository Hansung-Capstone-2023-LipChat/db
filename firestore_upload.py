'''
저장된 이미지를 firestore에 올리는 코드
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 파이어베이스 서비스 계정 키 파일 경로
cred = credentials.Certificate('firebase_json/iotcapston-firebase-adminsdk-t5vwf-5c4967f7bf.json')

# 파이어베이스 앱 초기화
firebase_admin.initialize_app(cred)

# 파이어스토어 클라이언트 생성
db = firestore.client()

# 이미지 업로드 함수
def upload_image(image_path, collection_name, document_name):
    # 이미지 파일 열기
    with open(image_path, 'rb') as image_file:
        # 이미지 데이터 읽기
        image_data = image_file.read()

    # 이미지 업로드
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.set({
        'image_data': image_data
    })
    print('이미지가 성공적으로 업로드되었습니다.')

faceid = "ex_face1"

# 이미지 업로드 호출
upload_image('images/ex_face1.jpg', 'face_img', faceid)
