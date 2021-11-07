from flask.wrappers import Request
from werkzeug.wrappers import request
from app import app
from flask import render_template, request
from models.player import Player
from models.game import Game


@app.route('/')
def splash():
    return render_template("splash.html", title="Rock, Paper, Scissors")
    
@app.route('/home')
def home():
    return render_template("game.html", title="Let's Play")
    
@app.route('/rules')
def rules():
    return render_template("rules.html", title="Rules")
    
@app.route('/result', methods=['POST'])
def play():
    winner = None
    choice_1 = request.form['player_1_choice']
    choice_2 = request.form['player_2_choice']
    name_1 = request.form['player_1_name']
    name_2 = request.form['player_2_name']
    
    player_1 = Player(name_1, choice_1)
    player_2 = Player(name_2, choice_2)
    
    game = Game()
    
    winner = game.play(player_1, player_2)
    
    return render_template("result.html", winner=winner, title="Results")