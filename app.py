
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request
import nltk
#from flask.ext.jsonpify import jsonify
from success import success
  
@app.route('/nltk', methods = ['POST', 'GET'])
def nltk_text():
     #   def get(self):
         if request.method == 'POST':
                 user = request.form['tag']
                 print("post methods")
                 return redirect(url_for('success', text = user))
              #  return {'hello':'world'}
         else:
                 user = request.args.get('tag')
                 print("get methods")
                 return redirect(url_for('success', text = user))
               # return {'hello':'world'}
#api.add_resource(success,'/success/<text>')
#api.add_resource(nltk_text,'/nltk')

if __name__ == '__main__':
        app.run(host = '0.0.0.0', debug = True)
