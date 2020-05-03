import os
os.system('clear')
class Aorcado:
    def __init__(self):
        self.Vidasmaximas = 8
        self.PALABRA = str(input("introduce una palabra con la que iniciar el juego: "))
        self.pila = []

    def vida6(self):
        os.system('clear')
        print("""













        ________________________________\n
        """)

    def vida5(self):
        os.system('clear')
        print("""
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |________________________________\n""")

    def vida4(self):
        os.system('clear')
        print("""
            ________________
         /
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |________________________________\n""")

    def vida3(self):
        os.system('clear')
        print("""
		  ________________
		 /                |
		|                 |
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|________________________________\n""")

    def vida2(self):
        os.system('clear')
        print("""
		  ______________________
		 /                      |
		|                  .-^^^^^^^-.
		|                 / .======.  \\
		|                 \/ 6   6   \/
		|                  ( \____/  )
		|                   \_______/
		|
		|
		|
		|
		|
		|
		|
		|
		|
		|________________________________\n""")

    def vida1(self):
        os.system('clear')
        print("""
		  ______________________
         /                      |
        |                  .-^^^^^^^-.
        |                 / .======.  \\
        |                 \/ 6   6   \/
        |                  ( \____/  )
        |          ___ooo___\_______/_________________
        |         /                                   \\
        |        |        echo por desmon              |
        |         \\___________________________________/
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |________________________________\n""")
    def vida0(self):
        os.system('clear')
        print("""
          ______________________
         /                      |
        |                  .-^^^^^^-.
        |                 / .======. \\
        |                 \/ 6   6  \/
        |                  ( \____/ )
        |          ___ooo___\______/_________________
        |         /                                  \\
        |        |       echo por desmon:              |
        |         \\__________________________________/
        |                   |  |
        |                   |  |
        |                   | _|
        |                   |  |
        |                   |  |
        |                   /-'\\
        |                  /    \\
        |                 (____ /
        |
        |________________________________\n""")

    def dead(self):
        os.system('clear')
        print("""
		  ______________________
         /                      |
        |                  .-^^^^^^-.
        |                 / .======. \\
        |                 \/ 6   6  \/
        |                  ( \____/ )
        |          ___ooo___\______/_________________
        |         /                                  \\
        |        |       echo por desmon:             |
        |         \\__________________________________/
        |                   |  | |  |
        |                   |  | |  |
        |                   | _| |_ |
        |                   |  | |  |
        |                   |  | |  |
        |                   /-'\\ /'-\\
        |                  /    \\/    \\
        |                 (_____/\\_____)
        |
        |________________________________\n""")

    def YaMurio(self):
        print("\n\n\tas perdido vuelve a jugar\n")
        exit()

    def main(self):
        os.system('clear')
        longitud = len(list(self.PALABRA))
        for i in range(int(longitud)):
            self.pila.append(None)
        print('la palabra a averiguar tiene una longitud de: '+str(len(self.pila))+' de caracteres')

        z = 0
        a = []
        f = -1

        while True:
            self.Intento = str(input('introduce una letra: '))
            os.system('clear')
            for i in range(longitud):
                if self.PALABRA[z] == self.Intento:
                    self.pila[z] = self.Intento
                    print("la letra: "+str(self.Intento)+ " fue correcta")
                    print("te quedan: "+str(self.Vidasmaximas)+" vidas en total")
                    z += 1
                    a.append(True)

                else:
                    z += 1
                    a.append(False)

            for k in a:
                if f == 0:
                    f = 1
                if k == True:
                    pass
                else:
                    f += 1

            if f == longitud:
                self.Vidasmaximas -= 1

                if self.Vidasmaximas == 7:
                    self.vida6()
                elif self.Vidasmaximas == 6:
                    self.vida5()
                elif self.Vidasmaximas == 5:
                    self.vida4()
                elif self.Vidasmaximas == 4:
                    self.vida3()
                elif self.Vidasmaximas == 3:
                    self.vida2()
                elif self.Vidasmaximas == 2:
                    self.vida1()
                elif self.Vidasmaximas == 1:
                    self.vida0()
                elif self.Vidasmaximas == 0:
                    self.dead()
                    self.YaMurio()

            if self.pila == list(self.PALABRA):
                os.system('clear')
                print("as ganado")
                exit()
            a = []
            z = 0
            f = -1

                #if z == self.Vidasmaximas:
                #    z = 0
Aorcado = Aorcado()
Aorcado.main()
