#!flask/bin/python
from flask import Flask, jsonify, render_template, make_response
from models.spell import SpellDataBase

app = Flask(__name__)

spell_db = SpellDataBase()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/spellcasting/spells_by_class/', methods=['GET'], defaults={'character_class':None, 'spell_level': None})
@app.route('/api/spellcasting/spells_by_class/<string:character_class>', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_class/<string:character_class>/<int:spell_level>', methods=['GET'])
def get_class_spells(character_class, spell_level):
    return spell_db.get_spell_list_by_class_and_level(character_class, spell_level)

@app.route('/spellcasting/spells_by_class/', methods=['GET'], defaults={'character_class':None, 'spell_level': None})
@app.route('/spellcasting/spells_by_class/<string:character_class>', methods=['GET'], defaults={'spell_level': None})
@app.route('/spellcasting/spells_by_class/<string:character_class>/<int:spell_level>', methods=['GET'])
def display_class_spells(character_class, spell_level):
    return render_template('class_spells.html', data=get_class_spells(character_class, spell_level))


@app.route('/api/spellcasting/spells_by_school/', methods=['GET'], defaults={'spell_school':None,'spell_level': None})
@app.route('/api/spellcasting/spells_by_school/<string:spell_school>', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_school/<string:spell_school>/<int:spell_level>', methods=['GET'])
def get_school_spells(spell_school, spell_level):
    return spell_db.get_spell_list_by_school_and_level(spell_school, spell_level)

@app.route('/spellcasting/spells_by_school/', methods=['GET'], defaults={'character_class':None, 'spell_level': None})
@app.route('/spellcasting/spells_by_school/<string:spell_school>', methods=['GET'], defaults={'spell_level': None})
@app.route('/spellcasting/spells_by_school/<string:spell_school>/<int:spell_level>', methods=['GET'])
def display_school_spells(spell_school, spell_level):
    return render_template('school_spells.html', data=get_school_spells(spell_school, spell_level))


@app.route('/api/spellcasting/spells_by_name/', methods=['GET'], defaults={'spell_level': None})
@app.route('/api/spellcasting/spells_by_name/<int:spell_level>', methods=['GET'])
def get_name_spells(spell_level):
    return spell_db.get_spell_list_by_level(spell_level)

@app.route('/spellcasting/spells_by_name/', methods=['GET'], defaults={'spell_level': None})
@app.route('/spellcasting/spells_by_name/<int:spell_level>', methods=['GET'])
def display_spells(spell_level):
    return render_template('spells.html', data=get_name_spells(spell_level))

if __name__ == '__main__':
    app.run(debug=True)