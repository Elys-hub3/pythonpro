import requests

verbs = ['GET', 'POST', 'PUT', 'OPTIONS', '404']

for verb in verbs:
	requ = requests.request(verb, 'http://localhost:8000')
	print(verb, requ.status_code, requ.reason)
