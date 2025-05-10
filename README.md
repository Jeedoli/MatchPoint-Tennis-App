<div align="center">
  
  ![tennis-5264102_1280](https://github.com/OZ-Coding-School/oz_02_collabo-007/assets/27201254/e1c6ca5b-c6e3-40f9-8b08-981fb0ad6680)
  
 # 🎾 Alchemist 테니스 매칭 서비스

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
![DRF](https://img.shields.io/badge/djangorestframework-3.14-red.svg)
</div>

> 테니스 선수 매칭, 대회 관리 및 클럽 운영을 위한 종합 플랫폼

## 📋 프로젝트 개요

Alchemist 테니스 매칭 서비스는 테니스 선수들이 파트너를 찾고, 대회에 참가하며, 클럽 활동을 관리할 수 있는 종합 플랫폼입니다. 사용자는 자신의 실력 등급(티어)에 맞는 대회에 참가하거나, 클럽에 가입 신청을 할 수 있으며, 대회 참가 후 포인트를 획득해 랭킹에 반영됩니다.

### 주요 기능

- **사용자 관리**: 회원가입, 로그인, 프로필 관리
- **대회 관리**: 대회 생성, 조회, 신청, 결과 등록
- **클럽 시스템**: 클럽 생성, 가입 신청, 클럽별 팀 관리
- **매치 시스템**: 경기 일정 관리, 결과 등록, 포인트 계산
- **티어 및 포인트**: 사용자 실력 등급 관리, 포인트 적립 시스템
- **관리자 기능**: 사용자, 대회, 클럽, 매치 등 종합 관리

## 🛠️ 기술 스택

- **백엔드**: Python 3.12, Django 5.0, Django REST Framework 3.14
- **데이터베이스**: SQLite (개발), PostgreSQL (배포)
- **인증**: JWT (JSON Web Tokens)
- **의존성 관리**: Poetry
- **API 문서화**: Swagger, ReDoc

## 🗂️ 프로젝트 구조

```text
oz_02_collabo-007-BE/
├── config/                    # 프로젝트 설정 파일
│   ├── settings.py            # Django 설정
│   ├── urls.py                # 메인 URL 라우팅
│   └── wsgi.py                # 웹 서버 게이트웨이
├── core/                      # 프로젝트 공통 기능
│   ├── log_middleware.py      # 로깅 미들웨어
│   └── manager.py             # 커스텀 매니저
├── users/                     # 사용자 앱
│   ├── models.py              # 사용자 모델
│   ├── serializers.py         # 시리얼라이저
│   ├── urls.py                # URL 정의
│   └── views.py               # API 뷰
├── competition/               # 대회 관리 앱
├── club/                      # 클럽 관리 앱
├── match/                     # 매치 관리 앱
├── team/                      # 팀 관리 앱
├── point/                     # 포인트 시스템 앱
├── tier/                      # 티어(등급) 시스템 앱
├── applicant/                 # 지원자 관리 앱
├── applicant_info/            # 지원 정보 관리 앱
├── participant/               # 참가자 관리 앱
├── participant_info/          # 참가 정보 관리 앱
├── custom_admin/              # 관리자 커스텀 기능
├── image_url/                 # 이미지 관리
├── payments/                  # 결제 시스템
├── manage.py                  # Django 프로젝트 관리 스크립트
├── poetry.lock                # Poetry 의존성 락 파일
└── pyproject.toml             # 프로젝트 의존성 정의
```

## 🚀 시작하기

### 1. 환경 설정

#### Poetry 설치
```bash
# macOS
curl -sSL https://install.python-poetry.org | python3 -

# Windows
curl -sSL https://install.python-poetry.org | python -
```

#### 가상환경 활성화 및 패키지 설치
```bash
poetry shell
poetry update
```

### 2. 환경 변수 설정
```bash
cp env.sample .env
# .env 파일에 필요한 환경 변수를 설정합니다
```

### 3. 데이터베이스 설정
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. 서버 실행
```bash
python manage.py runserver
```

## 🔑 주요 API 엔드포인트

### 인증 API
- `api/v1/auth/signup/`: 회원가입
- `api/v1/auth/signin/`: 로그인
- `api/v1/auth/logout/`: 로그아웃
- `api/v1/auth/refresh/`: 액세스 토큰 갱신

### 사용자 API
- `api/v1/users/me/`: 내 정보 조회/수정
- `api/v1/users/{id}/`: 특정 사용자 정보 조회

### 대회 API
- `api/v1/competitions/`: 대회 목록 조회
- `api/v1/competitions/{id}/`: 대회 상세 조회
- `api/v1/competitions/{id}/apply/`: 대회 신청

### 클럽 API
- `api/v1/clubs/`: 클럽 목록 조회
- `api/v1/clubs/{id}/`: 클럽 상세 조회
- `api/v1/clubs/{id}/apply/`: 클럽 가입 신청

### 매치 API
- `api/v1/matches/`: 매치 목록 조회
- `api/v1/matches/{id}/`: 매치 상세 조회
- `api/v1/matches/{id}/result/`: 매치 결과 등록

### 포인트/티어 API
- `api/v1/points/rankings/`: 랭킹 조회
- `api/v1/tiers/`: 티어 목록 조회

## 🏗️ 아키텍처 및 설계 원칙

### Django MTV 패턴
- **Model**: 데이터베이스 스키마 정의
- **Template**: 프론트엔드와의 API 인터페이스
- **View**: 요청 처리 및 응답 반환

### RESTful API 설계
- 리소스 중심의 URL 설계
- HTTP 메서드를 통한 CRUD 작업
- 적절한 상태 코드 반환

### SOLID 원칙 적용
- **단일 책임 원칙 (SRP)**: 각 모델과 뷰는 단일 책임만 가집니다
- **개방-폐쇄 원칙 (OCP)**: 확장에 열려 있고 수정에는 닫혀 있습니다
- **리스코프 치환 원칙 (LSP)**: 상속받은 클래스는 기본 클래스를 대체할 수 있습니다
- **인터페이스 분리 원칙 (ISP)**: 클라이언트는 필요한 인터페이스만 사용합니다
- **의존성 역전 원칙 (DIP)**: 추상화에 의존하여 유연성을 확보합니다

## 🔒 인증 및 보안

- JWT 토큰 기반 인증
  - 액세스 토큰: API 요청 인증
  - 리프레시 토큰: 쿠키 기반 보안 저장
- 비밀번호 해시화 (Django 빌트인 암호화)
- CORS 설정으로 허용된 출처만 접근 가능

## 🧪 테스트 및 품질 관리

- 단위 테스트: 주요 모델 및 API 엔드포인트
- 통합 테스트: 사용자 시나리오 기반
- 코드 품질: flake8, black을 통한 코드 스타일 관리

## 📊 시스템 모니터링

- Django 로깅 시스템을 통한 에러 추적
- 사용자 활동 로그 기록 및 분석
- 성능 모니터링 및 병목 현상 식별

## 🌱 프로젝트 향후 계획

- 실시간 알림 시스템 (WebSocket)
- 머신러닝 기반 매치 추천 시스템
- 모바일 앱 지원을 위한 API 확장
- 결제 시스템 연동 강화
- 대회 실시간 중계 기능

## 👥 프로젝트 팀

- 백엔드 개발자: 5명
- UI/UX 디자이너: 2명
- 프론트엔드 개발자: 3명
- QA 엔지니어: 1명

## 📄 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.



