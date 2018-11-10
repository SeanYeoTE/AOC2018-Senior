# Unit-Summon Order
summonOrder = [
    'peasant',
    'soldier',
    'soldier',
    'peasant',
    'soldier',
    'soldier',
    'griffin-rider',
    'peasant',
    'soldier',
    'soldier',
]
summonIndex = 0

# Enemy Hero
enemyBoss = hero.findByType("assassin", hero.findEnemies())[0]

# Coin Gathering
def findGem(unit, limitDistance):
    items = unit.findItems()
    for item in items:
        distance = unit.distanceTo(item)
        if distance < limitDistance:
            if item.value == 5:
                return item
            elif item.value == 3:
                return item
            elif item.value == 2:
                return item
    return unit.findNearestItem()

# LOGIC: Knight
def knightLogic(knight):
    enemy = knight.findNearestEnemy()
    if enemy:
        if knight.isReady("cleave"):
            hero.command(knight, "cleave", enemy)
        # The hero has access to other knight's abilities as well:

        else:
            hero.command(knight, "attack", enemy)

# LOGIC: Peasant
def peasantLogic(peasant):
    item = findGem(peasant, 10)
    if item:
        hero.command(peasant, 'move', item.pos)
    else:
        hero.command(peasant, 'buildXY', 'arrow-tower', peasant.pos.x, peasant.pos.y)

# LOGIC: Generic Unit
def defaultUnitLogic(unit):
    enemy = unit.findNearestEnemy()
    if enemy:
        hero.command(unit, "attack", enemy)

# GAME: PROCESSES
# GAME: Initialisation
hero.summon('peasant')

# GAME: Loop
while True:
    # Summon Units
    nextUnitType = summonOrder[summonIndex % summonOrder.length]
    if hero.costOf(nextUnitType) <= hero.gold:
        hero.summon(nextUnitType)
        summonIndex += 1
    else:
        summonIndex += 1

    # Run Unit Logic
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "knight":
            knightLogic(friend)
        elif friend.type == "peasant":
            peasantLogic(friend)
        else:
            defaultUnitLogic(friend)

    # LOGIC: Hero
    # collect coins OR attack enemies
    item = findGem(hero, 6)
    #enemy = hero.findNearestEnemy()
    hero.move(item.pos)
    #if item:
    #    hero.move(item.pos)
    #elif enemy:
    #    hero.attack(enemy)
