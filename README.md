# YuGiOh-Simulator
First personal project for Boot.Dev. A(n extremely) basic simulator for the Yu-Gi-Oh! card game using the classic rule-set. (Give or take a few things for the sake of maintaining a reasonable scope).
________________________________________________________________________________________________________________________________________________________________________________
-------------------------------------------------------------------Disclaimer-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is a non-profit project built purely for educational purposes. 

Yu-Gi-Oh! is owned by Konami, Shueisha and Studio Dice. Please support the official product.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
________________________________________________________________________________________________________________________________________________________________________________
The main rules are as follows:

    1. The Game Board is a 5X4 grid with 2 rows of 5 spaces alloted to each of 2 players.

    2. Each player starts the game with a total of 8000 life points. The first player to lose all of their life points loses.

    3. Each player starts the game drawing 5 cards from their deck of 40 cards, with an additional card being drawn at the start of each of their turns. If a player runs out of cards to draw, they automatically lose on the turn they fail to draw a card. (Commonly known as a "Deck Out") 

    4. Cards are separated into 3 broad categories: Monsters, Traps, and Spells.
        - Monster cards are placed on the player's front row and are used to attack the opponent's monsters or the opponent directly if they have no monsters summoned on their side of the field. 

        - Spell cards are played on the player's back row and can have a wide range of effects from boosting a monster's stats, to disarming trap cards and even regenerating the player's life points. Spell cards can either be played immediately or set faced down to activate later.

        - Trap cards must be set on the player's back row and cannot be activated until the opponent's turn at the earliest. Like spell cards, trap cards can have a wide range of effects, but they are usually geared more towards disrupting the opponent.    

    5. Each player has a "graveyard" where slain monsters and expended spells/traps are sent to. Some spell or trap effects may make it possible to retrieve cards from either player's graveyard.       

    6. A player can hold a maximum of 6 cards in their hand. If a player has more than 6 cards in their hand by the end of their turn, they are required to discard cards from their hand to their graveyard until they are down to 6.

    7. The turn order will be decided by coin toss, with the winner getting to choose whether to go first or second. To ensure the player going second has the opportunity to defend themself, the player who goes first will not be able to declare any attacks on the other player until their first turn has been completed.

These are the most basic rules of the game. Further information on turn structure and card use will be provided in the following sections.
________________________________________________________________________________________________________________________________________________________________________________

Monster Cards:

Monster cards are the player's main offensive force. They posses the following qualities:

 1. Rank 
            - A monster's rank determines the conditions for summoning the monster to the field.
                -Low rank monsters (Rank 1-4) can be summoned freely with no pre-requisites.
                -Mid rank monsters (Rank 5-6) require a monster currently on the player's side of the field to be tributed (sent from the field to the graveyard) in order to summon them.
                -High rank monsters (Rank 7 and above) require two monsters currently on the player's side of the field to be tributed in order to summon them.
            -Regardless of rank, only a single monster may be summoned from the player's hand to the field per turn, unless special summoned by the effect of a card.

2. Attack/Defense Points
            - Monster cards have scores representing their offensive and defensive capabilities.           

3. Mode
            - Monster cards can be placed on the field in one two modes: attack mode and defense mode.
                -Monsters in attack mode can be used to declare an attack on monsters on the enemy's side of the field, or on the enemy directly if they do not have any monsters summoned.
                -Monsters in defense mode cannot be used to attack the opponent in any way. However, they can shield you from being directly attacked by a monster and will not cost you any life-points even if they are destroyed by an attacking monster.
                -Monsters placed on the field in attack mode will always be face up, but monsters placed on the field in defense mode are initially placed face-down, preventing the opponent from seeing what they are.
                -Monsters can change from attack mode to defense mode or vice versa once per turn. Any monsters in attack mode that made an attack during the player's battle phase (see further in) will not be able to switch to defense mode for the duration of that turn.

4. Effect
            -Certain monsters may have an effect similar to a spell or trap card that activates under certain conditions.
            -Activation condtions include but may not be limited to:
                -Flipping a card initially in facedown defense position to face up position (If a facedown monster is attacked by another monster, it will automatically flip and activate it's effect regardless of it survives the attack. Facedown monters destroyed by a spell/trap/monster effect do not get flipped.)
                -The monster being sent from the field to the graveyard
                -A specified monster being on the field at the same time as the effect monster.
                -At the player's discretion.
________________________________________________________________________________________________________________________________________________________________________________         

