from Comment import Comment
import json
class Comments_DAO:
    def __init__(self):
        self.comments = []
    def newComent(self,game,userName,description):
        new = Comment(game,userName,description)
        self.comments.append(new)
        return True
    def getCommentsByGame(self,gameName):
        return json.dumps([Comment.dump() for Comment in self.comments if Comment.game == gameName ]) 
