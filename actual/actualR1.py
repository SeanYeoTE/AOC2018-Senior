# Defeat the enemy hero in under three minutes.

# Select the hero you want to use:
# 'sorcerer' - arcane
# 'marksman' - ranged
# 'guardian' - melee

# DEFINE MISSION GOALS
hero.playAs('guardian')
ruins = hero.ruins

# LOGIC: Goliath
def goliathLogic(goliath):
    friends = hero.findFriends()
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

# LOGIC: Normal
def defaultUnitLogic(unit):
    enemy = unit.findNearestEnemy()
    if enemy:
        hero.command(unit, "attack", enemy)
    else:
        hero.command(unit, "move", {'x':40,'y':34})

# GAME PROCESSES
# GAME: Initialisation
#hero.moveXY(32, 34)

# GAME: Loop
while True:
    #who do I summon next?
    friends = hero.findFriends()
    for friend in friends:
        #if friend.type == "peasant":
        #    peasantLogic(friend)
        #    target = friend
        if friend.type == "goliath":
            goliathLogic(friend)
        else:
            defaultUnitLogic(friend)
    
    enemy = hero.findNearestEnemy()
    hero.moveXY(40, 34)
    # if hero.team == "humans":
    #     base = {'x':8,'y':34}
    #     posi = {'x':30,'y':34}
    # else:
    #     base = {'x':72,'y':34}
    #     posi = {'x':50,'y':34}
    # if hero.isReady("blink"):
    #     if hero.pos != base:
    #         hero.blink(base)
    #     else:
    #         hero.blink(posi)
    if enemy:
        if hero.isReady("terrify"):
            hero.terrify()
            hero.shield()
        # if hero.isReady("bash"):
        #     hero.bash(enemy)
        # if hero.isReady("slam"):
        #     hero.slam(enemy)
        # else:
        #     hero.attack(enemy)
        # if hero.isReady("envenom"):
        #     hero.envenom()