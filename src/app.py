#!flask/bin/python
from flask import Flask, jsonify
from spell import SpellDataBase

app = Flask(__name__)

spell_db = SpellDataBase()


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/spellcasting/spells_by_class/', methods=['GET'], defaults={'character_class':None, 'spell_level': None})
@app.route('/api/spellcasting/spells_by_class/<string:character_class>', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_class/<string:character_class>/<int:spell_level>', methods=['GET'])
def get_class_spells(character_class, spell_level):
    return jsonify(spell_db.get_spell_list_by_class_and_level(character_class, spell_level))


@app.route('/api/spellcasting/spells_by_school/', methods=['GET'], defaults={'spell_school':None,'spell_level': None})
@app.route('/api/spellcasting/spells_by_school/<string:spell_school>', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_school/<string:spell_school>/<int:spell_level>', methods=['GET'])
def get_school_spells(spell_school, spell_level):
    return jsonify(spell_db.get_spell_list_by_school_and_level(spell_school, spell_level))


@app.route('/api/spellcasting/spells_by_name/', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_name/<int:spell_level>', methods=['GET'])
def get_name_spells(spell_level):
    return jsonify(spell_db.get_spell_list_by_level(spell_level))

if __name__ == '__main__':
    app.run(debug=True)