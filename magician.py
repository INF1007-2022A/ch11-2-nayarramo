"""
Chapitre 11.3

Classes pour représenter un magicien et ses pouvoirs magiques.
"""

import random as rd
from utils import clamp
from character import *


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	# TODO: __init__
	def __init__(self, name, power, min_level, mp_cost):
		super().__init__(name, power, min_level)
		self.mp_cost = mp_cost



# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician(Character):
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend 

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param max_mp: MP maximum
	:param attack: Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""

	def __init__(self, name, max_hp, max_mp, attack, magic_attack, defense, level):
		# TODO: Initialiser les attributs de Character
		super().__init__(name, max_hp, attack, defense, level)
		# TODO: Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		self.magic_attack = magic_attack
		self.max_mp = max_mp
		self.__mp = max_mp
		self.__spell = None
		self.using_magic = False

	@property
	def mp(self):
		return self.__mp

	@mp.setter
	def mp(self, val):
		self.__mp = clamp(val, 0, self.max_mp)

	# TODO: Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.
	@property
	def spell(self):
		return self.__spell

	@spell.setter
	def spell(self, val):
		if (val is not None) and (val.min_level > self.level): raise ValueError()
		else: self.__spell = val

	# TODO: Surcharger la méthode `compute_damage` 
	def compute_damage(self, other: "Character"):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
			# Soustraire à son MP le coût du sort
			# Retourner le résultat du calcul de dégâts magiques
		if self.will_use_spell():
			self.__mp -= self.__spell.mp_cost
			return self._compute_magical_damage(other)
		# Sinon
			# Retourner le résultat du calcul de dégâts physiques
		else: return self._compute_physical_damage(other)


	def will_use_spell(self):
		answer = (self.using_magic) and (self.__spell is not None) and (self.__spell.mp_cost < self.__mp)
		return answer

	def _compute_magical_damage(self, other: "Character"):
		# TODO: Calculer le dommage magique
		rand = rd.uniform(0.85, 1)
		critical = rd.randint(1, 8) == 1
		if critical: crit = 2
		else: crit = 1
		modifier = crit * rand
		dmg =  (((((2* (self.level + self.magic_attack) / 5)+ 2) * self.weapon.power) / 50) + 2) * modifier

		return int(dmg), critical


	def _compute_physical_damage(self, other: "Character"):
		# TODO: Calculer le dommage physique exactement de la même façon que dans `Character`
		return super().compute_damage(other)
