import urllib.parse as parse
import urllib.request
from urllib.request import urlopen as req_url
import json
import string
import webbrowser

# Search API for most recent average price scrape
def warframe():
	print("Search for an item")
	search = input()
	print("Searching for " + string.capwords(search) + "...")

	main_url = req_url('https://api.warframe.market/v1/items/' + search.replace(' ', '_') + '/orders')
	data = main_url.read()
	parsed = json.loads(data)
	parsed_data = parsed['payload']['orders'][-1]['platinum']
	date_time = parsed['payload']['orders'][-1]['last_update']

	print(string.capwords(search) + " minimum price is " + str(parsed_data) + " platinum as of " + date_time)

# Request to open search on warframe.market
	def browser_open():
		print('Would you like to buy/sell ' + string.capwords(search) + "? y/n")
		browser_answer = input()
		if browser_answer == "y":
			webbrowser.open_new('https://api.warframe.market/v1/items/' + search.replace(' ', '_'))
		#if browser_answer == "n":
	browser_open()

# Restart the script
	def restart_script():
		print('Start a new search? y/n')
		answer = input()
		if answer == "y":
			warframe()
		if answer == "n":
			print('Goodbye')

	restart_script()
warframe()