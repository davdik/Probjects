# import pymysql
#
# # Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='leLUkzukiE', passwd='wlWM83Jntl', db='leLUkzukiE')
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Getting all data from table “users”
# cursor.execute("INSERT into leLUkzukiE.users (name, id) VALUES ('John', 10)")
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()
#


# import urllib.request, json
#
# # Opening a web request
# url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ils&compact=n&apiKey=47310eaab41d6191e406")
# # Decoding response to str
# data = json.loads(url.read().decode())  # Decoding a web request
#
# # Parsing results
# results = data['results']
# USD_ILS = results['USD_ILS']
# val = USD_ILS['val']
# print(val)
