import stand_pic from './assets/stand.png'

function Card(){
    return(
        <div className="card">
            <img className="stand_image" src={stand_pic} alt="jojoimg"></img>
            <h2 className='Card-title'>Stand Name: The World</h2>
            <h3 className="Card-text">The World (ザ・ワールド（世界） Za Wārudo) is the Stand of DIO, featured in Stardust Crusaders.</h3>
        </div>

    );

}
export default Card