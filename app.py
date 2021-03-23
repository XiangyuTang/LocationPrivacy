from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")
@app.route('/index')
def index1():
	return render_template("index.html")

@app.route('/404')
def html_404():
	return render_template("404.html")

@app.route('/docs')
def doc():
	return render_template("docs.html")

@app.route('/account')
def account():
	return render_template("account.html")

@app.route('/charts')
def charts():
	return render_template("charts.html")

@app.route('/help')
def help():
	return render_template("help.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/notifications')
def notifications():
	return render_template("notifications.html")

@app.route('/orders')
def orders():
	return render_template("orders.html")

@app.route('/reset_password')
def reset_password():
	return render_template("reset-password.html")

@app.route('/settings')
def settings():
	return render_template("settings.html")

@app.route('/signup')
def signup():
	return render_template("signup.html")

#
# @app.route('/movie')
# def movie():
# 	datalist = []
# 	conn = sqlite3.connect("movie.db")
# 	cur = conn.cursor()
# 	sql = "select * from movie250"
# 	data = cur.execute(sql)
# 	for item in data:
# 		datalist.append(item)
# 	cur.close()
# 	conn.close()
# 	return render_template("movie.html",datalist = datalist)
# @app.route('/team')
# def team():
# 	return render_template("team.html")
# @app.route('/word')
# def word():
# 	return render_template("word.html")
# @app.route('/score')
# def score():
# 	score = [] #评分多少种，echarts的x坐标
# 	movie_num = [] #电影多少个，echarts的y坐标
# 	conn = sqlite3.connect("movie.db")
# 	cur = conn.cursor()
# 	sql = "select score,count(score) from movie250 group by score"
# 	data = cur.execute(sql)
# 	for item in data:
# 		score.append(item[0])
# 		movie_num.append(item[1])
# 	cur.close()
# 	conn.close()
# 	return render_template("score.html",score = score,movie_num=movie_num)

if __name__ == '__main__':
	app.run(debug=True)
