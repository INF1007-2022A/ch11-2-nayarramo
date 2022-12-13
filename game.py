"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""

import random
from utils import clamp
from character import *
from magician import *


# def deal_damage(attacker: "Character", defender: "Character"):
# 	# TODO: Calculer dégâts
# 	dmg, crit = attacker.compute_damage(defender)
# 	print(f"{attacker.name} used {attacker.weapon.name}\n  {defender.name} took {dmg} dmg")
# 	return dmg

def deal_damage(attacker: "Character", defender: "Character"):
	weaponUsed = attacker.spell.name if (isinstance(attacker, Magician) and attacker.will_use_spell()) else attacker.weapon.name
	dmg, crit = attacker.compute_damage(defender)
	print(f"{attacker.name} used {weaponUsed}\n  {defender.name} took {dmg} dmg")

	return dmg, crit

def run_battle(c1: "Character", c2: "Character"):
	print(f"{c1.name} ({c1.hp}) starts a battle with {c2.name} ({c2.hp})")
	_round = 0
	attacker, defender = c1, c2
	
	while c1.hp > 0 and c2.hp > 0:
		
		dmg, crit = deal_damage(attacker, defender)
		defender.hp = defender.hp - dmg
		if crit: print("-------Critical damage-------")
		print(f"{defender.name} now has {defender.hp} health points\n")
			
		attacker, defender = defender, attacker
		_round += 1
	
	if c1.hp == 0: print(f"{c1.name} is sleeping with the fishes")
	if c2.hp == 0: print(f"{c2.name} is sleeping with the fishes")
	return _round
