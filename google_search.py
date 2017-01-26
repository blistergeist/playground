# google_search.py
from googleapiclient.discovery import build
import pprint
import pickle
from os.path import isfile

def main():
	if not isfile('result.pickle'):
		with open('E:\\!Personal\\!Projects\\Wisp\\google_api_key.txt') as f:
			apiKey = f.read()
		service = build('customsearch', 'v1', developerKey=apiKey)
		result = service.cse().list(q='trump AROUND(10) racist', cx='014942726804186683924:f5vs59viobs').execute()
		
		with open('result.pickle', 'wb') as f:
			pickle.dump(result, f)
	else:
		with open('result.pickle', 'rb') as f:
			result = pickle.load(f)
	print(type(result))
	print(result)

if __name__ == '__main__':
	main()