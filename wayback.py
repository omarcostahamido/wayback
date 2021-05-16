import requests
import time
import argparse
# this is how i did it on the terminal:
# curl -X POST -F 'url=https://soundcloud.com/snakehips-1' https://web.archive.org/save/https://soundcloud.com/snakehips-1

print('wayback by OCH [v0.1] (2021/05/16)')
print('')

parser = argparse.ArgumentParser(description='Save url address to Internet Archive\'s Wayback Machine.')
parser.add_argument('url', metavar='URL', type=str, nargs='+',
                    help='full address like https://github.com/')
args = parser.parse_args()

x = requests.get('https://api.github.com/repos/%s/contributors' % (args.location[0]))
x = requests.post('https://web.archive.org/save/%s' % (args.url[0]), data = {'url':args.url[0]})

result = x.json()
print(len(result))

for contributor in result:
	name = contributor['login']
	time.sleep(0.2)
	y = requests.get('https://api.github.com/users/%s' % (name))
	if (y.json()['name'] == None):
		print(y.json()['login'])
	else:
		print(y.json()['name'])