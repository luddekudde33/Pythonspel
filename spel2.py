import random
import time
import sys
def clear():
    clear = "\n" * 100
    time.sleep(1.5)
    print(clear)

def skriv_ut(stringtoprint):
    for i in stringtoprint:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.07)
    clear() 

class Monster:
    def __init__(self):
        monsterNamn = ["Blixten McQueen", "bärgan","Doc Hudson", "Sally", "Chick Hicks", "mack", "Ramone", "Bert(världens bästa advokat)", "Guido", "Fillmore","Flo",]
        self.monsterNamn = random.choice(monsterNamn)
        self.HP = random.randint(5,40)
        self.str = random.randint(3,10)

    def taSkada(self,svärd):
        self.HP = self.HP - svärd.svärdStyrka

    def visaInfo(self):
        print(f"monsterts namn är: {self.monsterNamn}")
        print(f"monsterts hp är: {self.HP}")
        print(f"monsterts styrka är: {self.str}")


class Player:
    def __init__(self):
        self.namn = ""
        self.ryggsäck = [Item(), None, None, None, None]
        self.lvl = 1

    def karaktärbygge(self):
        self.namn = input("vad är ditt namn: ")
        self.HP = 30

    def taSkada(self,skada):
        self.HP = self.HP - skada
        if self.HP <= 0:
            skriv_ut(f"du förlorade på leveln {self.lvl}")
            exit()

    def lvlUpp(self):
        self.lvl = self.lvl+1
        if self.lvl > 10:
            skriv_ut(f"grattis {self.name} du klarade av spelet eftersom du nådde nivå 10!")
            exit()

    def visaInfo(self):
        print(f"ditt namn är: {self.namn}")
        print(f"ditt hp är: {self.HP}")
        print(f"din level är: {self.lvl}")
    

    def återställHp(self):
        self.HP = 30

    def läggTill(self,svärd):
        if self.finnsPlats():
            for i in range(0,5):
                if self.ryggsäck[i] == None:
                    self.ryggsäck[i] = svärd
                    return   
        else:
            self.visaRyggsäck()
            x = input("här ver det fullt, vilken plats vill du byta ut?")
            while x not in ["1","2","3","4","5"]:
                self.visaRyggsäck()
                x = input("här ver det fullt, vilken plats vill du byta ut?")
                
            self.ryggsäck[int(x)-1] = svärd 

    def finnsPlats(self):
        for i in self.ryggsäck:
            if i == None:
                return True
                
        return False              
                 



    def visaRyggsäck(self):
        for i in self.ryggsäck:
            if i:
                print(f"{i.svärdNamn} - styrka: {i.svärdStyrka}")
            else: 
                print("Här var det tomt")   
    

class Item: 
    def __init__(self):
        svärdNamn = ["Fire dragon", "Kökskniven", "Svärdet Bertil", "Nudisten leifös högra tå", "WOW jockes svärd"]
        self.svärdNamn = random.choice(svärdNamn)
        self.svärdStyrka = random.randint(1, 15)


