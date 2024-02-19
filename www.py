import requests

items = input("Enter the item : ")
items.lower()
items = items.replace(" ","_")
items +="_blueprint"

url = 'https://api.warframe.market/v1/items/{}/orders'.format(items)
headers = {'Content-Type': 'application/json'}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    json_data = response.json()
    ordersTab = json_data["payload"]["orders"]
    ordersTabSell = [elem for elem in ordersTab if elem["order_type"] == "sell"]
    ordersTabBuy = [elem for elem in ordersTab if elem["order_type"] == "buy"]
    #
    print("Sell : ")
    [print("{} : qqt{}".format(i["platinum"],i["quantity"])) for i in ordersTabSell]
    print("Buy : ")
    [print("{} : qqt{}".format(i["platinum"],i["quantity"])) for i in ordersTabBuy]

else:
    print(f"Error: {response.status_code}")
    print(response.text)

"""
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
x1, y1, x2, y2 = 475, 387, 1450, 459
"""
#https://stackoverflow.com/questions/52899174/real-time-ocr-in-python