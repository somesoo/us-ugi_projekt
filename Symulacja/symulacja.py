import json
import os
import time
 
# Clearing the Screen
os.system('cls')

with open (r"C:\Users\johnny\Documents\Studia\V_semestr\uslugi\Symulacja\tools.json") as tag:
	data_tag = json.load(tag)

#for i in range(len(data_tag["Boards"])):
#	print(data_tag["Boards"][i]["Where"])


def takeID(item):
	for i in range(len(data_tag["Boards"])):
		if data_tag["Boards"][i]["ID"] == item:
			return i

def takeName(item):
	for i in range(len(data_tag["Worker"])):
		if data_tag["Worker"][i]["Name"] == item:
			return i

def take_tool(toolID, worker):
	i = int(takeID(toolID))
	j = int(takeName(worker))
	data_tag["Boards"][i]["Where"] = data_tag["Worker"][j]["Name"]
	data_tag["Worker"][j]["inv"].append(str({data_tag["Boards"][i]["ID"]})[2:-2])
	#print(data_tag["Boards"][i])

def return_tool(toolID, worker, pos):
	i = int(takeID(toolID))
	j = int(takeName(worker))
	data_tag["Boards"][i]["Where"] = 'place'
	data_tag["Worker"][j]["inv"].remove(data_tag["Worker"][j]["inv"][pos])
	#print(data_tag["Boards"][i])

def check_tool(toolID):
	print(data_tag["Boards"][int(takeID(toolID))])

def check_inv(name):
	print(data_tag["Worker"][int(takeName(name))])

def check_szafa():
	for i in range(len(data_tag["Boards"])):
			if data_tag["Boards"][i]["Where"] == "place":
				print(i, data_tag["Boards"][i]["ID"], data_tag["Boards"][i]["Name"])

def check_workers():
	for i in range(len(data_tag["Worker"])):
			check_inv(data_tag["Worker"][i]["Name"])

def reczna_sym():
	for i in range(len(data_tag["Worker"])):
		print(i, data_tag["Worker"][i]["Name"])
	who = int(input("wybierz tożsamość: "))
	while who > len(data_tag["Worker"])-1:
		print("nie ma takiego uzytkownika, wybierz ponownie: ")
		who = int(input("wybierz tożsamość: "))
	wyb = int(input("Co chcesz zrobić:\n1. zabrac narzedzie\n2. odlozyc narzedzie\n3. Sprawdz zawartosc szaf\n4. sprawdz ekwipunek\n5. Wyjdz\nPodaj wybor: "))
	while wyb != 5:
		if wyb == 1:
			tool = 0
			for i in range(len(data_tag["Boards"])):
				if data_tag["Boards"][i]["Where"] == 'place':
					print(i, data_tag["Boards"][i]["ID"], data_tag["Boards"][i]["Name"])
			tl = int(input("Które narzędzie: "))
			while tl > len(data_tag["Boards"])-1:
				print("nie ma takiego narzędzia, wybierz ponownie: ")
				tl = int(input("Które narzędzie: "))
			tool = data_tag["Boards"][tl]["ID"]
			take_tool(tool, data_tag["Worker"][who]["Name"])
			check_inv(data_tag["Worker"][who]["Name"])
		elif wyb == 2:
			tool = 0
			#for i in range(len(data_tag["Boards"])):
			if data_tag["Worker"][who]["inv"] == []:
				print("Ekwipunek pusty")
			else:
				print(who, data_tag["Worker"][who]["Name"], data_tag["Worker"][who]["inv"])
				tool = int(input("Podaj narzedzie do odlozenia: "))
				while tool > len(data_tag["Worker"][who]["inv"])-1:
					print("nie ma takiego narzędzia, wybierz ponownie: ")
					tool = int(input("Które narzędzie: "))
				return_tool(data_tag["Worker"][who]["inv"][tool], data_tag["Worker"][who]["Name"], tool)
				check_inv(data_tag["Worker"][who]["Name"])
		elif wyb == 3:
			check_szafa()		
		elif wyb == 4:
			check_inv(data_tag["Worker"][who]["Name"])
		elif wyb > 4:
			print("Poza zakresem, powrót do menu")
		wyb = int(input("Co chcesz zrobić:\n1. zabrac narzedzie\n2. odlozyc narzedzie\n3. Sprawdz zawartosc szaf\n4. sprawdz ekwipunek\n5. Wyjdz\nPodaj wybor: "))

def automa_sym(tool, who):
	print("Pracownik bierze narzedzie: ")
	take_tool(tool, who)
	time.sleep(1)
	print("\nSprawdzam stan narzedzia: ")
	check_tool(tool)
	time.sleep(1)
	print(tool, who)
	check_inv(who)
	time(time.sleep)
	print("\n\nPracownik oddaje narzedzie: ")
	return_tool(tool, who)
	time.sleep(1)
	print("\nSprawdzam stan narzedzia: ")
	check_tool(tool)
	time.sleep(1)
	print("Sprawdzam eq pracownika: ")
	check_inv(who)


choice = input("Podaj co chcesz zrobic:\n1. Automatyczna symulacja\n2. Reczna symulacja\n3. Sprawdz zawartosc szaf\n4. Sprawdz pracownikow\n5. Generuj raport\n6. Wyjscie\nPodaj liczbe: ")
while choice != '6':
	# Clearing the Screen
	os.system('cls')
	if choice == '1':
		for i in range(len(data_tag["Worker"])):
			print(i, data_tag["Worker"][i]["Name"])
		who = int(input("wybierz tożsamość: "))
		while who > len(data_tag["Worker"])-1:
			print("nie ma takiego uzytkownika, wybierz ponownie: ")
			who = int(input("wybierz tożsamość: "))
		for i in range(len(data_tag["Boards"])):
			print(i, data_tag["Boards"][i]["ID"], data_tag["Boards"][i]["Name"])
		tl = int(input("Które narzędzie: "))
		while tl > len(data_tag["Boards"])-1:
			print("nie ma takiego narzędzia, wybierz ponownie: ")
			tl = int(input("Które narzędzie: "))
		tool = data_tag["Boards"][tl]["ID"]
		automa_sym(tool, who)
		ans = input().split(' ')[0]
		os.system('cls')
	elif choice == '2':
		reczna_sym()
		ans = input().split(' ')[0]
		os.system('cls')
	elif choice == '3':
		check_szafa()
		ans = input().split(' ')[0]
		os.system('cls')
	elif choice == '4':
		check_workers()
		ans = input().split(' ')[0]
		os.system('cls')
	elif choice == '5':
		print("Raport:\n")
		check_workers()
		print("Zawartość szaf: \n")
		check_szafa()	
		ans = input().split(' ')[0]
		os.system('cls')
	elif choice == '6':
		print("Koniec")
		os.system('cls')
		exit()
	choice = input("Podaj co chcesz zrobic:\n1. Automatyczna symulacja\n2. Reczna symulacja\n3. Sprawdz zawartosc szaf\n4. Sprawdz pracownikow\n5. Generuj raport\n6. Wyjscie\nPodaj liczbe: ")
	