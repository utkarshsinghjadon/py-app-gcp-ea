# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
# from flask import Flask
import wikipedia
import os
import datetime
import smtplib, ssl
import requests
from flask import Flask, request, json, redirect, url_for, render_template, make_response, session, escape
from firebase import firebase
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
app.secret_key = 'hehhhnn'

receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')

# def wishMe():
    
#     speak("I'm Archi. You must be Utkarsh Singh Jadon. Please tell me how may I help you?")

@app.route('/fire')
def fire():
    firebaseApp = firebase.FirebaseApplication('https://console-elite-default-rtdb.firebaseio.com/', None)
    result = firebaseApp.get('/users', None)
    return result
@app.route('/forms/')
def FormResponses():
     r = requests.get('https://eliteacademy.co.in/')
     link_status_code = r.status_code
     return link_status_code
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
	hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return("Morno!")
    elif hour>=12 and hour<18:
        return("Afternoon!") 
    else:
        return("Evening")
    return Wishing
    return 'Hello World!'+ Wishing

@app.route('/bot', methods=['POST'])
def on_event():
  """Handles an event from Google Chat."""
  event = request.get_json()
  if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
    text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
  elif event['type'] == 'MESSAGE':
    text = 'You said: `%s`' % event['message']['text']
  else:
    return
  return json.jsonify({'text': text})


@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/hello/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/hello/python/')
def hello_python():
   return 'Hello Python'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/seename',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/')
def index():
     if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + render_template('login.html') + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
     return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"
    # return render_template('login.html')
#    return '<html><body><h1>Hello World</h1></body></html>' or/ another method

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
   return render_template('score.html', marks = score)

@app.route('/result')
def result():
   dict = {'physix':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/result',methods = ['POST', 'GET'])
def resultform():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    userg = request.form['uid']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', userg)
   
   return resp 

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

@app.route('/login', methods = ['GET', 'POST'])
def reallogin():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
	
   '''

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
