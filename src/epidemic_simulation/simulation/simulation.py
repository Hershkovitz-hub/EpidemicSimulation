import random
from random import randint
import numpy as np

states = ["SUSCEPTIBLE", "INFECTIOUS", "REMOVED"]


def generate_bodies_example(n_bodies: int) -> list:
    bodies = []
    for i in range(n_bodies):
        bodies.append(
            {
                "position_x": randint(0,50),
                "position_y": randint(0,50),
                "state": states[randint(0, 2)],
                "counter":0
            }
        )
    return bodies

def isInside(circle_x, circle_y, rad, x, y): 
      
    # Compare radius of circle 
    # with distance of its center 
    # from given point 
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad): 
        return True
    else: 
        return False

radius=10 #needs to be user input
infection_prob= 0.8 #needs to be user input
duration=2

def is_infected(infection_prob):
    infection=random.choices([0,1],weights=[1-infection_prob,infection_prob],k=1)
    if infection==[1]:
        return(True)

def calc(bodies):
    bodies_to_change=[]
    for main_body in bodies:
        if main_body['state']=='SUSCEPTIBLE': 
            circle_x=main_body['position_x']
            circle_y=main_body['position_y']
            rad=radius
            for sec_body in bodies:
                if sec_body['state']=='INFECTIOUS': 
                    x=sec_body['position_x']
                    y=sec_body['position_y']
                    if isInside(circle_x, circle_y, rad, x, y):
                        if is_infected(infection_prob):
                           bodies_to_change.append((circle_x,circle_y))
                break
    return(bodies_to_change)

def state_change(bodies,bodies_to_change):
    for ind_tup in bodies_to_change:
        for body in bodies:
            if body['position_x']==ind_tup[0] and body['position_y']==ind_tup[1]:
                body['state']='INFECTIOUS'
    return(bodies)
        
def sick_len(bodies,duration):
    for sick_body in bodies:
        if sick_body['state']=='INFECTIOUS': 
            sick_body['counter']+=1
            if sick_body['counter']>duration:
                sick_body['state']='REMOVED'
    return(bodies)




  




