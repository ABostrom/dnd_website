import React from 'react';
import ReactDOM from 'react-dom'

class Spell extends React.Component{

    
    //render the components of a single spell object.
    //Example Spell is Eldritch Blast
    // {
    //     "casting_time":"1 action",
    //     "components":["V","S"],
    //     "description":"A beam of crackling energy streaks toward a creature within range. 
    //     Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage. 
    //     The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level.             
    //     You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.",
    //     "duration":"Instantaneous",
    //     "name":"Eldritch Blast",
    //     "spell_id":"eldritch-blast",
    //     "spell_level":0,
    //     "spell_range":120,
    //     "spell_school":5
    // }
    render(){
        return (
            <div className="spell">
                <h2>{this.props.name}</h2>
                <p>
                    {this.props.description};
                </p>
            </div>
        );
    }
}




class SpellLevel extends React.Component{

    //this is a key, and an array.
    // "Cantrip" : [Object1, Object2]
    render(){

        //something like this.props.name could be level1 or Cantrip etc.
        //followed by an array of spell links.
        return(
            <div className="spell-level">
                <h2>{this.props.name}</h2> 
            </div>
        );
    }
}


class SpellList extends React.Component{


    //this is an array of SpellLevel objects.
    
    //something like this.props.name could be Evokation / Warlock or something.
    //followed 
    render(){
        return(
            <div className= "spell-list">
                <h2>{this.props.name}</h2> 
                
            </div>
        );
    }
}



export function GetSpellsByName(){

    fetch('/api/spellcasting/spells_by_name/')
    .then(response => response.json())
    .then(data => {
      ReactDOM.render(process_json(data), document.getElementById('contents'));
    });
}
  
function process_json(json_data){

    const spells = []
    for(var spell_list_key in json_data){
        var spell_list = json_data[spell_list_key];
        for(var index in Object.values(spell_list)){
            var spell = spell_list[index];
            console.log(index + " "+ JSON.stringify(spell));
                spells.push(<a href={"spellcasting/spells_by_name/" + spell.spell_id + "/"} >{spell.name}</a>);
            }
        }

    console.log(spells);

    return (spells);
}