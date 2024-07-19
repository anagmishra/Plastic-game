import pygame
import pgzrun
import random
HEIGHT=500
WIDTH=500
initiallevel=1
finallevel=8
startspeed=10
itemlabels=["redbag","waterbottle","yellowlays","battery"]
isgameover=False
isgamecomplete=False
items=[]
animations=[]
def draw():
    global items, initiallevel, isgameover, isgamecomplete
    screen.clear()
    screen.blit("rrr",(0,0))
    if isgameover:
        screen.draw.text("game over, try again", fontsize=60, center=CENTRE, color="cyan")
    elif isgamecomplete:
        screen.draw.text("you did it, i guess", fontsize=60, center=CENTRE, color="cyan")
    else:
        for i in items:
            i.draw() # At least they show up

def update():
    global items
    if len(items)==0:
        items=createitems(initiallevel) #Number of items in a level equal to the number in the initial level variable

def createitems(noi): #Structure in which the functions are going to get called
    labelstocreate=getOptionsToCreate(noi) #labelstocreate will now have a list of bags
    newitems=generateitems(labelstocreate) #newitems will now have a list of Actors with the labels that were decided above
    spreadout(newitems) #We are spreading out those items evenly across the width of the screen
    animate(newitems) #Animate the items by aming them move downwards
    return newitems 

def getOptionsToCreate(noi):
    itemstocreate=["paperbag"] #Making sure that paper bags is always present
    for i in range(noi): #Displays as many items as noi
        itemstocreate.append(random.choice(itemlabels))
    return itemstocreate #Goes back to lime #15 for all returns
        
def generateitems(labelstocreate):
    newitems=[] 
    for i in labelstocreate: #labelstocreate now has all the items contained in the itemstocreate list
        item=Actor(i) # Creating as many Actors as items are to be created
        newitems.append(item)
    return newitems

def spreadout(newitems):
    numberofgaps=len(newitems) + 1 #Number of gaps will always be 1 more than the number of items
    gapsize=WIDTH/numberofgaps #Reduces the number of gaps for every increase in number of items
    random.shuffle(newitems)
    for index,item in enumerate(newitems): #Index contains index of newitems and item contains values of newitems
        x=(index+1)*gapsize
        item.x=x #Give x co-ordiante of the above value calculated

def animates(newitems):
    global animations
    for i in newitems:
        duration=startspeed-initiallevel
        i.anchor=("center","bottom") #It will anchor each items towards the bottom of the screen, in the center
        animation=animate(i, duration=duration, on_finished=handlegameover,y=HEIGHT) #We are saying that the object i, stays on the screen as long as the value is stored in the duration variable, and when the time ends, it will call the function that is given inside the on_finished.
        animations.append(animation)

def handlegameover():
    global isgameover
    isgameover=True

def on_mouse_down(pos):
    global items, initiallevel
    for i in items:
        if i.collidepoint(pos): #If i collides with the position
            if "paperbag" in i.image: #If paperbag is matching with the image of items
                handlegamecomplete()
            else:
                handlegameover()

def handlegamecomplete():
    global items,initiallevel, animations, isgamecomplete
    stopanimations(animations)
    if initiallevel==finallevel:
        isgamecomplete=True
    else:
        initiallevel+=1 #Adds to the current level
        items=[] #Resetting both the lists
        animations=[]

def stopanimation(animations):
    for i in animations:
        if i.running:
            i.stop()

pgzrun.go
