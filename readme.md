# 현재 백엔드 오류로 인해 작동하지 않습니다.

고칠 시간이 없습니다.ㅠㅠ 죄송합니다. 다른 프로젝트도 많으니 구경해주세요
# 크리스마스 익명편지 CML

"크리스마스 익명편지 CML(ChristMasLetter)"은 Flask 웹 프레임워크와 Firebase를 이용하여 만든 익명 편지 서비스입니다. 이 서비스를 사용하여 친구들에게 익명으로 메시지를 전할 수 있습니다.

## 스크린샷

### 홈 화면

![홈 화면](screenshots/home.jpg)

### 로그인 화면

![로그인 화면](screenshots/login.jpg)

### 편지함 화면

![편지함 화면](screenshots/inbox.jpg)

## 기능

- **회원가입 및 로그인:** 사용자는 회원가입을 통해 계정을 생성하고 로그인하여 서비스를 이용할 수 있습니다.

- **편지 작성 및 송신:** 로그인한 사용자는 다른 사용자에게 익명으로 편지를 작성하고 전송할 수 있습니다.

- **편지함 확인:** 받은 편지는 수신자의 편지함에 저장되며, 수신자는 로그인 후 편지함에서 편지를 확인할 수 있습니다.

- **로그아웃:** 사용자는 로그아웃하여 계정의 보안을 유지할 수 있습니다.

## 사용 방법

1. **사용자 계정 생성:** 웹 사이트에 접속하여 회원가입을 진행합니다.

2. **로그인:** 계정이 생성되면 로그인하여 서비스를 이용할 수 있습니다.

3. **편지 작성:** "Send Letter" 페이지에서 수신자의 닉네임을 입력하고 편지를 작성합니다.

4. **편지 확인:** 수신자는 로그인 후 "My Letters" 페이지에서 받은 편지를 확인할 수 있습니다.

5. **로그아웃:** 사용이 끝나면 로그아웃하여 계정의 보안을 유지합니다.

## 웹 사이트

방문하여 서비스를 이용하세요: [크리스마스 익명편지 CML](https://appoung.pythonanywhere.com)

## 개발 환경 설정

이 프로젝트는 Python과 Flask 웹 프레임워크, 그리고 Firebase를 사용하여 개발되었습니다. 아래는 개발 환경 설정에 필요한 몇 가지 단계입니다.

1. **Python 및 Flask 설치:**

   ```bash
   pip3 install Flask
   ```

2. **Firebase 설정:**

   - Firebase 콘솔에서 프로젝트를 생성하고 서비스 계정을 위한 `serviceAccountKey.json` 파일을 다운로드합니다.
   - 다운로드한 파일을 프로젝트 루트에 추가합니다.

3. **Firebase 모듈 설치:**

   ```bash
   pip3 install firebase-admin
   ```

4. **실행:**
   ```bash
   python3 app.py
   ```

서비스를 사용하기 위해서는 위의 단계를 따라야 합니다.

## 라이센스

이 프로젝트는 [MIT 라이센스](LICENSE) 하에 배포되었습니다.

## 👤 Made by

   **한병준**


[![GitHub Badge](https://img.shields.io/badge/GitHub-181717?&logo=GitHub&logoColor=white&style=for-the-badge&link=https://github.com/appoung)](https://github.com/appoung)
