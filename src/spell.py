
class SpellDataBase:

    def __init__(self):
        super().__init__()

        self.spells = {
            1 : Spell(1, "Eldritch Blast", "Evocation", 0, "1 action", 120, "Instantaneous", ["V", "S"], 
            "A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage. \
            The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. \
            You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam."), 
            
            2 :  Spell(1, "Mending", "Transmuation", 0, "1 action", 0, "Instantaneous", ["V", "S", "M"], 
            "This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former damage.\
            This spell can physically repair a magic item or construct, but the spell can't restore magic to such an object."),
        }


        bard_spells = ClassSpellList("bard", cantrips=[2])
        warlock_spells = ClassSpellList("warlock", cantrips=[1])

        self.class_spells = {
            bard_spells.character_class : bard_spells, 
            warlock_spells.character_class : warlock_spells
        }

    def get_spells(self):
        return self.spells.values()

    def get_spell_by_id(self, spell_id):
        return self.spells[spell_id]

    def get_spell_list_by_class_and_level(self, character_class, spell_level=None):
        return [self.spells[spell_id] for spell_id in self.class_spells[character_class].get_spells_by_level(spell_level)]



class ClassSpellList:

    def __init__(self, character_class, cantrips=[], level1=[], level2=[], level3=[], level4=[], level5=[], level6=[], level7=[], level8=[], level9=[]):
        super().__init__()

        self.character_class = character_class
        self.spells = {
            0: cantrips,
            1: level1,
            2: level2,
            3: level3,
            4: level4,
            5: level5,
            6: level6,
            7: level7,
            8: level8,
            9: level9
        }

    def get_spells_by_level(self, spell_level=None):
        if spell_level is None:
            return [spell_id for spell_ids in self.spells.values() for spell_id in spell_ids ] #return list of all spell ids
        else :
            return self.spells[spell_level] # else just return the particular level of spell ids



class Spell:

    def __init__(self, id, name, spell_school, spell_level, casting_time, spell_range, duration, components, description):
        super().__init__()
        self.id = id
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