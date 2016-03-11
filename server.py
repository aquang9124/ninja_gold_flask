from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsaSecretAssKey"

@app.route('/')
def index():
	if "money" in session:
		cat = "dog"
	else:
		session["money"] = 0
	if "activities" in session:
		cat = "cat"
	else:
		session['activities'] = []
	if "losses" in session:
		cat = "mouse"
	else:
		session['losses'] = []
	return render_template('index.html', money=session['money'], activities=session['activities'], losses=session['losses'])
@app.route('/gold', methods=['POST'])
def make_gold():
	farm_gold = random.randrange(10, 21)
	cave_gold = random.randrange(5, 11)
	house_gold = random.randrange(2, 6)
	casino_gold = random.randrange(0, 51)
	luck = random.randrange(0, 11)
	if request.form['building'] == 'farm':
		session['money'] += farm_gold
		session['activities'].append("You farmed and made %s golds!" % str(farm_gold))
	if request.form['building'] == 'cave':
		session['money'] += cave_gold
		session['activities'].append("You explored a cave and made %s golds!" % str(cave_gold))
	if request.form['building'] == 'house':
		session['money'] += house_gold
		session['activities'].append("You robbed a house and made %s golds!" % str(house_gold))
	if request.form['building'] == 'casino':
		if luck > 7:
			session['money'] += casino_gold
			session['activities'].append("You went to a casino and made %s golds!" % str(casino_gold))
		else:
			session['money'] -= casino_gold
			session['losses'].append("You went to a casino and lost %s golds!" % str(casino_gold))
	return redirect('/')
@app.route('/reset', methods=['POST'])
def reset_game():
	session.clear()
	return redirect('/')
app.run(debug=True)