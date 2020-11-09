from User_DAO import User_DAO
from Videogames_DAO import Videogames_DAO
from Comments_DAO import Comments_DAO
from flask import Flask
from User import User
from flask_cors import CORS
from flask.globals import request

app = Flask(__name__)
CORS(app)
# Creando una instancia de la clase para usuarios
userHandler = User_DAO()
userHandler.newUser("Usuario","Maestro","admin","admin","admin")
# Creando una instancia de la clase para video juegos
gameHandler = Videogames_DAO()
gameHandler.newGame("Crysis: Remastered 2020","2020",180.00,"Acción","Aventura","Bélicos","https://www.muycomputer.com/wp-content/uploads/2020/09/Crysis-Remastered-para-PC.jpg","https://cdn1.epicgames.com/17a1f8585f9246808597b30780aaf4fb/offer/EGS_CrysisRemastered_Crytek_S2-1200x1600-45e894b4daa06064cf2ae91bccf6221b.jpg?h=854&resize=1&w=640","El shooter clásico en primera persona de Crytek ha vuelto con un gameplay lleno de acción, un mundo abierto y las emocionantes batallas épicas que te atraparon la primera vez; ahora con gráficos remasterizados optimizados para una nueva generación de hardware.")
gameHandler.newGame("Grand Theft Auto: V","2013",320.00,"Acción","Aventura","Bélicos","https://tecnogaming.com/wp-content/uploads/2013/04/GTA-V-portada.jpg","https://cdn2.unrealengine.com/Diesel%2Fproductv2%2Fgrand-theft-auto-v%2Fhome%2FGTAV_EGS_Artwork_1280x720_V04-1280x720-31e7e0e50fda38709553f5313027ba5b76bd10b6.jpg","Grand Theft Auto V es un videojuego de acción-aventura de mundo abierto desarrollado por el estudio Rockstar North y distribuido por Rockstar Games. Fue lanzado el 17 de septiembre de 2013 para las consolas PlayStation 3 y Xbox 360.")
gameHandler.newGame("Mario Kart Live: Home Circuit","2020",250.00,"Carreras","Aventura","Multijugador","https://uvejuegos.com/img/caratulas/58430/mario-kart-8-deluxe.jpg","https://miro.medium.com/max/1040/0*Kq9QHUExjVZgZ_cY","Mario Kart Live: Home Circuit es un videojuego de carreras de realidad mixta desarrollado por Velan Studios y distribuido por Nintendo.​ Home Circuit utiliza juguetes de la vida real, con autos controlados a control remoto que responden a cómo juega el jugador en el juego.​")
gameHandler.newGame("Red Dead Revolver","2004",180.00,"Acción","Aventura","Disparos","https://upload.wikimedia.org/wikipedia/en/c/c1/Red_Dead_Revolver_Coverart.jpg","https://i.ytimg.com/vi/_8yxEqmxOvE/maxresdefault.jpg","Red Dead Revolver es un videojuego de disparos en tercera persona de tipo western publicado por Rockstar Games y desarrollado por Rockstar San Diego. Fue lanzado en América del Norte el 4 de mayo de 2004 para PlayStation 2 y Xbox.")
gameHandler.newGame("Black","2006",85.00,"Disparos","Acción","Guerra","https://images-na.ssl-images-amazon.com/images/I/613W2Z8A74L._AC_SY445_.jpg","https://i.ytimg.com/vi/vHeV7i4IgZ8/maxresdefault.jpg","Black es un videojuego de acción en primera persona desarrollado por Criterion Games y publicado por Electronic Arts. Es considerado una obra de culto debido a su nivel de calidad en gráficos y jugabilidad para su época.")
gameHandler.newGame("Fornite: Revolved","2020",275.00,"Acción","Aventura","Primera persona","https://image.api.playstation.com/vulcan/img/rnd/202008/2621/gq2XHV05RkLllSF8J2oU9OXh.png","https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2020/08/como-descargar-fortnite-movil-2020-2039729.jpg?itok=bWnIS9Sp","Fortnite es un videojuego del año 2017 desarrollado por la empresa Epic Games, lanzado como diferentes paquetes de software que presentan diferentes modos de juego, pero que comparten el mismo motor de juego y mecánicas. Fue anunciado en los Spike Video Game Awards en 2011")
# Creando una instancia de la clase comentarios
commentHandler = Comments_DAO()

