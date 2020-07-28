from epidemic_simulation.simulation import SimulationManager

test_remove_infected=SimulationManager([],{'infection_r':0.6,'infection_p':0.7,'sickness_duration':6})


test_remove_infected.infected_bodies=[
        {'counter':0,"state":'INFECTIOUS'},
        {'counter':1,"state":'INFECTIOUS'},
        {'counter':2,"state":'INFECTIOUS'},
        {'counter':3,"state":'INFECTIOUS'},
        {'counter':4,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':7,"state":'INFECTIOUS'},
        {'counter':8,"state":'INFECTIOUS'},
        {'counter':9,"state":'INFECTIOUS'}
    ]
test_remove_infected.bodies=[
        {'counter':0,"state":'INFECTIOUS'},
        {'counter':1,"state":'INFECTIOUS'},
        {'counter':2,"state":'INFECTIOUS'},
        {'counter':3,"state":'INFECTIOUS'},
        {'counter':4,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':7,"state":'INFECTIOUS'},
        {'counter':8,"state":'INFECTIOUS'},
        {'counter':9,"state":'INFECTIOUS'},
        {'counter':0,"state":'SUSCEPTIBLE'},
        {'counter':0,"state":'SUSCEPTIBLE'},
        {'counter':0,"state":'SUSCEPTIBLE'}
    ]

def test_count_not_greater_than_duration():
    test_remove_infected.remove_infected()
    count_list=[]
    for body in test_remove_infected.bodies:
        count_list.append(body['counter'])
    if all (count_list)<=test_remove_infected.sickness_duration:
        return True
    else:
        return False

test_remove_infected.infected_bodies=[
        {'counter':0,"state":'INFECTIOUS'},
        {'counter':1,"state":'INFECTIOUS'},
        {'counter':2,"state":'INFECTIOUS'},
        {'counter':3,"state":'INFECTIOUS'},
        {'counter':4,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':7,"state":'INFECTIOUS'},
        {'counter':8,"state":'INFECTIOUS'},
        {'counter':9,"state":'INFECTIOUS'}
    ]
test_remove_infected.bodies=[
        {'counter':0,"state":'INFECTIOUS'},
        {'counter':1,"state":'INFECTIOUS'},
        {'counter':2,"state":'INFECTIOUS'},
        {'counter':3,"state":'INFECTIOUS'},
        {'counter':4,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':6,"state":'INFECTIOUS'},
        {'counter':7,"state":'INFECTIOUS'},
        {'counter':8,"state":'INFECTIOUS'},
        {'counter':9,"state":'INFECTIOUS'},
        {'counter':0,"state":'SUSCEPTIBLE'},
        {'counter':0,"state":'SUSCEPTIBLE'},
        {'counter':0,"state":'SUSCEPTIBLE'}
]

def test_count_duration_equals_counter():
    will_be_REMOVED=[body for body in test_remove_infected.bodies if body['counter']==test_remove_infected.sickness_duration] 
    removed_before=[body for body in test_remove_infected.bodies if body['state']=='REMOVED'] 
    test_remove_infected.remove_infected()
    removed_after=[body for body in test_remove_infected.bodies if body['state']=='REMOVED'] 
    if len(removed_after)-len(removed_before)==len(will_be_REMOVED):
        return True
    else:
        return False

print(test_count_not_greater_than_duration())
print(test_count_duration_equals_counter())