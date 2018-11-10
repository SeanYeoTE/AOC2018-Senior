# Unit-Summon Order
summonOrder = [
    'soldier',
    'soldier',
    'knight'
]
summonIndex = 0

# Peasants' Chest-Search Order
chestPriorities = [
    'gold-chest',
    'bronze-chest',
    'solver-chest'
]
chestIndex = 0

# Base Position
basePos = {}
if hero.pos.x < 40:
    basePos = {'x': 6, 'y': 59}
else:
    basePos = {'x': 74, 'y': 6}

# Enemy Hero
enemyBoss = hero.findByType("potion-master", hero.findEnemies())[0]

# To find an unclaimed chest of chestType.
def unclaimedChest(chestType):
    unclaimed = []
    chests = hero.findChests()
    # findChests includes all chests, whether carried or not.
    for chest in chests:
        # Check if the chest is being carried.
        if not chest.parent and chest.type == chestType:
            unclaimed.append(chest)
    return hero.findNearest(unclaimed)

# To choose the next in priority chest type.
def chooseChest():
    for k in range(len(chestPriorities)):
        nextChestType = chestPriorities[chestIndex % chestPriorities.length]
        chest = unclaimedChest(nextChestType)
        if chest:
            return chest
        chestIndex += 1
    return None

# LOGIC: Peasant
def peasantLogic(peasant):
    chest = chooseChest()
    # See if the peasant's carrying a chest.
    if peasant.peekItem():
        # Return it to base.
        hero.command(peasant, "dropItem", basePos)
    elif chest and not chest.parent:
        # Go pickup a chest!
        hero.command(peasant, "pickUpItem", chest)
    else:
        # If there is no chest to pickup, just return home.
        hero.command(peasant, "move", basePos)

# LOGIC: Knight
def knightLogic(knight):
    enemy = knight.findNearestEnemy()
    if enemy and enemy.type != "arrow-tower":
        if knight.isReady("cleave"):
            hero.command(knight, "cleave", enemy)
        # Advanced units have more than one ability.
        else:
            hero.command(knight, "attack", enemy)

# LOGIC: Archer Tower
def towerLogic(tower):
    enemy = tower.findNearestEnemy()
    if tower:
        hero.command(tower, "attack", enemy)

# LOGIC: Generic Unit
def defaultUnitLogic(unit):
    enemy = unit.findNearestEnemy()
    if enemy and enemy.type != "arrow-tower":
        hero.command(unit, "attack", enemy)
    else:
        hero.command(unit, "move", {'x': 40, 'y': 33})

# GAME: PROCESSES
# GAME: Initialisation

# GAME: Loop
while True:
    # Summon Units
    nextUnit = summonOrder[summonIndex % summonOrder.length]
    if hero.costOf(nextUnit) <= hero.gold:
        hero.summon(nextUnit)
        summonIndex += 1
    
    # Run Unit Logic
    friends = hero.findFriends()
    peasants = hero.findByType('peasant', friends)
    for friend in friends:
        if friend.type == 'peasant':
            peasantLogic(friend)
        elif friend.type == 'arrow-tower':
            towerLogic(friend)
        elif friend.type == 'knight':
            knightLogic(friend)
        else:
            defaultUnitLogic(friend)

    # LOGIC: Hero
    # attack enemies
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "arrow-tower":
        hero.attack(enemy)
