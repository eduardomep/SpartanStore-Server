from Videogame import Videogame
import json
class Videogames_DAO:
    def __init__(self):
        self.videogames = []
        self.counter = 0
    def newGame(self,name,year,price,category1,category2,category3,picture,banner,description):
        for videogame in self.videogames:
            if videogame.name == name:
                print('el nombre de juego ya está en uso')
                return False
        new = Videogame(self.counter,name,year,price,category1,category2,category3,picture,banner,description)
        self.videogames.append(new)
        self.counter += 1
        return True
    def deleteGame(self,name):
        for videogame in self.videogames:
            if videogame.name == name:
                print('elimino '+str(name))
                self.videogames.remove(videogame)
                return True
        return False
    def printGames(self):
        for videogame in self.videogames:
            print(str(videogame.id)+" - "+str(videogame.name))
    def getGamesNames(self):
        for videogame in self.videogames:
            return videogame
    def getGames(self):
        return json.dumps([Videogame.dump() for Videogame in self.videogames]) 
    def getGameByName(self,name):
        for videogame in self.videogames:
            if videogame.name == name:
                return videogame
        return False
    def getGamesByCategory(self,category):
        return json.dumps([Videogame.dump() for Videogame in self.videogames if Videogame.category1 == category or Videogame.category2 == category or Videogame.category3 == category ]) 