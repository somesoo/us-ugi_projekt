import pymysql
import json

connection = pymysql.connect(host='192.168.113.64', user='jonatan',passwd='1234',database='uslugi')
cursor=connection.cursor()
cursor.execute("DELETE FROM `Workers` WHERE 1")
cursor.execute("DELETE FROM `Boards` WHERE 1")
with open (r"tools.json") as tag:
    json_obj = json.load(tag)

for item in range(len(json_obj["Boards"])):
    id = int(json_obj["Boards"][item]["ID"])
    name = json_obj["Boards"][item]["Name"]
    where = json_obj["Boards"][item]["Placement"]
    cursor.execute("insert into Boards(ID,Name,Placement) value(%s, %s, %s)",(id,name,where))

for item in range(len(json_obj["Worker"])):
    name = json_obj["Worker"][item]["Name"]
    for i in range(len(json_obj["Worker"][item]["inv"])):
        inventory = json_obj["Worker"][item]["inv"][i]
        #print(name, inventory)
        cursor.execute("insert into Workers (Name,Inventory) value (%s, %s)",(name,inventory))
        
connection.commit()
connection.close()