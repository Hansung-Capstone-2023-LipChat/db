from google.cloud import storage
from google.oauth2 import service_account

# 서비스 계정 인증 정보가 담긴 JSON 파일 경로
KEY_PATH = "./config/newlipchat-257573dc6071.json"

# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 구글 스토리지 클라이언트 객체 생성
client = storage.Client(credentials = credentials, project = credentials.project_id)

# 버킷 이름
bucket_name = "lip_chat_video_data"
# 블랍 이름
blob_name = "data.mp4"
# 적재할 파일 경로
file_path = "./video/1.mp4"

# 버킷 선택
bucket = client.get_bucket(bucket_name)
# 블랍 객체 생성
blob = bucket.blob(blob_name)
# 파일 업로드
blob.upload_from_filename(file_path)
# 버킷에 업로드된 객체의 공개 URL
# blob.public_url