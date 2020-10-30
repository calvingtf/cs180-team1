import pandas as pd


class SoccerPlayer:


    def __init__(self, player_id, name, nationality, position,
                 overall, age, hits, potential, team):
        self.player_id = player_id
        self.name = name
        self.nationality = nationality
        self.position = position
        self.overall = overall
        self.age = age
        self.hits = hits
        self.potential = potential
        self.team = team


    def __str__(self) -> str:
        return f"id: {self.player_id}, " \
               f"Name: {self.name}, " \
               f"Nationality: {self.nationality}, " \
               f"position: {self.position}, " \
               f"overall: {self.overall}, " \
               f"age: {self.age}, " \
               f"hits: {self.hits}, " \
               f"potential: {self.potential}, " \
               f"team: {self.team}"

    def toCsvString(self): #TODO test toCsvString function
        return f"{self.player_id};{self.name};{self.nationality};{self.position};" \
               f"{self.overall};{self.age};{self.hits};{self.potential};{self.team}\n"

    def toArray(self):#TODO test toArray function
        player = []
        player.append(self.player_id)
        player.append(self.name)
        player.append(self.nationality)
        player.append(self.position)
        player.append(self.overall)
        player.append(self.age)
        player.append(self.hits)
        player.append(self.potential)
        player.append(self.team)

        return player


csvPath = r'../FIFA-21Complete.csv'


def readCsv(path):
    DB = open(path, 'r', encoding='utf8')
    myList = DB.readlines()
    return myList


playerList = readCsv(csvPath)
players = []
twoDList = []
for line in playerList:
    elems = line.split(sep=';')  # "\"FC Barcelona \"\\n"
    twoDList.append(elems)
    tmpPlayer = SoccerPlayer(elems[0], elems[1], elems[2], elems[3], elems[4], elems[5], elems[6], elems[7], elems[8])
    players.append(tmpPlayer)

df = pd.DataFrame(twoDList, columns=['player_id', 'name', 'nationality', 'position',
                                     'overall', 'age', 'hits', 'potential', 'team'])


# print(df[df['name'] == 'Lionel Messi'])


def searchPlayerName(playerName:str, dataFrame):
    playerName = playerName.strip()
    if len(playerName) == 0:
        print('Please enter Player Name again')
        return
    else:
        dataFrame = dataFrame[dataFrame['name'].str.contains(playerName)]

        if dataFrame.empty:
            print(' Player not found')
        else:
            print(dataFrame)

    return dataFrame
searchPlayerName('Lionel Messi ',df)


def searchPlayerNationality(PlayerCountry:str, dataFrame):
    PlayerCountry = PlayerCountry.strip()
    if len(PlayerCountry) == 0:
        print('Please enter country again')
        return
    else:
        dataFrame = dataFrame[dataFrame['nationality'].str.contains(PlayerCountry)]

        if dataFrame.empty:
            print('Country not found')
        else:
            print(dataFrame)

    return dataFrame

def searchPlayerTeam(PlayerTeam:str, dataFrame):
    PlayerTeam = PlayerTeam.strip()
    if len(PlayerTeam) == 0:
        print('Please enter team again')
        return
    else:
        dataFrame = dataFrame[dataFrame['team'].str.contains(PlayerTeam)]

        if dataFrame.empty:
            print('team not found')
        else:
            print(dataFrame)

    return dataFrame


def searchPlayerPosition(PlayerPosition:str, dataFrame):
    PlayerPosition = PlayerPosition.strip()
    if len(PlayerPosition) == 0:
        print('Please enter position again')
        return
    else:
        dataFrame = dataFrame[dataFrame['position'].str.contains(PlayerPosition)]

        if dataFrame.empty:
            print('position not found, example enter CB,LW,RW')
        else:
            print(dataFrame)

    return dataFrame


def searchPlayerAge(PlayerAge:str, dataFrame):
    PlayerAge = PlayerAge.strip()
    if len(PlayerAge) == 0:
        print('Please enter again')
        return
    else:
        dataFrame = dataFrame[dataFrame['age'].str.contains(PlayerAge)]

        if dataFrame.empty:
            print('No player with that age')
        else:
            print(dataFrame)

    return dataFrame


def searchPlayerRating(PlayerRating:str, dataFrame):
    PlayerRating = PlayerRating.strip()
    if len(PlayerRating) == 0:
        print('Please enter rating again')
        return
    else:
        dataFrame = dataFrame[dataFrame['overall'].str.contains(PlayerRating)]

        if dataFrame.empty:
            print('No player with that rating')
        else:
            print(dataFrame)

    return dataFrame

# instead of http response, have a render and pass 2-d list of all filtered results
# modify get search back, and get attributes back