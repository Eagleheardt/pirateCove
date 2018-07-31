import time
import os
import random

ppCove = """______          _          ______    _       _      ______ _           _         _____                _ 
| ___ \        | |         | ___ \  | |     ( )     | ___ (_)         | |       /  __ \              | |
| |_/ /_ _ _ __| |_ _   _  | |_/ /__| |_ ___|/ ___  | |_/ /_ _ __ __ _| |_ ___  | /  \/ _____   _____| |
|  __/ _` | '__| __| | | | |  __/ _ \ __/ _ \ / __| |  __/| | '__/ _` | __/ _ \ | |    / _ \ \ / / _ \ |
| | | (_| | |  | |_| |_| | | | |  __/ ||  __/ \__ \ | |   | | | | (_| | ||  __/ | \__/\ (_) \ V /  __/_|
\_|  \__,_|_|   \__|\__, | \_|  \___|\__\___| |___/ \_|   |_|_|  \__,_|\__\___|  \____/\___/ \_/ \___(_)
                     __/ |                                                                              
                    |___/                                                                               
"""

winString ="""
__   _______ _   _   _    _ _____ _   _ _ _ 
\ \ / /  _  | | | | | |  | |_   _| \ | | | |
 \ V /| | | | | | | | |  | | | | |  \| | | |
  \ / | | | | | | | | |/\| | | | | . ` | | |
  | | \ \_/ / |_| | \  /\  /_| |_| |\  |_|_|
  \_/  \___/ \___/   \/  \/ \___/\_| \_(_|_)
"""

loseString="""
__   _______ _   _   _     _____ _____ _____ 
\ \ / /  _  | | | | | |   |  _  /  ___|  ___|
 \ V /| | | | | | | | |   | | | \ `--.| |__  
  \ / | | | | | | | | |   | | | |`--. \  __| 
  | | \ \_/ / |_| | | |___\ \_/ /\__/ / |___ 
  \_/  \___/ \___/  \_____/\___/\____/\____/
"""

def makeFalse(gridSize,someArr):
	for i in range(0,gridSize):
		someArr.append([])
		for j in range(0,gridSize):
			someArr[i].append(False)
			
def makeObstacles(gridSize, obstacles, treasures):
	placed = 0

	while placed < (gridSize * 2):
		aRow = random.randint(0, gridSize)
		aCol = random.randint(0, gridSize)
		try:
			if not (obstacles[aRow][aCol]) and not (treasures[aRow][aCol]):
				placed+=1
				obstacles[aRow][aCol] = True
			else:
				continue
		except:
			continue
	
def buryTreasure(gridSize, obstacles, treasures):
	placed = 0

	while placed < gridSize:
		aRow = random.randint(0, gridSize)
		aCol = random.randint(0, gridSize)
		try:
			if not (obstacles[aRow][aCol]) and not (treasures[aRow][aCol]):
				placed+=1
				treasures[aRow][aCol] = True
			else:
				continue
		except:
			continue
	
def printGrid(gridSize, shovelHealth, totalTreasure, obstacles, treasures, digSquares):
	os.system('CLS')
	for i in range(0,gridSize):
		for j in range(0,gridSize):
			if digSquares [i][j]:
				if obstacles[i][j]:
					print("R ", end="")
				elif treasures[i][j]:
					print("X ", end="")
				elif digSquares[i][j]:
					print("E ", end="")
				else:
					print("O ", end="")
			else:
				print("O ", end="")
				
			if j is gridSize-1:
				print(i+1,end="")
			if i is 2 and j is gridSize-1:
				print("   ROWS",end="")
		print("")
		if i is gridSize-1:
			for k in range(0,gridSize):
				print(k+1 ,end=" ")
			print("""\n\nCOLUMNS\n
Shovel Health: {0}
Treasures left: {1}
""".format(shovelHealth,totalTreasure))

