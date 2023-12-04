def solution(bandage, health, attacks):
    dur, heal ,bonus = bandage
    max_health = health
    t1 = 0
    for t2, damage in attacks:
        health = min(health + heal*(t2-t1-1) + bonus * ((t2-t1-1)//dur), max_health)
        health -= damage
        if health <= 0:
            return -1
        t1 = t2
    return health