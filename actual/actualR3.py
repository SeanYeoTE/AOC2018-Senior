# DEFINE MISSION GOALS
hero.playAs('guardian')
ruins = hero.ruins

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

# LOGIC: Normal
def defaultUnitLogic(unit):
    enemy = unit.findNearestEnemy()
    if enemy:
        hero.command(unit, "attack", enemy)
    # else:
    #     hero.command(unit, "move", {'x':40,'y':34})

# GAME PROCESSES
# GAME: Initialisation
#hero.moveXY(32, 34)

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
        else:
            defaultUnitLogic(friend)
    
    enemy = hero.findNearestEnemy()
    hero.moveXY(40, 34)
    if enemy:
        if hero.isReady("terrify"):
            hero.terrify()
            hero.shield()
        if hero.isReady("bash"):
            hero.bash(enemy)
