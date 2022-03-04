#VOKABELTRAINER
from os import system
from sre_constants import JUMP
from time import sleep
import random

#Terminal leeren
def clears():
	#Linux:
	#system("clear")
	#Windows
	system("cls")
#Menus
def menu(mode):
	#Startmenu
	if mode == "main":
		clears()
		print("VOKABELTRAINER\n")
		print("------------------------Auswahl------------------------\n")
		print("(1)  Vokabeln verwalten")
		print("(2)  Vokabeln suchen")
		print("(3)  Vokabeltraining beginnen")
		print("(4)  Vokabeltest")
		print("(5)  Punkt 5")
		print("(6)  Programm beenden")
		print("\n-------------------------------------------------------")
	#Vokabeltrainermenu
	if mode == "trainer":
		clears()
		print("VOKABELTRAINER\n")
		print("----------------------Vokabeltrainer----------------------\n")
		print("(1)  Englisch - Deutsch")
		print("(2)  Deutsch - Englisch")
		print("(3)  Zurück zum Startmenü")
		print("\n-------------------------------------------------------")		
	#Vokabeltestmenu	
	if mode == "test":
		clears()
		print("VOKABELTRAINER\n")
		print("----------------------Vokabeltest----------------------\n")
		print("Hier wirst du eine zuvor bestimmte Anzahl von Vokabeln abgefragt und kannst am Schluss genau sehen, welche Vokabeln du schon beherrschst und welche du noch üben musst.\n")
		print("(1)  Englisch - Deutsch")
		print("(2)  Deutsch - Englisch")
		print("(3)  Zurück zum Startmenü")
		print("\n-------------------------------------------------------")		
	#Vokabeln Verwalten Menü
	if mode == "manage":
		clears()
		print("VOKABELTRAINER\n")
		print("-------------------Vokabeln verwalten-------------------\n")
		print("(1)  Vokabeln hinzufügen")
		print("(2)  Alle Vokabeln anzeigen")
		print("(3)  Vokabeln löschen")
		print("(4)  Vokabelsammlung zurücksetzen")
		print("(5)  Zurück zum Startmenü")
		print("\n-------------------------------------------------------")		

# Dictionary mit Vokabeln als csv-Datei(de,eng) und Metadaten als csv-Datei(de, level )speichern
def voc_save(vocdic, vocstats):
	#Vokabeln speichern
	f = open("vokabeln.csv", "w")
	csv =""
	for de, eng in vocdic.items():
		csv = csv + de + "," + eng + "\n"
	f.write(csv)
	f.close()

	#Metadaten speichern
	f = open("vokabelstats.csv", "w")
	csv =""
	for word in vocdic.keys():
		if word in vocstats:
			csv = csv + word + "," + str(vocstats.get(word)) +"\n"
		else:
			csv = csv + word + "," + "0" +"\n"
	f.write(csv)
	f.close()

#csv-Datei und Metadaten laden
def voc_load():
	#Vokabeln laden
	f = open("vokabeln.csv")
	file_content = f.read()
	vocdic = {}
	#string in Zeilen aufteilen
	lines = file_content.split("\n")
	#Leere Elemente entfernen
	while "" in lines:
		lines.remove("")
	#Zeilen in einzelne Wörter aufteilen und dem Dic hinzufügen
	for paar in lines:
		words = paar.split(",")
		vocdic.update({words[0]: words[1]})
	f.close()

	#Metadaten laden
	f = open("vokabelstats.csv")
	file_content = f.read()
	vocstats = {}
	#string in Zeilen aufteilen
	lines = file_content.split("\n")
	#Leere Elemente entfernen
	while "" in lines:
		lines.remove("")
	#Zeilen in einzelne Wörter aufteilen und dem Dic hinzufügen
	for paar in lines:
		words = paar.split(",")
		if words[1] != "":
			vocstats.update({words[0]: str(words[1])})
		#Falls noch kein Level-Wert vorhanden
		else:
			vocstats.update({words[0]: "0"})
	f.close()
	return vocdic,vocstats

#Zufällige Vokabel aussuchen
def rndvoc():
	vocs, vocstats = voc_load()
	delist = list(vocs.keys())
	englist = list(vocs.values())
	levellist = list(vocstats.values())
	#zufälliges Level aussuchen
	rndvoc= ""
	rndsol = ""
	level = "empty"
	while level == "empty":
		x = random.randint(1,100)
		if x <= 30 and "0" in levellist:
			level = "0"
		elif x <=55 and "1" in levellist:
			level = "1"
		elif x <=75 and "2" in levellist:
			level = "2"
		elif x <= 90 and "3" in levellist:
			level = "3"
		elif x <= 96 and "4" in levellist:
			level = "4"
		elif "5" in levellist:
			level = "5"
	#Vokabel des Levels suchen
	while True:
		x = random.randint(0, len(levellist)-1)
		if levellist[x] == level:
			rndvoc = delist[x]
			rndsol = englist[x]
			break
	return(rndvoc, rndsol)





