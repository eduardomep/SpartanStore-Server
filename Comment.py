import datetime
class Comment:
    def __init__(self,game,userName,description):
        self.userName = userName
        self.game = game
        self.date =  str(datetime.datetime.now())
        self.description = description
    def dump(self):
        return {
            'name': self.userName,
            'game': self.game,
            'date':  self.date,
            'description': self.description
        }