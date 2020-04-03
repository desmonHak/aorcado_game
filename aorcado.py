def yo():
	if a == 2:
				
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("") 
		print("________________________________\n")
	elif a == 3:
		print("")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|") 
		print("|________________________________\n")
	elif a == 4:
		print("  ________________")
		print(" /")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|") 
		print("|________________________________\n")
	elif a == 5:
		print("  ________________")
		print(" /                |")
		print("|                 |")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|") 
		print("|________________________________\n")
	elif a == 6:
		print("  ______________________")
		print(" /                      |")
		print("|                  .-^^^^^^^-.")
		print("|                 / .======.  \\")
		print("|                 \/ 6   6   \/")
		print("|                  ( \____/  )")
		print("|                   \_______/")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|") 
		print("|________________________________\n")                  
	elif a == 7:
		print("  ______________________")
		print(" /                      |")
		print("|                  .-^^^^^^^-.")
		print("|                 / .======.  \\")
		print("|                 \/ 6   6   \/")
		print("|                  ( \____/  )")
		print("|          ___ooo___\_______/_________________")
		print("|         /                                   \\")
		print("|        |        echo por desmon: David       |")
		print("|         \\___________________________________/")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|") 
		print("|________________________________\n")
	elif a == 8:
			 
		print("  ______________________")
		print(" /                      |")
		print("|                  .-^^^^^^-.")
		print("|                 / .======. \\")
		print("|                 \/ 6   6  \/")
		print("|                  ( \____/ )")
		print("|          ___ooo___\______/_________________")
		print("|         /                                  \\")
		print("|        |       echo por desmon: David       |")
		print("|         \\__________________________________/")
		print("|                   |  |")
		print("|                   |  |")
		print("|                   | _|")
		print("|                   |  |")
		print("|                   |  |")
		print("|                   /-'\\")
		print("|                  /    \\")
		print("|                 (____ /")
		print("|") 
		print("|________________________________\n")
	elif a == 9:
		print("  ______________________")
		print(" /                      |")
		print("|                  .-^^^^^^-.")
		print("|                 / .======. \\")
		print("|                 \/ 6   6  \/")
		print("|                  ( \____/ )")
		print("|          ___ooo___\______/_________________")
		print("|         /                                  \\")
		print("|        |       echo por desmon: David       |")
		print("|         \\__________________________________/")
		print("|                   |  | |  |")
		print("|                   |  | |  |")
		print("|                   | _| |  |")
		print("|                   |  | |  |")
		print("|                   |  | |  |")
		print("|                   /-'\\ /'-\\")
		print("|                  /    \\/    \\")
		print("|                 (_____/\\_____)")
		print("|") 
		print("|________________________________\n")
	else:
		print(" \n")
		print(" \n")
		print("as perdido")
		print("vuelve a jugar")
		print(" \n")
		exit()
		
#a = a + 1

letra1 = False
letra2 = False
letra3 = False
letra4 = False
letra5 = False
letra6 = False
letra7 = False
letra8 = False
letra9 = False
letra10 = False
letra11 = False
letra12 = False

print(" \n")
print(" \n")


variable = False


e = 1
a = 1

palabra = list(raw_input("introduce la palabra: "))
print(" \n" * 100)
sda = len(palabra)
print("no introducir letras repetidas")

print("el numero de letras son: " + str(len(palabra)) + " \n")
print(" \n")
print(" \n")
print("tienes 9 vidas\n")

while True:
	letra = raw_input("ingrese una letra: ")
	if len(letra) > 2:
		print("no ingrese mas de una letra, el juego te lo dara como False.")
	if len(palabra) == 2:
		
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if letra1 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+ str(letra)+" =")
				print("========================================================")
				sda = len(palabra)
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================\n")
				print(" \n" * 3)
				if ad[0] == True and ad[1] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad == True and ad == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if letra1 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+ str(letra)+" =")
				print("========================================================")
				sda = len(palabra)
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				print(" \n" * 3)
				if ad[0] == True and ad[1] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad == True and ad == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()

		
			
	elif len(palabra) == 3:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if letra1 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if letra2 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if letra3 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 4:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if letra1 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if letra1 == True:
				print("========================================================")
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True:
				print("usted a ganado")
				exit()
					
			elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False:
				if ad[0] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[1] == True :
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[2] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[3] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True:
				print("usted a ganado")
				exit()
					
			elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False:
				if ad[0] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[1] == True :
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[2] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				elif ad[3] == True:
					print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
			
	elif len(palabra) == 5:
		
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			print("========================================================")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 6:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 7:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 8:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		elif palabra[7] == letra:
			letra8 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[7] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 9:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[7] == letra:
			letra8 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[7] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[8] == letra:
			letra9 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[8] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8]:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 10:
		
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[7] == letra:
			letra8 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[7] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[8] == letra:
			letra9 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[8] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[9] == letra:
			letra10 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[9] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
	elif len(palabra) == 11:
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[7] == letra:
			letra8 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[7] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[8] == letra:
			letra9 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[8] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[9] == letra:
			letra10 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[9] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[10] == letra:
			letra11 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[10] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
			
	elif len(palabra) == 12:
		
		if palabra[0] == letra:
			letra1 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[0] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[1] == letra:
			letra2 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[1] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[2] == letra:
			letra3 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[2] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
			
			
		elif palabra[3] == letra:
			letra4 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[3] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[4] == letra:
			letra5 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[4] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
	
		elif palabra[5] == letra:
			letra6 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[5] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[6] == letra:
			letra7 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[6] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[7] == letra:
			letra8 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[7] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[8] == letra:
			letra9 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[8] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[9] == letra:
			letra10 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[9] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
			
		elif palabra[10] == letra:
			letra11 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[10] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		elif palabra[11] == letra:
			letra12 = True
			ad = [letra1, letra2, letra3, letra4, letra5, letra6, letra7, letra8, letra9, letra10, letra11, letra12]
			print("=============================================")
			print("la letra: " + palabra[11] + " es correcta")
			print("=============================================\n")
			if True:
				print("= el numero de letras son: "+str(len(palabra))+"       =")
				print("= etsa es la letra que as introducido: "+str(letra)+"  =")
				print("========================================================")
				print("= "+str(sda)+"                                         =")
				print("= "+str(ad)+"                                          =")
				print("========================================================")
				if ad[0] == True and ad[1] == True and ad[2] == True and ad[3] == True and ad[4] == True and ad[5] == True and ad[6] == True and ad[7] == True and True == ad[8] and ad[9] == True and ad[10] == True and True == ad[11] == True:
					print("usted a ganado")
					exit()
					
				elif ad[0] == False or ad[1] == False or ad[2] == False or ad[3] == False or ad[4] == False or ad[5] == False or ad[6] == False or ad[7] == False or ad[8] == False or ad[9] == False or ad[10] == False or ad[11] == False:
					if ad[0] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[1] == True :
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[2] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[3] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[4] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[5] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[6] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[7] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[8] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[9] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[10] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
					elif ad[11] == True:
						print("la letra: " + letra + " es correcta pero falta una letra.")
				else:
					print("no a introducido ningun caracter corrector.")
		else:
			variable = True
			if variable == True:
				a = a + 1
			yo()
		 
		
		
			
	elif len(palabra) < 13:
		print("=============================================================")
		print("       ------ aqui as ingresado muchas palabras ------       ")
		print("=============================================================\n")
		exit()
	else:
		print("=============================================================")
		print("       ------ aqui as ingresado muchas palabras ------       ")
		print("=============================================================\n")
		exit()

# echo por Desmon
