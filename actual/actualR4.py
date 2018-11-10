# DEFINE MISSION GOALS
hero.playAs('guardian')
ruins = hero.ruins
enemyBoss = hero.findByType("guardian", hero.findEnemies())[0]

# LOGIC: Goliath
def goliathLogic(goliath):
    enemies = hero.findNearestEnemy()
    if enemies:
        if goliath.isReady("warcry"):
            hero.command(goliath, "warcry", goliath)
        elif goliath.isReady("hurl"):
            hero.command(goliath, "hurl", enemies, {'x':67,'y':34})
        elif goliath.isReady("stomp"):
            hero.command(goliath, "stomp", enemies)
        hero.command(goliath, "attack", enemies)
    else:
        hero.command(goliath, "move", {'x':40,'y':34})
#        hero.command(friend, "attack", friend.findNearest(enemies))

# LOGIC: Knight
def knightLogic(knight):
    enemy = knight.findNearestEnemy()
    if enemy:
        if knight.isReady("bash"):
            hero.command(knight, "bash", enemy)
        elif knight.isReady("cleave"):
            hero.command(knight, "cleave", enemy)
        else:
            hero.command(knight, "attack", enemy)
    # else:
    #     hero.command(knight, "move", {'x':40,'y':34})

# LOGIC: Artillery
def artilleryLogic(friend):
    target = friend.findByType("artillery", friend.findEnemies())[0]
    if target:
        hero.command(friend, "attack", target)
    else:
        enemy = hero.findNearestEnemy()
        hero.command(friend, "attack", enemy)

# LOGIC: Paladin
def paladinLogic(paladin):
    if paladin.isReady("heal"):
        hero.command(paladin, "cast", "heal", hero)
    # if paladin.isReady("shield"):
    #     hero.command(paladin, "shield")
    # else:
    #     enemy = paladin.findNearestEnemy()
    #     hero.command(paladin, "attack", enemy)
    # else:
    #     hero.command(paladin, "move", {'x':40,'y':34})

# LOGIC: Librarian
def librarianLogic(librarian):
    if librarian.canCast("grow"):
        hero.command(librarian, "cast", "grow", hero)
    elif librarian.canCast("shrink"):
        goliath = librarian.findByType("goliath", librarian.findEnemies())[0]
        if enemyBoss:
            hero.command(librarian, "cast", "shrink", enemyBoss)

# LOGIC: Necromancer
def necromancerLogic(friend):
    if friend.canCast("summon-undead"):
        hero.command(friend, "cast", "summon-undead")
    else:
        enemies = friend.findNearestEnemy()
        if enemies:
            hero.command(friend, "attack", enemies)

# LOGIC: Normal
def defaultUnitLogic(unit):
    enemy = unit.findNearestEnemy()
    if enemy:
        if unit.type != "skeleton":
            hero.command(unit, "attack", enemy)
    # else:
    #     hero.command(unit, "move", {'x':40,'y':34})

# GAME PROCESSES
# GAME: Initialisation
#hero.moveXY(32, 34)
friends = hero.findFriends()
for friend in friends:
    if friend.type != 'arrow-tower':
        hero.command(friend, "move", {'x':40,'y':34})

# GAME: Loop
while True:
    #who do I summon next?
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "goliath":
            goliathLogic(friend)
        # elif friend.type == "knight":
        #     knightLogic(friend)
        elif friend.type == "paladin":
            paladinLogic(friend)
        elif friend.type == "librarian":
            librarianLogic(friend)
        elif friend.type == "necromancer":
            necromancerLogic(friend)
        elif friend.type == "artillery":
            artilleryLogic(friend)
        else:
            defaultUnitLogic(friend)
    
    enemy = hero.findNearestEnemy()
    hero.moveXY(40, 34)
    if enemy:
        if hero.isReady("terrify"):
            hero.terrify()
            hero.shield()
        elif hero.isReady("bash"):
            hero.bash(enemy)
