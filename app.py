import requests, html
from flask import Flask, render_template, request
from decouple import config
import pprint,random
# TELEGRAM API
app = Flask(__name__)
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

# GOOGLE API
google_url = 'https://translation.googleapis.com/language/translate/v2'
google_key = config('GOOGLE_TOKEN')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route(f'/{token}',methods=['POST'])
def telegram():
    # 1. 텔레그램이 보내주는 데이터 구조 확인
    pprint.pprint(request.get_json())
    # 2. 사용자 아이디, 메시지 추출
    chat_id = request.get_json().get('message').get('chat').get('id')
    message = request.get_json().get('message').get('text')

    # 사용자가 로또라고 입력하면
    if message == '로또':
        result = random.sample(range(1,46),6)
        # 사용자가 /번역 이라고 말하면 한-영 번역 제공
    elif message[:4] == '/번역 ':
        data = {
            'q': message[4:],
            'source': 'ko',
            'target': 'en'

        }    
        response = requests.post(f'{google_url}?key={google_key}',data).json()
        result = html.unescape(response['data']['translations'][0]['translatedText'])
# 그 외의 경우엔 메아리
    else:
        result = '로또 혹은 /번역 이라고 입력해보세요!'


    # 3. 텔레그램 API에 요청해서 답장 보내주기
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    return '', 200






@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    my_text = request.args.get('message')
    # 1.사용자가 입력한 데이터 받아오기
    # receive_message = requests.get(f'{url}/bot{token}/getUpdates').json()['result'][0]['from']['text']
    ### 2. 텔레그램 API 메시지 전송요청 보내기
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={my_text}')
    return '메시지 전송 완료!!:)'




# 반드시 제일 아래에/ 마지막에 실행되도록 할 것
if __name__ == '__main__':
    app.run(debug=True)