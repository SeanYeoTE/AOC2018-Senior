# Enemy Hero
enemyBoss = hero.findByType("assassin", hero.findEnemies())[0]

# Summoning
summonRatio = {
    'peasant': 0.05,
    'soldier': 0.55,
    'griffin-rider': 0.0,
    'knight': 0.40
}

def getTotal(dictionary):
    totalList = list(dictionary.values())
    total = 0
    for n in totalList:
        total += int(n)
    return total

def toSummon():
    global summonRatio
    friendCount = {
        'peasant': 0,
        'soldier': 0,
        'griffin-rider': 0,
        'knight': 0
    }
    friendRatio = {
        'peasant': 0,
        'soldier': 0,
        'griffin-rider': 0,
        'knight': 0
    }
    friends = hero.findFriends()
    for friend in friends:
        friendCount[friend.type] += 1
    totalFriends = getTotal(friendCount)
    for friend in friendCount:
        friendRatio[friend] = (friendCount[friend] / totalFriends)
    differences = {
        'peasant': 0,
        'soldier': 0,
        'griffin-rider': 0,
        'knight': 0
    }
    for friend in differences:
        difference = summonRatio[friend] - friendRatio[friend]
        differences[friend] = difference
    highest = -5
    toSpawn = 'soldier'
    for friend in differences:
        if differences[friend] > highest:
            highest = differences[friend]
            toSpawn = friend
    return toSpawn

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
        if knight.isReady("bash"):
            hero.command(knight, "bash", enemy)
        elif knight.isReady("cleave"):
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
hero.moveXY(64, 20)

# GAME: Loop
while True:
    # Summon Units
    nextUnitType = toSummon()
    if hero.costOf(nextUnitType) <= hero.gold:
        hero.summon(nextUnitType)

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
    enemy = hero.findNearestEnemy()
    if item:
        #if hero.isReady("blink"):
        #    hero.blink(item.pos)
        #else:
        #    hero.move(item.pos)
        hero.move(item.pos)
    elif enemy:
        if hero.isReady("throw"):
            hero.throw(enemy)
        elif hero.isReady("cleave"):
            hero.cleave(enemy)
        hero.attack(enemy)
    else:
        for friend in friends:
            if friend.type == "knight" and friend.health < 60:
                if hero.cast("earthskin", friend):
                    hero.cast("earthskin", friend)
