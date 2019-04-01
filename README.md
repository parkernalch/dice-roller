# dice-roller
console application that rolls polyhedral dice from plaintext equations

# Structure
# **/dice.py**
## Die class
#### Attributes
- **Value** (int): Number of sides
- **canAceUp** (bool): If the die rolls its maximum value, continue rolling and incrementing the roll result until it stops rolling max value
- **canAceDown** (bool): If the die rolls its minimum value, continue rolling and decrementing the roll result until it stops rolling min value
#### Methods:
- **Roll**(self):
roll and return a single die of type self.value
    - Output:
        ~~~
        {
            'result': Sum of dice rolls,
            'dice': [list of rolled dice values]
        }
        ~~~
        
- **RollN**(self, count):
roll and return <count> number of dice of type self.value
    - Output:
        ~~~
        {
            'result': Sum of all dice rolls,
            'dice': [[], [list of lists of all dice rolled], []]
        }
        ~~~

### Global Variables
- **standard_dice**:
dictionary containing standard array of polyhedral dice 
- **savage_dice**:
dictionary containing standard array of dice for Savage Worlds RPG

### Other Methods
- **Wild_Roll**(die, wild_die)
as per Savage Worlds rules, wild cards roll an additional 'exploding' d6 alongside all trait rolls and pick the die with the highest result. This method mimics that.
    - Output:
    ~~~
    {
        'crit_fail': Boolean value representing whether or not both dice were ones,
        'trait_fail': Boolean value representing whether or not non-wild die was a one,
        'result': Int value showing highest roll result from the two dice,
        'dice': [List of values for each roll of the selected die]
    }
    ~~~

# **/roll.py**
### Roll(equation):
uses regular expression matching to pull out atomic elements of a dice equation, which it then loops through, calling the Roll or RollN methods of the attached dice as necessary.
##### Usage
- Simple Rolls:
    - To roll a 20-sided die one time, one would enter the equation: 1d20 (<count>d<value>)
- Exploding Rolls:
    - To roll an exploding die, append an ! to the end of the roll atom: e.g. 1d4!
- Keep the highest N results from a group:
    - After the roll atom, include 'h[number to keep]'
    - e.g. 4d6h3 --> roll 4 six-sided dice and keep the highest 3
- Keep the lowest N results from a group:
    - After the roll atom, include 'l[number to keep]'
    - e.g. 4d6l3 --> roll 4 six-sided dice and keep the lowest 3

## To Do (other projects):
- Wrap this into a GUI and bundle an EXE with pyinstaller
- Create API that takes equation as POST request and returns the json object roll result
