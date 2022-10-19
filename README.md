
## 패키지 설치
pipenv install


## Server 실행 방법
APP_ENV=dev uvicorn app.main:app --reload


## Migration 방법
1) Model 변경 부분에 대한 version 자동 생성
APP_ENV=dev alembic revision --autogenerate -m "Init Test DB"

2) 생성된 version을 DB에 마이그레이션 실행
!! /migrations/versions 위치에 생성된 파일의 내용을 확인 후 마이그레이션 진행. 누락된 경우가 있을 수 있음 !!
APP_ENV=dev alembic upgrade head
APP_ENV=dev alembic downgrade head


## 구현내용
1) 유저
   1) 회원가입
      1) 회원가입시 올바른 이메일인지 체크한다
      2) 비밀번호는 Hashing 하여 저장한다
   2) 로그인
      1) 로그인 시 Access Token을 발행하고 Header Cookie에 저장한다
      2) Token 기한은 1일이며 기한이 지났을 때는 다시 로그인 해야 한다
      
2) 가계부(관련된 모든 요청은 로그인된 상태이어야 한다, 로그인한 유저와 관련된 정보들만 노출한다)
   1) CRUD(로그인한 유저가 작성한 가계부 내역만 조회, 수정, 삭제 가능하다)
   
3) 도커
   1) docker-compose.yml 에서 DockerFile을 참고하여 이미지를 빌드하고 컨테이너에 이미지를 올린다.
4) 테스트
   1) cd payhere_ass_back
   2) pytest