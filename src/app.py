#!flask/bin/python
from flask import Flask, jsonify
from spell import Spell, SpellDataBase, ClassSpellList

app = Flask(__name__)

spell_db = SpellDataBase()


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/spellcasting', methods=['GET'])
def get_spells():
    return jsonify([vars(spell) for spell in spell_db.get_spells()])

@app.route('/api/spellcasting/<string:character_class>', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/<string:character_class>/<int:spell_level>', methods=['GET'])
def get_class_spells(character_class, spell_level):
    return jsonify([vars(spell) for spell in spell_db.get_spell_list_by_class_and_level(character_class.lower(), spell_level)])

if __name__ == '__main__':
    app.run(debug=True)