@app.route('/')
def main():
    return '<h1>Hola, me llamo Eduardo 😋</h1>'

@app.route('/newUser',methods=['POST'])
def new_user():
    response = {}
    name = request.json['name']
    last_name = request.json['last_name']
    user_name = request.json['user_name']
    password = request.json['password']
    user_type = request.json['user_type']
    print("Intentanto crear para:" + str(user_name))
    if(userHandler.newUser(name,last_name,user_name,password,user_type)):
        response = {
            "state": "ok",
            "message": "El usuario ha sido creado con éxito"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "El nombre de usuario ya esta en uso"
        }
        return response

@app.route('/getPassword',methods=['POST'])
def get_password():
    response = {}
    user_name = request.json['user_name']
    if(userHandler.getPassword(user_name) == False):
        response = {
            "state": "error",
            "message": "El usuario no existe"
        }
        return response
    response = {
        "state": "ok",
        "message": "La contraseña es: " + str(userHandler.getPassword(user_name))
    }
    return response
    
@app.route('/login',methods=['POST'])
def login():
    response = {}
    user_name = request.json['user_name']
    password = request.json['password']
    if(userHandler.login(user_name,password)):
        
        response = {
            "state": "ok",
            "message": "Bienvenido " + str(user_name),
            "userRole": str(userHandler.getUserRole(user_name))
        }
        return response
    response = {
        "state": "error",
        "message": "El usuario no existe o verificar tu usuario y contraseña"
    }
    return response

# Rutas de Videjuegos -----------------
# Crear videojuego
@app.route('/newVideoGame',methods=['POST'])
def createVideoGame():
    response = {}
    name = request.json['name']
    year = request.json['year']
    price = request.json['price']
    category1 = request.json['category1']
    category2 = request.json['category2']
    category3 = request.json['category3']
    picture = request.json['picture']
    banner = request.json['banner']
    description = request.json['description']    
    if(gameHandler.newGame(name,year,price,category1,category2,category3,picture,banner,description)):
        response = {
            "state": "ok",
            "message": "Videojuego ingresado correctamente"
        }
        return response
    response = {
        "state": "error",
        "message": "El videojuego ya existe"
    }
    return response
    
# Elminar videojuego
@app.route('/deleteVideoGame',methods=['POST'])
def deleteVideoGame():
    response = {}
    name = request.json['name']
    gameHandler.printGames()
    if(gameHandler.deleteGame(name)):
        response = {
            "state": "ok",
            "message": "Videojuego eliminado correctamente"
        }
        return response
    response = {
        "state": "error",
        "message": "No existe el videojuego"
    }
    return response
    
# Obtener videoJuegos
@app.route('/getVideoGames',methods=['GET'])
def getVideoGames():
    return  gameHandler.getGames()
    
# Obtener información de videoJuego
@app.route('/videoGameView',methods=['GET'])
def getVideoGameByName():
    response = {}
    name = request.args.get("name", None)
    game_response = gameHandler.getGameByName(name)
    if (game_response != False):
        response = {
            "name": str(game_response.name),
            "description": str(game_response.description),
            "price": str(game_response.price),
            "category1": str(game_response.category1),
            "category2": str(game_response.category2),
            "category3": str(game_response.category3),
            "picture": str(game_response.picture),
            "banner": str(game_response.banner)
        }
        return  response
    response = {
        "state": "error",
    }
    return  response
# Crear comentario
@app.route('/newComment',methods=['POST'])
def newComment():
    response = {}
    userName = request.json['userName']
    gameName = request.json['gameName']
    description = request.json['description']
    if(commentHandler.newComent(gameName,userName,description)):
        response = {
            "state": "ok",
            "message": "Comentario ingresado"
        }
        return response
    response = {
        "state": "error",
        "message": "Ocurrio un error"
    }
    return response
# Obtener comentarios de videoJuego
@app.route('/getComments',methods=['POST'])
def getCommentsByGame():
    game = request.json['game']
    return  commentHandler.getCommentsByGame(game)

# Obtener resultados de búsqueda
@app.route('/getCategoryResult',methods=['POST'])
def getCategoryResult():
    category = request.json['category']
    return  gameHandler.getGamesByCategory(category)

    

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)