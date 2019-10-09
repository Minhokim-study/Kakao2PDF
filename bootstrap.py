#-*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app) #요렇게 해줘야 적용된다.

@app.route('/bootstrap') #접속할 URL
def bootstrap():
	return render_template('bootstrap.html') #예제 템플릿

if __name__ == '__main__':
	app.run(host='0.0.0.0', port="1010", debug=True)