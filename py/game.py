import random

player_hp = 100
enemy_hp = 100

while player_hp > 0 and enemy_hp > 0:
    action = input("Attack or Heal? ").lower()

    if action == "attack":
        damage = random.randint(10, 25)
        enemy_hp -= damage
        print("You attacked for", damage, "damage!")

    if action == "heal":
        heal = random.randint(10, 20)
        player_hp += heal
        print("You healed", heal, "HP!")

    enemy_damage = random.randint(5, 18)
    player_hp -= enemy_damage
    print("Enemy attacked you for", enemy_damage, "damage!")

    print("Player HP:", player_hp)
    print("Enemy HP:", enemy_hp)

if player_hp <= 0:
    print("You lost!")
else:
    print("You won!")