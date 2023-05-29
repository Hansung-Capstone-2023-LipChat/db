'''
firestore에서 저장된 이미지를 읽어오는 코드.
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import io
from PIL import Image

# 파이어베이스 서비스 계정 키 파일 경로
cred = credentials.Certificate('firebase_json/iotcapston-firebase-adminsdk-t5vwf-5c4967f7bf.json')

# 파이어베이스 앱 초기화
firebase_admin.initialize_app(cred)

# 파이어스토어 클라이언트 생성
db = firestore.client()

# 이미지 읽기 함수
def read_image(collection_name, document_name):
    # 문서 참조 가져오기
    doc_ref = db.collection(collection_name).document(document_name)
    doc = doc_ref.get()

    # 문서에서 이미지 데이터 읽기
    image_data = doc.to_dict().get('image_data')

    if image_data:
        # 이미지 데이터를 바이트 스트림으로 변환
        image_stream = io.BytesIO(image_data)

        # 이미지 열기
        image = Image.open(image_stream)

        # 이미지 보여주기 (예시로 출력)
        image.show()
    else:
        print('이미지 데이터가 없습니다.')

faceid = "ex_face1"

# 이미지 읽기 호출
read_image('face_img', faceid)
