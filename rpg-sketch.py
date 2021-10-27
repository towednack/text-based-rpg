import time
import copy
import random

# Cores Para Texto
destaque = '\033[1;36m'
red = '\033[30;41m'
green = '\033[30;42m'
yellow = '\033[30;43m'
blue = '\033[30;44m'
white = '\033[30;107m'
noColor = '\033[m'

# Variáveis de Jogo
availableLocation = ['floresta', 'deserto', 'montanhas de neve', 'rio']
currentLocation = ' '
randomLocationNumber = 0

availableFarmItem = ['nothing', 'appleTree', 'blueberryBush', 'insectNest']
farmItemActive = False
farmItemOptions = ['take', 'leave']

locationGrammarCorrection = ' '

playerHealth = 100
playerDamage = 20

playerInventory = []
inventoryDefaultRemoved = False

monsterDefaultHealth = 50
monsterDefaultDamage = 5

# Variáveis de habilidade/opções
enemyOptions = ['attack', 'run']
basicOptions = ['explore']

inventoryOptionAdded = False
playerSafe = True
randomObjectValue = 0

# Base do Jogo
print(f'{destaque}', '≈='*9, f'╔==Wild╦Planet==╗', '≈='*9, f'{noColor}')

playerName = input('Olá aventureiro, antes de começar a sua jornada precisamos saber o seu nome - ')
time.sleep(1)
print(' ')
print('=≠'*20)
print(' ')

if currentLocation == ' ':
	randomLocationNumber = random.randrange(4)
	currentLocation = copy.copy(availableLocation[randomLocationNumber])

if currentLocation == 'floresta':
	locationGrammarCorrection = 'na'
elif currentLocation == 'montanhas de neve':
    locationGrammarCorrection = 'nas'
else:
	locationGrammarCorrection = 'no'

print(f'{yellow}Você está atualmente {locationGrammarCorrection} {currentLocation}!{noColor}')
print('=≠'*20)
print(' ')

while playerSafe == True:
    print('Opções disponíveis:')
    print(f'{white}--{basicOptions}{noColor}')
    menuChoice = input('O que você gostaria de fazer agora? ')
    
    if menuChoice == 'explore':
        randomObjectValue = random.randrange(3)
        if randomObjectValue == 0:
            print('Você não encontrou nada...')
            time.sleep(1)
            print(' ')
        else:
            print(f'Você encontrou um {availableFarmItem[randomObjectValue]}.')
            farmItemActive = True
            time.sleep(1)
            print(' ')
    if farmItemActive == True:
        print('Opções disponíveis:')
        print(f'{white}--{farmItemOptions}{noColor}')
        menuChoice = input(f'Há um {availableFarmItem[randomObjectValue]} sendo usado por {playerName}. O que quer fazer? ')
        farmItemActive = False

    if menuChoice == 'take':
            if playerInventory == []:
                inventoryOptionAdded = True
                basicOptions.append('inventory')
                
            if availableFarmItem[randomObjectValue] == 'appleTree':
                playerInventory.insert(0, availableFarmItem[randomObjectValue])
            if availableFarmItem[randomObjectValue] == 'blueberryBush':
                playerInventory.insert(1, availableFarmItem[randomObjectValue])
            if availableFarmItem[randomObjectValue] == 'insectNest':
                playerInventory.insert(2, availableFarmItem[randomObjectValue])
                
    elif menuChoice == 'inventory':
            if inventoryOptionAdded == True:
                print('Seu inventário:')
                if playerInventory == []:
                    print('Você não tem nenhum item ainda.')
                    print(' ')
                else:
                    print(f'{blue}>> {playerInventory}{noColor}')
                    print(' ')
            else:
                print(f'{red}O jogador {playerName} ainda não desbloqueou esta opção!{noColor}')
    elif menuChoice == 'invDev':
        print(f'Inventário do dev: {playerInventory}')
        print(' ')
    if menuChoice == 'explore' or menuChoice == 'inventory' or menuChoice == 'take' or menuChoice == 'leave':
        print('--'*10)
        print(' ')
    else:
        print(f'{red}{menuChoice}{noColor} {yellow}não é uma opção válida!{noColor}')
        print(' ')