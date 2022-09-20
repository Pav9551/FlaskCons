from requests import get

res = get('https://api.github.com/events')
print(res.text)