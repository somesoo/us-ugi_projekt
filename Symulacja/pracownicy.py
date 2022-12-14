import pymysql
import json

connection = pymysql.connect(host='192.168.182.64', user='jonatan',passwd='1234',database='uslugi')
cursor=connection.cursor()

with open (r"tools.json") as tag:
    json_obj = json.load(tag)
    
for item in range(len(json_obj["Worker"])):
    name = json_obj["Worker"][item]["Name"]
    inventory = json_obj["Worker"][item]["inv"]
    cursor.execute("insert into Workers (Name,Inventory) value (%s, %s)",(name,inventory))

connection.commit()
connection.close()