import requests

verbs = ['GET', 'POST', 'PUT', 'OPTIONS', 'TEST']

for verb in verbs:
	requ = requests.request(verb, '0.0.0.0:8080')
	print(verb, requ.status_code, requ.reason, requ.status_bar, requ.reason_phrase)