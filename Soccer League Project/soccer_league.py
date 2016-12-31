import csv
import random


def avg_height_checker(list_of_teams):
    #A function used for finding average height of teams. The
    #avg height of each team will be stored in this list in the
    #format [sharks, dragons, raptors]
    avg_heights = []
    for team in list_of_teams:
        avg_height = 0
        for i in team:
            avg_height += int(i[1])
        avg_height = avg_height / len(team)
        avg_heights.append(int(avg_height))

    base_height = 0
    for i in avg_heights:
        if i - base_height < 1 and i - base_height > -1:
            return False #If the avg heights are within 1 inch of each other, False is
                         #returned and the while loop below is broken from""" 
        base_height = i

    return avg_heights  # If the avg heights are not within 1 inch of each other, they are returned


def write_letter(list_of_teams, dates, team_names):

    
    for team in list_of_teams:
        if team == sharks:
            team_name = team_names[0]
            date = dates[0]
        elif team == dragons:
            team_name = team_names[1]
            date = dates[1]
        else:
            team_name = team_names[2]
            date = dates[2]        
        for player in team:
            with open('letters/{}_{}.txt'.format(player[0].split()[0].lower(),
                                     player[0].split()[1].lower()), 'w') as letter:
                letter.write("""Dear {},\n\nWe are happy to inform you that your child, {}
will be playing soccer as part of the {} team. {}
will need lots of practice in order to be the best at soccer.
Because of this, the first practice day will be on {}. We hope to see you soon!""".format(
    player[3], # Name of guardian(s)
    player[0], # player's name
    team_name,      # team name
    player[0].split()[0],  #player's first name
    date)) # the first practice date
                letter.close()



if __name__ == "__main__": #prevent code from being executed when imported
    
    exp = []  # a list where experienced players will be stored
    not_exp = [] # a list where inexperienced players will be stored

    sharks = []
    dragons = []
    raptors = []
    league = [sharks, dragons, raptors]
    team_names = ['Sharks', 'Dragons', 'Raptors']
    dates = ['the 17th \nof March at 3pm',
             'the 17th \nof March at 1pm',
             'the 18th \nof March at 3pm']

    with open('soccer_players.csv') as player_file:
        player_reader = csv.reader(player_file)
        all_players = list(player_reader)
        player_file.close()
        
    for i in all_players[1:]:  # Starting at index 1 as index 0 is not a player
        if i[2] == 'YES':  # Sorting all players into experienced and not_experienced
            exp.append(i)
        else:
            not_exp.append(i)

    exp_per_team = int(len(exp)/3) # How many experienced players will be on each team
    not_exp_per_team = int(len(not_exp)/3) # How many inexperienced players will be on each team

    for team in league:
        for i in exp[:exp_per_team]:
            team.append(i)
            exp.remove(i)

    for team in league:
        for i in not_exp[:not_exp_per_team]:
            team.append(i)
            not_exp.remove(i)
        
        
    while avg_height_checker(league): #this while loop makes sure teams are of similar height
        index = random.randint(0,5) # chooses index of random player to swap - see below
        avg_heights = avg_height_checker(league)
        shortest_team = avg_heights.index(min(avg_heights))
        tallest_team = avg_heights.index(max(avg_heights))

        short_player = league[shortest_team][index] #these 4 lines swap a random player from the shortest -
        tall_player = league[tallest_team][index]   # - and tallest teams. This will be repeated until
        league[tallest_team][index] = short_player  # - teams are within 1 inch height of each other
        league[shortest_team][index] = tall_player



    write_letter(league, dates, team_names)
    
    
