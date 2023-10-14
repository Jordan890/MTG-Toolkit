import { Edit, Save } from "@mui/icons-material";
import { useState } from "react";
import '../styles/Deck.css'

function Deck(){

    const [deckName, setDeckName] = useState("");
    const [deckPrice, setDeckPrice] = useState("$20.00");
    const [isEditing, setIsEditing] = useState(false);

    const handleNameChange = (e: any) => {
        setDeckName(e.target.value);
    }
    const handleEditClick = (e: any) => {
        setIsEditing(true);
    }
    const handleSaveClick = (e:any) => {
        setIsEditing(false);
    }
    const image = "https://cards.scryfall.io/art_crop/front/0/e/0ec6bee0-f3b9-48cc-9f75-e4029a8f5a8d.jpg?1675619927";

    const myStyle = { 
    backgroundImage:`url(${image})`,
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    };

    return (
        <>
        <div className="container">
            <div className="deckLayout">
                <div className="cardImage" style={myStyle}>
                    <div className="sameRow">
                        <form>
                            <fieldset disabled={!isEditing}>
                                <input 
                                type="text"
                                name="deckName"
                                value = {deckName}
                                onChange={handleNameChange}
                                /> 
                            </fieldset>
                        </form>
                        {!isEditing ? <button onClick={handleEditClick}><Edit/></button> : <button onClick={handleSaveClick}><Save/></button>}
                    </div>
                </div>
                <div className="sameRow">
                    <span className="singleRow">{deckPrice}</span>
                </div>
            </div>
        </div>
        </>
    )



}

export default Deck;