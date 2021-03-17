from flask import Flask, Blueprint, request, render_template, jsonify
import sqlite3


user = Blueprint('user', __name__, url_prefix='/' )

@user.route('/signUp' , methods= ['GET' , 'POST'])
def index():

    # Creating a link with the DB 
    connect = sqlite3.connect('prova')
    cur = connect.cursor()
    

    if request.method == 'POST':
        # Getting all the data form the SignUp Form 
        username = request.get_json(force=True, silent=True).get('username', None)
        firstname = request.get_json(force=True, silent=True).get('firstname', None)
        surname = request.get_json(force=True, silent=True).get('surname', None)
        email = request.get_json(force=True, silent=True).get('email', None)
        pass1 = request.get_json(force=True, silent=True).get('pass1', None)
        pass2 = request.get_json(force=True, silent=True).get('pass2', None)
        
        #Checking the password equality
        if len(pass1) > 6 and len(pass2) > 6:
            if pass1 != pass2:
                return jsonify({'status' : 'error', 'message' : "password don't match"})
        else:
            return jsonify({'status' : 'error', 'message' : 'Password too short'})


        # Checking username originality
        queryCheck = f"SELECT username FROM prova WHERE username = '{username}'"
        
        cur.execute(queryCheck)
        result = cur.fetchall()

        if result.count() == 0:
            # Username is not present
            pass
        
        

        connect.commit() # Save changes
        connect.close() 



        #funzione che crea nuovo utente: addUser()
        #return jsonify({'status' : 'success' , 'utente_creato' : '<tutti i dati dell utente creato>' })
    else:
        return jsonify({'status' : 'fail' , 'message' : 'metodo_url non valido'})

    """
    if request.method == 'GET':
        if not request.args:
            return jsonify({'status' : 'fail' , 'message' : 'api_get_all_users'})
        elif len(request.args)==1 and request.args['id']:
            return jsonify({'status' : 'request' , 'message' : f"api_get_user_{request.args['id']}"})
        else:
            return jsonify({'status' : 'error' , 'message' : 'bad_request'})
    """



@user.route("/user")
def user_function():
    return "todo"






