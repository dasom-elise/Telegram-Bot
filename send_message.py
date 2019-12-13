import requests
from decouple import config



url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
# 봇과 대화하는 사용자의 ChatId 추출
#chat_id = requests.get(f'{url}/bot{token}/getUpdates').json()['result'][0]['message']['from']['id']
chat_id = config('CHAT_ID')
# 보낼 메시지 입력받기
text = input('메시지를 입력하세요: ')

send_message = requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}') # 토큰 다음은 메서드

print(send_message.text)