#Main
#csv-Datei mit Vokabeln erstellen, falls noch nicht vorhanden
f = open("vokabeln.csv", "a")
f.close()
f = open("vokabelstats.csv", "a")
f.close()

while True:
	clears()
	menu("main")
	select = input("Bitte wähle aus: ")
	
	#Bei leerer Abgabe
	if select == "":
		print("Bitte gebe die Zahl der Option ein, die du wählen möchtest.")
		sleep(2.5)
	
	#Vokabeln verwalten
	if select == "1":

		clears()
		vocs, vocstats = voc_load()
		while True:
			menu("manage")
			select_sub = input("Bitte wähle aus: ")

			#Vokabeln hinzufügen
			if select_sub == "1":
				while True:
					clears()
					print("VOKABELTRAINER\n")
					print("------------------Vokabeln hinzufügen-----------------")
					print("\nFügen sie neue Vokabelpaare hinzu\nUm zum Menü zurückzukehren, drücken sie Enter\n")
					newvocde = input("Gebe zuerst das deutsche und danach das englische Wort ein.\n")
					if newvocde == "":
						break
					clears()
					print("VOKABELTRAINER\n")
					print("------------------Vokabeln hinzufügen-----------------")
					print("\nFügen sie neue Vokabelpaare hinzu\nUm zum Menü zurückzukehren, drücken sie Enter\n")
					newvoceng = input("Gebe zuerst das deutsche und danach das englische Wort ein.\n" + newvocde + " => ")
					vocs.update({newvocde:newvoceng})
					vocstats.update({newvocde:0})
					clears()
					voc_save(vocs, vocstats)

			#Alle Vokabeln anzeigen
			if select_sub == "2":
				vocs, vocstats= voc_load()
				clears()
				print("VOKABELTRAINER\n")
				print("------------------Vokabeln anzeigen-----------------")
				for de, eng in vocs.items():
					print(de + " => "+ eng)
				print(f"Insgesamt {len(vocs)} Vokabeln")
				input("\nMit Enter gelangst du zurück zum Menü\n")

			#Vokabeln löschen
			if select_sub == "3":
				while True:
					vocs,vocstats = voc_load()
					clears()
					print("VOKABELTRAINER\n")
					print("------------------Vokabeln löschen-----------------")
					print("\nLöschen sie einzelne Vokabelpaare \nUm zum Menü zurückzukehren, drücken sie Enter\n")
					for de, eng in vocs.items():
						print(de + " => "+ eng)
					deletevocs = input("Gebe die deutsche Form des Wortes ein, dass du löschen willst: ")
					if deletevocs in vocs:
						vocs.pop(deletevocs)
					if deletevocs == "":
						break
					voc_save(vocs, vocstats)
					
			#Vokabeln zurücksetzen
			if select_sub == "4":
				select_sub = input("Möchtest du wirklich alle Vokabeln löschen? Zum abbrechen gebe ´cancel´ ein. ")
				if select_sub.lower() != "cancel":
					vocs = {}
					voc_save(vocs, vocstats)

			#zum Hauptmenü zurück
			if select_sub == "5":
				break

	#Vokabeln suchen
	if select == "2":
		vocs,vocstats = voc_load()
		#getrennte Listen mit deutsche und Englischen Worten erstellen
		delist = list(vocs.keys())
		englist = list(vocs.values())
		
		while True:
			clears()
			print("VOKABELTRAINER\n")
			print("-------------------Vokabeln suchen------------------")
			print("\nDurchsuche deine Vokabelsammlung nach einem\nbeliebigen deutschen oder englischen Wort\n")
			search = input("Wonach möchtest du suchen? Mit Enter kehrst du zum Menü zurück. \n")
			if search == "":
				break
			elif search in delist:
				vocsearchnum = delist.index(search)
				print(f"Das englische Wort für '{search}' ist '{englist[vocsearchnum]}'")
			elif search in englist:
				vocsearchnum = englist.index(search)
				print(f"Das deutsche Wort für '{search}' ist '{delist[vocsearchnum]}'")
			else:
				print(f"'{search}' konnte nicht gefunden werden")
			input()
	

	#Vokabeltraining starten
	#Levels: Neu 0 bei jedem richtig +1 bis 5, bei jedem Falsch -1
	if select == "3":
		vocs , vocstats = voc_load()
		clears()
		print("VOKABELTRAINER\n")
		#Submenü
		menu("trainer")
		
		select_sub = input("Bitte wähle aus: ")
		#Eng - De
		if select_sub == "1":
			while True:
				clears()
				print("VOKABELTRAINER\n")
				print("----------------------Vokabeltrainer----------------------\n")
				print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
				trainsol, trainvoc = rndvoc()
				guess = input(trainvoc + " => ")
				#Leere Eingabe
				if guess == "":
					print("Leere Abgabe. Was möchtest du tun?")
					select_sub= input("(1) Lösung anzeigen \n(2) Zurück zum Hauptmenü \n")
					if select_sub == "1":
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + trainsol)
						vocstats.update({trainsol:int(vocstats.get(trainsol))-1})
						input("Fortfahren mit Enter")
					elif select_sub == "2":
						break
				#Eingabe überprüfen
				else:
					#richtig
					if guess== trainsol:
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + trainsol)
						#Level erhöhen
						if int(vocstats.get(trainsol)) < 5:
							vocstats.update({trainsol:int(vocstats.get(trainsol))+1})
						input("Richtig!Fortfahren mit Enter \n")
					#falsch
					else: 
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + guess + "    |" + trainsol)
						#Level erhöhen
						if int(vocstats.get(trainsol)) > 1:
							vocstats.update({trainsol:int(vocstats.get(trainsol))-1})
						input("Falsch!Fortfahren mit Enter \n")
				voc_save(vocs, vocstats)

				
		#De - Eng
		if select_sub == "2":
			while True:
				clears()
				print("VOKABELTRAINER\n")
				print("----------------------Vokabeltrainer----------------------\n")
				print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
				trainvoc, trainsol = rndvoc()
				guess = input(trainvoc + " => ")
				#Leere Eingabe
				if guess == "":
					print("Leere Abgabe. Was möchtest du tun?")
					select_sub= input("(1) Lösung anzeigen \n(2) Zurück zum Hauptmenü \n")
					if select_sub == "1":
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + trainsol)
						input("Fortfahren mit Enter")
						vocstats.update({trainsol:int(vocstats.get(trainsol))-1})
					elif select_sub == "2":
						break
				#Eingabe überprüfen
				else:
					#richtig
					if guess== trainsol:
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + trainsol)
						#Level erhöhen
						if int(vocstats.get(trainvoc)) < 5:
							vocstats.update({trainvoc:int(vocstats.get(trainvoc))+1})
						input("Richtig!Fortfahren mit Enter \n")
					#falsch
					else: 
						clears()
						print("VOKABELTRAINER\n")
						print("----------------------Vokabeltrainer----------------------\n")
						print("Gebe die englische Übersetzung ein. Um die Lösung einzublenden oder zum Menü zurückzukehren, drücke Enter")
						print(trainvoc + " => " + guess + "    |" + trainsol)
						#Level erhöhen
						if int(vocstats.get(trainvoc)) > 1:
							vocstats.update({trainvoc:int(vocstats.get(trainvoc))-1})
						input("Falsch!Fortfahren mit Enter \n")
				voc_save(vocs, vocstats)
		if select_sub == "3":
			clears()
	

	#Vokabeltest
	if select == "4":
		vocs,vocstats = voc_load()
		#getrennte Listen mit deutsche und Englischen Worten erstellen
		delist = list(vocs.keys())
		englist = list(vocs.values())
		menu("test")
		test_lang = input("Bitte wähle aus:")
		test_count = input("Wie viele Vokabeln sollen abgefragt werden? Um alle Vokabeln abzufragen, gebe ´all´ ein: ")
		if test_count == "all":
			test_count = len(delist)-1
		elif int(test_count) > len(delist) or int(test_count) < 1:
			print(f"Fehler: Bitte Zahl zwischen 1 und {len(delist)} angeben")
			sleep(3)
			continue
		#Liste mit zufälligen Wörtern generieren
		#Eng-De
		if test_lang == "1":
			testwords = []
			solution = []
			while len(testwords) != int(test_count):
				rndnum = random.randint(1, len(englist)-1)
				rndword = englist[rndnum]
				rndsol = delist[rndnum]
				if not rndword in testwords:
					testwords.append(rndword)
					solution.append(rndsol)
		#De-Eng
		if test_lang == "2":
			testwords = []
			solution = []
			while len(testwords) != int(test_count):
				rndnum = random.randint(1, len(delist)-1)
				rndword = delist[rndnum]
				rndsol = englist[rndnum]
				if not rndword in testwords:
					testwords.append(rndword)
					solution.append(rndsol)

		#Test starten
		answers = []
	
		#Vokabeln abfragen
		for x in range(len(testwords)):
			clears()
			print("VOKABELTRAINER\n")
			print("------------------Vokabeltest-----------------\n")
			answers.append(input(testwords[x] + "=> "))
		
		#Auswertung
		mistakes = 0
		clears()
		print("VOKABELTRAINER\n")
		print("------------------Vokabeltest-----------------")
		for x in range(len(testwords)):
			print(testwords[x] + " => " + answers[x], end = "")
			if answers[x] == solution[x]:
				print("   |Richtig\n")
			else:
				print("   |Falsch, richtige Lösung: " + solution[x] + "\n")
				mistakes = mistakes +1 
		print(f"{int(test_count)-mistakes} von {test_count} richtig, das entspricht {(1-(mistakes/int(test_count)))*100}%")
		input("Möchtest du Fortfahren? ")



	if select == "5":
		clears()
		print("VOKABELTRAINER\n")
		print("------------------Punkt 5-----------------")
		input()

	#Programm beenden
	if select == "6":
		clears()
		break