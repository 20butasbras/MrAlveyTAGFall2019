"""
##### 0) Header #####
# Text Adventure Game
A chance to make your own Text Adventure Game.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canvas for more information.

# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""

##### 1) Author Info #####

# Change these three fields
__author__ = "21lawresha@washk12.org"
__title__ = " Ben ? "
__description__ = ('You are a Germen medieval peasant Farmmer who was in \n'+
'his field who has just thrown down his hoe down win by making 100 gold')

# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"


##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.

''''
Records:
    World:
        status (str): Whether or not the game is "playing", "won",
                      "quit", or "lost". Initially "playing".
        map (dict[str: Location]): The lookup dictionary matching 
                                   location names to their
                                   information.
        player (Player): The player character's information.

      
    Player:
        location (str): The name of the player's current location.
        inventory (list[str]): The player's collection of items.
                               Initially empty.
        state (bool: Hungry): the current health of the player
    
    Location:
        about (str): A sentence that describes what this location 
                     looks like.
        neighbors (list[str]): A list of the names of other places 
                               that you can reach from this 
                               location.
        stuff (list[str]): A collection of things available at 
                           this location.
        people (list[Person(s)]): a list of person(s) at a location
        
        Person:
            name (str): the person's name
            r_info (str): they say somthing random lore based
            Buy/sell (str): what the person sells/buys
            
            
'''

##### 3) Core Game Functions #####
# Implement the following to create your game.

def render_introduction():
    '''...'''
    return ("== Ben ? ==\n"+
            "= By Shaden Lawrence =\n"+
            "\n"+
            ".... *Nothing* ... *Something* Light your flying through space on a long voyage\n"+
            ' *Smack* ... your awake ... your hear in the distance "Ben ?"\n'+
            " you get up. your in a field your old. you dust your self off\n"+
            ' your old bones hurt then you hear it again "Ben!" this time more angry\n '+
            '"what are you doing... i dont pay you a a copper an hour for doing nothing"\n'+
            'Aw so you need money ... guess your job is to get money then.\n'+
            "== Objective Gained ==\n" + "== Get 10 gold==")
def random_cliff_text():
    
    
    
    
def create_map():
    return{
        'Farm House':{
            'neighbors':['Field','Town of Zik'],
            'about':"a old house sat on a hill over looking a large ranch it\n"+
                     "looks like it has not seen much use but there is a table nearby\n"+
                     "East is a large Field and to the South there is the town of Zik",
            'stuff':['1 gold','bowl of soup'],
            'people':['Your boss']
            }
            
        'Field':{
            'neighbors':['Farm house','Sheep Pasture','Woods 2'],
            'about':"A large Field of golden wheat\n",
            'stuff':["wheat","hoe"],
            'people':[]
            }
        
        'Sheep pasture':{
            'neighbors':['Field','Woods 1'],
            'about':"Large Field of grass there are some sheep with wool and\n"+
            'chikens with eggs',
            'stuff':['wool','eggs'],
            'people':[]
            }
        'Woods 1':{
            'neighbors':['Cavern','Pasture','Woods 3'],
            'about':"You are in a clearing in the forest ",
            'stuff':[],
            'people':[]
            }
        'Cavern 1':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 1':{
            'neighbors':['Cavern 1',],
            'about':"Calm still waters there might be a ship out there...\n"+
            'But probably not thats the edge of the world',
            'stuff':[],
            'people':[],
            }
        'Town of Zik':{
            'neighbors':['Farm house','Woods 2','River','Blacksmith'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Woods 2':{
            'neighbors':['Town of Zik', 'Thief Hideout','Field'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Thief Hideout':{
            'neighbors':['Woods 2','woods 3','Wood w/ River 1'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Woods 3':{
            'neighbors':['Thief Hideout','Cavern 2','Woods'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Cavern 2':{
            'neighbors':['Woods 3','Ocean 2','Cavern','Cavern 2','Woods 4',],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 2':{
            'neighbors':['Cavern 2'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Black Smith':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'River':{
            'neighbors':['Black Smith','Wood w/ River 1','Town of Zik'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Wood w/ River 1':{
            'neighbors':['River','Cavern 2','Thief Hideout','Wood w/ River'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Cavern 3':{
            'neighbors':['Wood w/ River 1','Woods 4','Cavern 2'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Woods 4':{
            'neighbors':['Cavern 3','Ocean 3','Cavern 2'],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 3':{
            'neighbors':['Woods 4'],
            'about':"",
            'stuff':['Gold egg'],
            'people':[],
            }
        "Ulga's House":{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Woods 5':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ginger Bread House':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Woods w/ River 2':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 4':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Clif 1':{
            'neighbors':[],
            'about':random_cliff_text(),
            'stuff':[],
            'people':[],
            }
        'Clif 2':{
            'neighbors':[],
            'about':random_cliff_text(),
            'stuff':[],
            'people':[],
            }
        'Clif 3':{
            'neighbors':[],
            'about':random_cliff_text(),
            'stuff':[],
            'people':[],
            }
        'Clif 4':{
            'neighbors':[],
            'about':random_cliff_text(),
            'stuff':[],
            'people':[],
            }
        'Ocean 5':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 6':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 7':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 8':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
        'Ocean 9':{
            'neighbors':[],
            'about':"",
            'stuff':[],
            'people':[],
            }
            
    }
def create_player():
    return {
        'location': 'Field',
        'inventory': [],
        'Gold': 0
        }

def create_world():
    return{
        'Map': create_map()
        'player': create_player(),
        'status':"playing"
        
    }
def render_player(world):
    
def render_location(world):
    # ...
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    # ...

def render_visible_stuff(world):
     location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']

    visible_stuff = []
    for thing in stuff:
        if thing == 'Grue':
            if 'flashlight' not in inventory:
                visible_stuff.append(thing)
        else:
            visible_stuff.append(thing)

    return "You see: " + ', '.join(visible_stuff)

def render(world):
    return (render_location(world) +
            render_player(world) +
            render_visible_stuff(world))
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.
    
    Args:
        world (World): The current world to modify.
    
    Returns:
        str: A message describing the change that occurred in the world.
    '''

def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.
    
    Args:
        world (World): The final world state to use in describing the ending.
    
    Returns:
        str: The ending text of your game to be displayed.
    '''

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.
    
    Note:
        Use your answer to Programming Problem #42.3
    
    Args:
        options (list[str]): The potential commands to select from.
    
    Returns:
        str: The command that was selected by the user.
    '''

###### 4) Win/Lose Paths #####
# The autograder will use these to try out your game
# WIN_PATH (list[str]): A list of commands that win the game when entered
# LOSE_PATH (list[str]): A list of commands that lose the game when entered.

WIN_PATH = []
LOSE_PATH = []
    
###### 5) Unit Tests #####
# Write unit tests here

from cisc108 import assert_equal

# Confirm that we printed the name of the game
assert_equal("== Ben ? ==" in render_introduction(), True)
# We should have 5 lines of text
assert_equal(render_introduction().count("\n"),7)
# Make sure it explicitly mentions "your house" to set up the punchline,
#   that you've been in your own house the entire game.
assert_equal("old bones" in render_introduction().lower(), True)

A)

###### 6) Main Function #####
# Do not modify this area

def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()
