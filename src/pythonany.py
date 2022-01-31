import requests
import random

def create_acc():
    username = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(12))
    password = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#') for i in range(18))
    email = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for i in range(17))
    url = 'https://www.pythonanywhere.com/registration/register/beginner/'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '256',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'cookie_warning_seen=True; csrftoken=QPldz6eClLRiMvczJ3gRu8FlCP45cbZzoGhc1tOUgsQZ381qvNJk2tXt2KVqfoeZ; sessionid=oag2fm4ea17dklxonpvmq26v93xtzuok; _ga=GA1.1.912772697.1641589928; _gid=GA1.1.1863051091.1641589928; _gat=1',
    'Host': 'www.pythonanywhere.com',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/registration/register/beginner/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }
    data = {
    'csrfmiddlewaretoken': 'X3UhBXp7o52VRzA63M9InnvoGSwZq0uivUQg3kZpjM1C8cpXPwCbVINw6NnktdJI',
    'username': username,
    'email': email+'@gmail.com',
    'password1': password,
    'password2': password,
    'tos': 'on',
    'recaptcha_response_token_v3': '',
    }
    re = requests.post(url,headers=headers,data=data)
    return {"Username": f'{username}',"Email": f'{email}gmail.com',"Password": f'{password}',"Host": 'www.pythonanywhere.com'}