def printLegend(difficulty):
	dictDiff = {
	5:"a beginner",
	6:"an easy",
	7:"a medium",
	8:"a hard",
	9:"an expert"}

	legend = """You are exploring {0} difficulty island.
 ________________________________________________
| LEGEND                                         |
|                                                |
| O = Unexplored square                          |
| E = Empty square                               |
| R = Rock                                       |
| X = Treasure!                                  |
|________________________________________________|
""".format(dictDiff[difficulty])

	print(legend)

def askSize():
	print(ppCove)
	playField = input(
		"""(LEGAL NOTICE: We are not affiliated with Pirate Pete's Party Cove.)
		
How large of an island would you like to explore?

5 - beginner
6 - Easy
7 - Medium
8 - Hard
9 - Expert

Your Answer: """
	)
	try:
		playInt = int(playField)
		if (playInt >= 5 and playInt <= 9):
			return playInt
		else: 
			raise exception
	except: 
		print("Invalid Choice!")
		time.sleep (1)
		os.system('CLS')
		return askSize()
		
def checkSquare(aRow, aCol, fieldSize):
	try:
		if (0 < int(aRow) <= fieldSize) and (0 < int(aCol) <= fieldSize):
			return True
		else: 
			return False
	except: 
		return False
		
def preGame(difficulty):
	os.system('CLS')
	intro =""" _____________________________________________________________
|  _____          _                   _   _                   |
| |_   _|        | |                 | | (_)                  |
|   | | _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___   |
|   | || '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|  |
|  _| || | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \  |
|  \___/_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/  |
|_____________________________________________________________|

The island will have many obstacles!
You will have to find {0} treasures with only {1} shovel health.

Your shovel has limited uses, be careful!
Hitting an empty square will lower your shovel health by 1.
Hitting a rock will lower your shovel health by 5.
Hitting a treasure will not hurt your shovel.

After digging a square, it will be replaced by a symbol from the below legend.
""".format(difficulty,difficulty*3)

	print(intro)
	printLegend(difficulty)
	time.sleep (5)
	input("Press enter to continue")
	
def startGame():

	obstacles = []
	treasures = []
	digSquares = []

	playField = askSize()
	
	preGame(playField)
	
	makeFalse(playField, obstacles)
	makeFalse(playField, treasures)
	makeFalse(playField, digSquares)
	
	totalTreasure = playField
	shovelHealth = playField * 3
	
	makeObstacles(playField,obstacles, treasures)
	buryTreasure(playField,obstacles, treasures)

	while totalTreasure > 0 and shovelHealth > 0:
		printGrid(playField, shovelHealth, totalTreasure,obstacles, treasures, digSquares)
		printLegend(playField)
		
		pRow = input("Please select a row to dig in: ")
		pCol = input("Please select a column to dig in: ")
		
		if checkSquare(pRow, pCol, playField):
			rInt = (int(pRow)-1)
			cInt = (int(pCol)-1)
			if digSquares[rInt][cInt]:
				print("You've already dug there!")
				time.sleep (3)
				continue
			elif obstacles[rInt][cInt]:
				print("You hit a rock! -5 Shovel Health!")
				time.sleep (3)
				digSquares[rInt][cInt] = True
				shovelHealth -= 5
				if shovelHealth <= 0:
					shovelHealth = 0
					printGrid(playField, shovelHealth, totalTreasure,obstacles, treasures, digSquares)
					print("You broke your shovel!")
					print(loseString)
					time.sleep (6)
					input("\nPress enter to exit game.")
					exit()
				else:
					continue
			elif treasures[rInt][cInt]:
				print("You've struck treasure!")
				time.sleep (2)
				digSquares[rInt][cInt] = True
				totalTreasure -= 1
				if totalTreasure <= 0:
					printGrid(playField, shovelHealth, totalTreasure,obstacles, treasures, digSquares)
					print("You found all the treasure!")
					print(winString)
					time.sleep (6)
					input("\nPress enter to exit game.")
					exit()
				else:
					continue
			else:
				digSquares[rInt][cInt] = True
				print("No treasure there! -1 Shovel Health.")
				time.sleep (1)
				shovelHealth -= 1
				continue
		else:
			print("Enter valid coordinates!")
			time.sleep (1)
			continue
		
startGame()