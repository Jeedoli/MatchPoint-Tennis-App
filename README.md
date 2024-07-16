<div align="center">
  
  ![tennis-5264102_1280](https://github.com/OZ-Coding-School/oz_02_collabo-007/assets/27201254/e1c6ca5b-c6e3-40f9-8b08-981fb0ad6680)
  
  <div>
    <img src="https://img.shields.io/badge/-Next_JS-black?style=for-the-badge&logoColor=white&logo=nextdotjs&color=000000" alt="nextdotjs" />
    <img src="https://img.shields.io/badge/-TypeScript-black?style=for-the-badge&logoColor=white&logo=typescript&color=3178C6" alt="typescript" />
    <img src="https://img.shields.io/badge/-Tailwind_CSS-black?style=for-the-badge&logoColor=white&logo=tailwindcss&color=06B6D4" alt="tailwindcss" />
  </div>

  <h3 align="center">알케미스트 - 테니스 대회 앱</h3>

   <div align="center">
     여러분의 테니스 대회 참가를 더욱 편리하고 즐겁게 만들어드립니다. "알케미스트"에 오신 것을 진심으로 환영합니다!
    </div>
</div>

## 📌 <a name="table">바로가기</a>

1. 🎾 [Introduction](#introduction)
2. 💻 [Quick Start](#quick-start)
3. ⚙️ [Tech Stack](#tech-stack)
4. 🗂️ [Folder Structure](#folder-structure)
5. 🔗 [Links](#links)
6. 📋 [Commit Convention](#commit-convention)

## <a name="introduction">🎾 Introduction</a>

당신의 테니스 대회 참가를 위한 모든 것을 한데 모았습니다! "알케미스트"에 오신 것을 환영합니다. <br/> 알케미스트는 테니스 대회 참가를 더욱 쉽고 효율적으로 만들기 위해 최선을 다하고 있습니다. <br/> 이 앱을 통해 당신은 다가오는 대회의 일정을 확인하고, 원하는 대회에 손쉽게 참가할 수 있습니다. <br/> 또한 다른 테니스 팬들과 함께 대회 결과를 공유하고, 승리의 기쁨을 함께 나눌 수 있습니다.

## <a name="quick-start">💻 Quick Start</a>

다음 단계에 따라 컴퓨터에서 로컬로 프로젝트를 설정합니다.

**Settings**

컴퓨터에 다음이 설치되어 있는지 확인

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/en) v20.11.0
- [npm](https://www.npmjs.com/) v10.2.4

**Repository Clone**

```bash
git clone https://github.com/OZ-Coding-School/oz_02_collabo-007.git
```

**Check Your Node Version**

```bash
node -v
```

nvm이 설치되어 있는 경우

```bash
nvm use
```

**Installation**

프로젝트 설치

```bash
npm ci
```

**Setting Environment Variables**

프로젝트 root 경로에 `.env`를 생성

```env
API_URL
```

**Running the Project**

```bash
npm run dev
```

프로젝트를 보려면 브라우저에서 [http://localhost:3000](http://localhost:3000)을 엽니다.

## <a name="tech-stack">⚙️ Tech Stack</a>

- Next.js
- TypeScript
- TailwindCSS
- Stroybook
- framer-motion
- clsx

## <a name="folder-structure">🗂️ Folder Structure</a>

```
  📦 alchemist
 ┣ 📂 .github
 ┣ 📂 .storybook ------> (스토리북 설정)
 ┣ 📂 .vscode
 ┣ 📂 app
 ┃ ┣ 📂 _asset ------> (font, icon등 asset)
 ┃ ┃ ┣ 📂 fonts
 ┃ ┃ ┗ 📂 icons
 ┃ ┣ 📜 layout.tsx
 ┃ ┗ 📜 page.tsx
 ┣ 📂 components ------> (공통 컴포넌트)
 ┃ ┣ 📂 core ------> (가장 작은 core 단위)
 ┃ ┣ 📂 module ------> (여러개 core의 결합)
 ┃ ┗ 📂 organism ------> (여러 module의 결합)
 ┣ 📂 lib ------> (유틸리티 함수)
 ┃ ┣ 📂 hook ------> (hooks 폴더)
 ┃ ┗ 📂 utils ------> (util 함수)
 ┣ 📂 public
 ┣ 📂 stories ------> (storybook 파일)
 ┣ 📂 styles ------> (global 스타일)
 ┣ 📜 .eslintrc.json
 ┣ 📜 .gitignore
 ┣ 📜 .npmrc
 ┣ 📜 .nvmrc
 ┣ 📜 .prettierrc
 ┣ 📜 README.md
 ┣ 📜 next.config.mjs
 ┣ 📜 package-lock.json
 ┣ 📜 package.json
 ┣ 📜 postcss.config.mjs
 ┣ 📜 tailwind.config.ts
 ┗ 📜 tsconfig.json
```

## <a name="links">🔗 Links</a>

<span style="font-size:50px">🤪</span> 배포링크 아직없지롱

## <a name="commit-convention">📋 Commit Convention</a>

- 🎉 feat : 새로운 기능 추가
- 🪛 refactor : 코드 리팩터링
- 💣 fix : 기능 수정, 버그 수정
- 🖍️ chore : 오타 수정 및 새로운 기능이 추가되지 않고, 코드가 변경 된 경우 (주석 추가 및 수정 포함)
- 📝 docs : 문서 수정 (readme 수정 시)
- ⚙️ conf : 환경 설정
- 🗿 build : 빌드 관련 파일 수정 및 삭제한 경우
- ✅ test : 테스트 코드, 리팩터링 테스트 코드 추가(프로덕션 코드 변경 X)





### Alchemist 테니스 앱 프로젝트

## 프로젝트 처음시작 설정  

#### 1. 가상환경 설치하기(poetry)
  - mac:  
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```
  - windows  
  ```bash
  curl -sSL https://install.python-poetry.org | python -
  ```
  - 설치완료 후 `poetry --version` 으로 설치된 poetry 확인
  - poetry 가상환경 실행
  ```bash
  poetry shell
  ```
  - poetry 가상환경 비활성화
  ```bash
  deactivate
  ```
  - poetry 가상환경에 패키지 설치 
  ```bash
  poetry update
  ```

<br>

#### 2. 장고 명령어
- 서버 실행
  ```bash
  python manage.py runserver
  ```
- 데이터베이스 마이그레이션 파일 생성
  ```bash
  python manage.py makemigrations
  ```
- 데이터베이스 마이그레이션 적용
  ```bash
  python manage.py migrate
  ```
- 장고 슈퍼유저 생성  
  ```bash
  python manage.py createsuperuser
  ```
<br>


#### 3. 데이터베이스
- 장고는 기본적으로 sqlite을 사용하고 있어서 데이터베이스에 따로 연결을 설정을 해주지 않아도 된다. 테스트 단계에서는 sqlite를 사용하여 빠른 개발이 가능하고 서비스로 제공할 때 운영 환경에 따라 데이터베이스를 연결해주면 된다.
```py
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
<br>


# APIs  

### 1. 회원가입 / 로그인
장고에서 제공해주는 기본 URL: 127.0.0.1:8000/

- 회원가입
  - `api/v1/auth/signup/` : 회원가입 시 access token과 refresh token 쿠키에 설정

- 로그인
  - `api/v1/auth/signin/` : 회원가입 시 access token과 refresh token 쿠키에 설정

- 로그아웃
  - `api/v1/auth/logout/` : 회원가입 시 access token과 refresh token 쿠키에 설정





<br>
<br>
<br>



## 기본 Django 프로젝트 구조
- Django 프로젝트를 생성하면 기본적으로 다음과 같은 구조를 갖습니다:

```python
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app1/
        migrations/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    app2/
```





## 프로젝트 디렉토리: `myproject/`

- **`__init__.py`**: Python에서 현재 디렉토리를 패키지로 인식하게 해주는 파일입니다.
- **`settings.py`**: 프로젝트의 설정을 포함합니다. 데이터베이스 구성, 정적 파일 설정, 타임존 등의 설정이 여기에 포함됩니다.
- **`urls.py`**: 프로젝트의 URL 선언이 됩니다. 사이트의 URL과 적절한 뷰의 연결을 정의합니다.
- **`asgi.py`**와 **`wsgi.py`**: 프로젝트를 서비스하기 위한 ASGI(Asynchronous Server Gateway Interface)와 WSGI(Web Server Gateway Interface) 애플리케이션의 진입점입니다. 이를 통해 Django 앱을 웹 서버와 연결할 수 있습니다.

## 앱 디렉토리: `app1/`

- **`migrations/`**: 데이터베이스 스키마 변경사항을 관리하는 마이그레이션 파일들이 위치하는 디렉토리입니다.
- **`__init__.py`**: 이 디렉토리를 Python 패키지로 인식하게 합니다.
- **`admin.py`**: 이 파일을 통해 Django 관리자 사이트에서 모델을 관리할 수 있습니다.
- **`apps.py`**: 앱의 구성을 포함하는 파일입니다. 여기서 앱의 이름, 레이블 등을 설정할 수 있습니다.
- **`models.py`**: 앱의 데이터 모델을 정의합니다. Django ORM을 통해 데이터베이스와 상호작용합니다.
- **`tests.py`**: 앱의 테스트 케이스를 포함합니다.
- **`views.py`**: 애플리케이션의 뷰 함수를 정의합니다. 사용자의 요청에 대해 어떤 데이터를 처리하고, 어떤 템플릿을 보여줄지 결정합니다.


## 고급 Django 프로젝트 폴더 구조

대규모 또는 팀 프로젝트에서 고려할 수 있는 고급 폴더 및 파일 구조 예시입니다.

- `apps/`: 모든 Django 앱을 이 폴더 안에 넣습니다. 각 앱은 독립적인 기능 단위로 구성됩니다.
- `config/`: `settings.py`, `urls.py`, `wsgi.py`, `asgi.py` 등의 프로젝트 설정 파일을 이 폴더 안에 넣습니다.
- `core/`: 공통적으로 사용되는 모델, 뷰, 유틸리티 등을 포함합니다.
- `templates/`: 전역적으로 사용되는 템플릿 파일을 저장합니다.
- `static/`: CSS, JavaScript, 이미지 파일 등 정적 파일을 저장합니다.
- `media/`: 사용자가 업로드한 파일을 저장합니다.
- `tests/`: 프로젝트 전체의 테스트 코드를 포함합니다.
- `api/`: Django REST Framework를 사용하여 API를 구현할 때, API 관련 파일을 이 폴더에 넣습니다.


---

# Django와 Django Rest Framework (DRF)

Django는 Python으로 작성된 강력한 웹 프레임워크로서, MTV(Model-Template-View) 패턴을 사용합니다. 이는 전통적인 MVC(Model-View-Controller) 패턴과 유사하며, 주로 명칭상의 차이가 있습니다.

## Django MTV 패턴

- **Model**: 데이터와 데이터베이스의 상호작용을 관리합니다.
- **Template**: 사용자에게 보여질 HTML을 처리합니다.
- **View**: 사용자의 요청을 받아 처리하고, 적절한 응답을 반환합니다.

Django에서 "View"는 MVC의 "Controller"와 유사한 역할을 수행하고, "Template"은 MVC의 "View"에 해당합니다.

## Django Rest Framework (DRF)

DRF는 Django에서 RESTful API를 쉽게 구축할 수 있도록 도와주는 강력한 라이브러리입니다. DRF를 사용하면 주로 JSON이나 XML 같은 데이터 포맷으로 사용자에게 정보를 반환합니다. 이 경우, "Template" 대신 "View"에서 직접 데이터를 처리하고 반환합니다.

## DRF에서의 "View"

DRF에서 "View"는 클라이언트의 요청을 받아 모델과의 상호작용을 처리하고, 그 결과를 JSON 등의 형태로 클라이언트에게 반환하는 역할을 합니다. 이는 MVC 패턴에서의 "Controller" 역할에 해당합니다.

DRF는 이러한 역할을 수행하기 위해 `APIView` 클래스나 `ViewSet` 클래스와 같은 여러 추상화된 클래스와 믹스인을 제공합니다.

## 결론

Django와 DRF를 사용할 때, MVC 패턴의 원칙은 여전히 존재합니다. 다만, Django와 DRF에서는 "Controller"의 역할을 하는 구성 요소를 "View"라고 명명합니다. 이 "View"는 사용자의 요청을 처리하고 모델과의 상호작용을 담당하는 역할을 수행합니다.

---


## Best Practices

- **DRY (Don't Repeat Yourself)**: 코드의 중복을 최소화합니다.
- **모듈화**: 재사용 가능한 컴포넌트로 코드를 구성합니다.
- **명확한 네이밍**: 파일, 클래스, 함수의 이름을 명확하고 일관되게 지정합니다.
- **환경 분리**: 개발, 테스트, 운영 환경의 설정을 분리합니다 (`settings.py`).

## 참고 자료

- [Django 공식 문서](https://docs.djangoproject.com/en/3.2/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/en/latest/)





---

## 객체지향 프로그래밍 (OOP) 기초

객체지향 프로그래밍은 데이터(속성)와 그 데이터를 처리하는 데 필요한 메서드(행동)를 결합하여 객체를 생성하는 프로그래밍 패러다임입니다. 이는 다음과 같은 주요 원칙에 기반합니다:

- **캡슐화:** 데이터(속성)와 함수(메서드)를 클래스라는 하나의 단위로 묶어 관리합니다.
- **상속:** 한 클래스가 다른 클래스의 속성 및 메서드를 상속받을 수 있습니다.
- **다형성:** 같은 이름의 메서드가 다른 클래스에서 다른 동작을 할 수 있습니다.
- **추상화:** 복잡한 실제 세계를 단순화하여 모델링합니다.


## 장고에서의 MVC 패턴 적용

장고는 MVC의 변형인 MTV(Model-Template-View) 패턴을 사용합니다:

- **모델(Model):** 데이터베이스 스키마(데이터 모델)를 정의합니다.
- **템플릿(Template):** 사용자에게 보여지는 부분(HTML)을 담당합니다.
- **뷰(View):** 웹 요청을 받고 응답을 반환합니다. 컨트롤러의 역할을 합니다.

### 예시: 블로그 시스템

장고 프로젝트에서 객체지향 및 MVC 패턴을 적용하는 간단한 예시로 블로그 시스템을 들 수 있습니다.

#### 모델(Model)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### 뷰(View) 및 URLconf

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
```

urls.py:

```python
from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]
```

#### 템플릿(Template)

`blog/post_list.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>블로그</title>
</head>
<body>
    <h1>블로그 포스트 목록</h1>
    <ul>
        {% for post in}
```


# django SOLID 5개 원칙 설명 및 예시

## 1. Single Responsibility Principle (SRP) (단일 책임 원칙)

- **원칙 설명:** 한 클래스는 하나의 책임만 가져야 한다는 원칙입니다. Django에서는 모델(Model), 뷰(View), 템플릿(Template)의 분리를 통해 이 원칙을 적용할 수 있습니다. 예를 들어, 데이터베이스와 관련된 로직은 모델에, 사용자 인터페이스와 관련된 로직은 템플릿에, 그리고 이 둘 사이의 상호 작용을 처리하는 로직은 뷰에 담을 수 있습니다.
- **Django 예시:** Django에서 모델(Model), 뷰(View), 템플릿(Template)은 각각의 책임을 명확하게 분리합니다. 예를 들어, 사용자 모델은 사용자 데이터 관리만을 책임지며, 사용자 데이터를 화면에 표시하는 로직은 뷰나 템플릿에서 처리합니다.
- **Python 코드 예시:**
  ```python
  class UserManager:
      def create_user(self, username, password):
          # 사용자 생성 로직
          pass
  
  class UserAuthentication:
      def authenticate(self, username, password):
          # 사용자 인증 로직
          pass
  ```

## 2. Open/Closed Principle (OCP) (개방/폐쇄 원칙)

- **원칙 설명:** 소프트웨어 구성요소는 확장에는 열려 있어야 하지만, 변경에는 닫혀 있어야 한다는 원칙입니다. Django에서는 앱을 통해 프로젝트를 확장할 수 있으며, 미들웨어, 커스텀 유저 모델 등을 통해 기능을 추가하거나 변경할 수 있습니다.
- **Django 예시:** Django의 클래스 기반 뷰(Class-Based Views, CBV)는 확장이 매우 용이합니다. ListView나 DetailView와 같은 기본 뷰를 상속받아 필요에 따라 확장할 수 있습니다.
- **Python 코드 예시:**
  ```python
  class BaseView:
      def render(self):
          # 기본 렌더링 로직
          pass
  
  class CustomView(BaseView):
      def render(self):
          # 확장된 렌더링 로직
          super().render()
          # 추가 로직
  ```

## 3. Liskov Substitution Principle (LSP) (리스코프 치환 원칙)

- **원칙 설명:** 서브타입은 언제나 그것의 베이스 타입으로 교체할 수 있어야 한다는 원칙입니다. Django의 클래스 기반 뷰(CBV)는 이 원칙을 잘 따르고 있습니다. 예를 들어, Django의 제네릭 뷰는 상속을 통해 확장되며, 기반 클래스의 인터페이스를 유지하면서 추가적인 기능을 제공합니다.
- **Django 예시:** ar 클래스는 Transportation 클래스의 서브클래스입니다. start_transportation 함수는 Transportation의 인스턴스를 인자로 받지만, Car 인스턴스로 대체해도 문제없이 동작합니다. 이는 LSP 원칙을 잘 따르고 있다고 볼 수 있습니다.
- **Python 코드 예시:**
```python
  class Transportation:
    def start_engine(self):
        return "엔진이 시작되었습니다."

  class Car(Transportation):
    def start_engine(self):
        return super().start_engine() + " 안전벨트를 착용해주세요."

# 함수에서 Transportation 타입을 기대합니다.
def start_transportation(transportation):
    print(transportation.start_engine())

# Car 인스턴스는 Transportation의 서브타입으로 대체 사용될 수 있습니다.
car = Car()
start_transportation(car)  # "엔진이 시작되었습니다. 안전벨트를 착용해주세요."
  ```

## 4. Interface Segregation Principle (ISP) (인터페이스 분리 원칙)

- **원칙 설명:** 사용하지 않는 인터페이스는 클라이언트에 강제되어서는 안 된다는 원칙입니다. Django에서는 믹스인(Mixin)을 사용하여 필요한 기능만을 조합하여 사용할 수 있습니다. 이를 통해 더 깔끔하고 명확한 인터페이스를 제공할 수 있습니다.
- **Django 예시:** Django의 신호 시스템은 ISP의 좋은 예시입니다. 신호 수신자는 관심 있는 특정 이벤트에만 의존합니다.
- **Python 코드 예시:**
  ```python
  class WorkerInterface:
      def work(self):
          pass
  
  class Worker(WorkerInterface):
      def work(self):
          # 실제 작업 수행
          pass
  
  class SuperWorker(WorkerInterface):
      def work(self):
          # 더 복잡한 작업 수행
          pass
  ```

## 5. Dependency Inversion Principle (DIP) (의존성 역전 원칙)

- **원칙 설명:** 고수준 모듈은 저수준 모듈에 의존하지 않아야 하며, 둘 다 추상화에 의존해야 한다는 원칙입니다. Django에서는 이 원칙을 서드 파티 앱이나 Django의 앱들 간의 결합도를 낮추기 위해 사용할 수 있습니다. 예를 들어, 시그널(signals)을 사용하여 느슨한 결합을 구현할 수 있습니다.
- **Django 예시:** OrderView 클래스는 OrderServiceInterface에 정의된 메소드를 사용합니다. OrderService는 이 인터페이스를 구현하는 구체적인 클래스입니다. OrderView의 생성자를 통해 어떤 OrderServiceInterface 구현체를 주입받을지 결정함으로써, OrderView와 OrderService 간의 직접적인 의존성을 제거하고, 유연성 및 테스트 용이성을 높이고 있습니다.
- **Python 코드 예시:**
```python
from abc import ABC, abstractmethod

# 추상화된 서비스 인터페이스
class OrderServiceInterface(ABC):
    @abstractmethod
    def create_order(self, user, product_id):
        pass

# 구체적인 서비스 구현체
class OrderService(OrderServiceInterface):
    def create_order(self, user, product_id):
        return "Order created for {} with product ID {}".format(user, product_id)

# 뷰에서의 사용 - 의존성 주입을 통해
class OrderView:
    def __init__(self, order_service: OrderServiceInterface):
        self.order_service = order_service

    def post(self, user, product_id):
        result = self.order_service.create_order(user, product_id)
        return result

# 서비스 인스턴스 생성 및 주입
order_service = OrderService()
order_view = OrderView(order_service)
print(order_view.post('user123', 'product456'))
```



## django 애플리케이션 로그 확인(?)
- **Django Logging System**: 표준 Python logging 모듈을 사용하며, settings.py에서 설정을 통해 유연하게 로깅을 관리할 수 있습니다. 이 방법은 Django 프레임워크와 밀접하게 통합되어 있어서 Django 애플리케이션에서 널리 사용됩니다. 다양한 로그 레벨과 출력 형식을 지정할 수 있으며, 파일, 콘솔, 이메일 등 다양한 출력 대상을 설정할 수 있습니다. 기본적인 오류 추적 및 시스템 모니터링에 매우 유용합니다.

- **Custom Logging Model**: 데이터베이스에 사용자 행동 로그를 남기기 위해 커스텀 모델을 생성하는 방식입니다. 이 방식은 프로젝트의 특정 요구사항(예: 사용자 행동 분석, 감사 로그)에 맞춰 매우 상세한 로깅을 할 수 있게 해줍니다. 하지만, 로그 데이터의 증가로 인한 데이터베이스의 부하를 고려해야 합니다.

- **Third-Party Packages**: django-activity-stream, sentry와 같은 서드파티 패키지를 사용하는 방식입니다. 이 패키지들은 로깅을 위한 다양한 기능을 제공하며, 특히 sentry는 오류 로깅과 모니터링을 위해 매우 인기가 있습니다. sentry는 애플리케이션에서 발생하는 예외를 자동으로 캡처하고, 오류 분석과 알림 기능을 제공하여 신속한 대응을 가능하게 합니다.