class GameManager:
    def __init__(self,player):
        self.player = player
    
    def gameloop(self):
        alt = self.meny()
        if alt == 1:
            self.dörrar()
        elif alt == 2:
            self.player.visaRyggsäck()
        elif alt == 3:
            self.player.visaInfo()
        elif alt == 4:
            exit()           
    
    def start(self):
        skriv_ut(
        """
        Välkommen till mulle mecks äventyrsspel, du befinner dig i kylarköping.
        Detta spel går ut på att komma upp i en sådan hög level som möjligt!
        Du kommer slåss mot olika innvånare i byn och ställa dina sten, sax och påse kunskaper på prov!
        Du kommer presenteras med tre dörrar som antingen har en invånre, en kista med godsaker eller en fälla!
        För att vinna spelet så behöver du ta dig upp i nivå 10!
        Men först behöver jag veta ditt namn.
        """)
        self.player.karaktärbygge()

    def stenSaxPåse(self):

        self.player.visaRyggsäck()

        svärdVal = input("vilket svärd vill du välja (1-5) ?  ")
        while svärdVal not in ["1","2","3","4","5"] or not self.player.ryggsäck[int(svärdVal)-1]:
            self.player.visaRyggsäck()
            svärdVal = input("vilket svärd vill du välja (1-5) ?  ")
        svärd = self.player.ryggsäck[int(svärdVal)-1]

        monster = Monster()
        monster.visaInfo()

        while self.player.HP > 0 and monster.HP>0:

            sspVal = ["Sten", "Sax", "Påse"]

            spelarVal = input("välj Sten , Sax eller Påse:  ")

            while spelarVal not in sspVal:
                spelarVal = input("välj Sten, Sax eller Påse:  ")

            monsterVal = random.choice(sspVal)
            
            if spelarVal == monsterVal:
                skriv_ut("slipps som man säger i amerikat, tie!")
            elif spelarVal == "Sten" and monsterVal == "Sax":
                monster.taSkada(svärd)
                skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster.monsterNamn} valde Sax. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.")
                
            elif spelarVal == "Papper" and monsterVal == "Sten":
                monster.taSkada(svärd)
                skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster.monsterNamn} valde Sten. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.")
                
            elif spelarVal == "Sax" and monsterVal == "Påse":
                monster.taSkada(svärd)
                skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster.monsterNamn} valde påse. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.")
            
            else:
                self.player.taSkada(monster.str)
                skriv_ut(f"Mulle: Denna gång lyckades du inte men ge inte upp! Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.")
                
        self.player.lvlUpp()        
        skriv_ut(f"grattis {monster.monsterNamn} dog, din lvl är nu {self.player.lvl}")
        self.player.återställHp()


    def dörrar(self):
        print(
    """
    Vad vill du göra?
   1. dörr 1                    2. dörr 2                     3. dörr 3           
 __________________           __________________           __________________
/    __________    \         /    __________    \         /    __________    \ 
|   /          \   |         |   /          \   |         |   /          \   |
|   |          |   |         |   |          |   |         |   |          |   |
|   |          |   |         |   |          |   |         |   |          |   |
|   |          |   |         |   |          |   |         |   |          |   |
|   \__________/   |         |   \__________/   |         |   \__________/   |
|                  |         |                  |         |                  |
|    __      __    |         |    __      __    |         |    __      __    |
|   /  \    /  \   |         |   /  \    /  \   |         |   /  \    /  \   |
|   |  |    |  |   |         |   |  |    |  |   |         |   |  |    |  |   |
|   |  |    |  |   |         |   |  |    |  |   |         |   |  |    |  |   |
|   \__/    \__/   |         |   \__/    \__/   |         |   \__/    \__/   |
\__________________/         \__________________/         \__________________/
"""
    )
        lista = [1,2,3] 
        tal = random.choice(lista)
        dörrVal= input("välj en dörr 1,2 eller 3: ") 
        while dörrVal not in ["1","2","3"]:
            dörrVal= input("välj en dörr 1,2 eller 3: ") 
        if tal == 1:
            nyttHp = random.randint(3,7)
            self.player.taSkada(nyttHp)
            skriv_ut(f"{self.player.namn}, du öppnade en fälla och tappar där av {nyttHp} hp. Ditt hp är nu {self.player.HP}! ")
        elif tal == 2:
            svärd = Item()
            skriv_ut(f"Grattis du hittade {svärd.svärdNamn} - styrka: {svärd.svärdStyrka}")
            self.player.läggTill(svärd)

        elif tal == 3:
            skriv_ut(
                """
                Mulle:
                ojojoj bakom denna dörr väntade inte en fräsig kärra,
                utan du har kommit fram till ett monster.
                Jag hoppas att du har vässat dina sten, sax och påse kunskaper
                för nu kommer de behövas!
                """
            )
            self.stenSaxPåse()

        

    def meny(self):
        alt = input(
                """
                Vill du gå vidare till dörrarna tryck 1
                Eller vill du kolla din ryggsäck tryck 2 
                Eller kolla på info om din karaktär tryck 3
                Eller tryck 4 för att avsluta
                """) 
        clear()
        if alt in ["1","2","3","4"]:
            return int(alt)  
        return self.meny()

        
player = Player()
gameManager = GameManager(player)
gameManager.start()
while True:
    gameManager.gameloop()