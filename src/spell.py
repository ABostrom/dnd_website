from flask import jsonify
from enum import auto
import enum
class SpellComponent(enum.IntEnum):
    v = auto()
    s = auto()
    m = auto()

class SpellSchools(enum.IntEnum):
    abjuration = auto()
    conjuration =auto()
    divination = auto()
    enchantment = auto()
    evocation = auto()
    illusion = auto()
    necromancy = auto()
    transmutation = auto()

class CharacterClasses(enum.IntEnum):
    bard = auto()
    cleric = auto()
    druid = auto()
    paladin = auto()
    ranger = auto()
    sorcerer = auto()
    warlock = auto()
    wizard = auto()

class SpellLevels(enum.IntEnum):
    Cantrip = 0
    level1 = 1
    level2 = 2
    level3 = 3
    level4 = 4
    level5 = 5
    level6 = 6
    level7 = 7
    level8 = 8
    level9 = 9


class SpellDataBase:

    def __init__(self):
        super().__init__()

        self.spells = {
            1 : Spell(1, "Eldritch Blast", SpellSchools.evocation, SpellLevels.Cantrip, "1 action", 120, "Instantaneous", [SpellComponent.v, SpellComponent.s] 
            #,"A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage. \
            #The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. \
            #You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam."
            ), 
            
            2 :  Spell(2, "Mending", SpellSchools.transmutation, SpellLevels.Cantrip, "1 action", 0, "Instantaneous", [SpellComponent.v, SpellComponent.s, SpellComponent.m]
            ,"This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former damage.\
            This spell can physically repair a magic item or construct, but the spell can't restore magic to such an object."
            ),

            3 : Spell(3, "Eldritch Smash", SpellSchools.evocation, SpellLevels.level1, "1 action", 120, "Instantaneous", [SpellComponent.v, SpellComponent.s]
            #,"A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage. \
            #The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. \
            #You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam."
            ), 
        }

        #create dictionary of empty spell school objects.
        self.school_spells = {school: SpellList(school.name) for school in SpellSchools}
       
        #append the spell id, to the appropriate data table to get by school.
        for spell in self.spells.values():
            self.school_spells[spell.spell_school].add_spell_by_level(spell.spell_id, spell.spell_level)

        #create the class spell lists by level
        bard_spells = SpellList(CharacterClasses.bard, cantrips=[2])
        warlock_spells = SpellList(CharacterClasses.warlock, cantrips=[1])
        self.class_spells = {
            CharacterClasses.bard : bard_spells, 
            CharacterClasses.warlock : warlock_spells
        }

        self.spell_levels = SpellList("all")
        for spell in self.spells.values():
            self.spell_levels.add_spell_by_level(spell.spell_id, spell.spell_level)
        

        #print(self.get_spell_list_by_level())
        print(self.get_spell_list_by_school_and_level())
        #print(self.get_spell_list_by_class_and_level())

    def get_spells(self):
        return self.spells.values()

    def get_spell_by_id(self, spell_id):
        return self.spells[spell_id]

    def get_spell_list_by_class_and_level(self, character_class=None, spell_level=None):
        if character_class is None:
            return {char_class.name: {sp_level.name: [vars(self.spells[spell_id]) for spell_id in spell_ids] for sp_level, spell_ids in spell_lists.get_spells_by_level(spell_level).items()} for char_class, spell_lists in self.class_spells.items()}
        else : 
            if isinstance(character_class, str):
                character_class = CharacterClasses[character_class] # convert string to enum
            return {character_class.name : {sp_level.name: [vars(self.spells[spell_id]) for spell_id in spell_ids] for sp_level, spell_ids in self.class_spells[character_class].get_spells_by_level(spell_level).items()}}


    #this returns a spell list by school. and then by level.
    def get_spell_list_by_school_and_level(self, school=None, spell_level=None):
        if school is None:
            return {spell_school.name: {sp_level.name: [vars(self.spells[spell_id]) for spell_id in spell_ids] for sp_level, spell_ids in spell_lists.get_spells_by_level(spell_level).items()} for spell_school, spell_lists in self.school_spells.items()}
        else : 
            if isinstance(school, str):
                school = SpellSchools[school] #convert string to enum
            return {school : {sp_level.name: [vars(self.spells[spell_id]) for spell_id in spell_ids] for sp_level, spell_ids in self.school_spells[school].get_spells_by_level(spell_level).items()}}


    #tested and correct.
    def get_spell_list_by_level(self, spell_level=None):
        return {sp_level.name: [vars(self.spells[spell_id]) for spell_id in spell_ids] for sp_level, spell_ids in self.spell_levels.get_spells_by_level(spell_level).items()}


class SpellList:

    def __init__(self, name, cantrips=[], level1=[], level2=[], level3=[], level4=[], level5=[], level6=[], level7=[], level8=[], level9=[]):
        super().__init__()

        #default args on mutable objects in python share across classes. so clone into new array when storing.
        self.name = name
        self.spells_by_level = {
            SpellLevels.Cantrip: list(cantrips),
            SpellLevels.level1: list(level1),
            SpellLevels.level2: list(level2),
            SpellLevels.level3: list(level3),
            SpellLevels.level4: list(level4),
            SpellLevels.level5: list(level5),
            SpellLevels.level6: list(level6),
            SpellLevels.level7: list(level7),
            SpellLevels.level8: list(level8),
            SpellLevels.level9: list(level9)
        }


    def add_spell_by_level(self, spell_id, spell_level):
        self.spells_by_level[spell_level].append(spell_id)

    def get_spells_by_level(self, spell_level=None):
        if spell_level is None:
            return self.spells_by_level
        else :
            if isinstance(spell_level, int):
                spell_level = SpellLevels[spell_level]            
            return {spell_level : self.spells_by_level[spell_level]} # else just return the particular level of spell ids

class Spell:

    def __init__(self, spell_id, name, spell_school, spell_level, casting_time, spell_range, duration, components, description=""):
        super().__init__()
        self.spell_id = spell_id
        self.name = name
        self.spell_school = spell_school
        self.spell_level = spell_level
        self.casting_time = casting_time
        self.spell_range = spell_range
        self.duration = duration
        self.components = components
        self.description = description
        

    
    def serialize(self):
            return {
                'name': self.name, 
                'spell_school': self.spell_school,
                'casting_time': self.casting_time,
            }



db = SpellDataBase()