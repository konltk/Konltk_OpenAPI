#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request
import konlp.asp.asp as A
import json
from flask_jsonpify import jsonify
import konlp.tokenizer.wordcount as wc

app = Flask(__name__)

@app.route('/success/autospacing/<text>')
def success1(text):
       q = A.KltAsp()
       q.dic_init('/usr/local/asp_dic')
       print("------------------" + text.encode('utf8'))
       str_ = q.asp(text.encode("utf8"))
     #  return(str_)
       it= json.dumps(str_, ensure_ascii=False, encoding ='utf-8') 
       return it

@app.route('/success/wordcounting/<text>')
def success2(text):
       q1 = wc.WordCount()
       str_1 = q1.wordcount(text.encode('utf8'))
      # return "%s" %str_1
       it1 = json.dumps(str_1, ensure_ascii=False, encoding='utf-8')
       return it1

@app.route('/nltk/autospacing',methods = ['POST','GET'])
def get_text1():
       if request.method=='POST':
             user = request.form['space']
             return redirect(url_for('success1', text = user))
       else :
             user = request.args.get('space')
             return redirect(url_for('success1',text= user))
@app.route('/nltk/wordcounting', methods = ['POST'])
def get_text2():
       if request.method == 'POST':
             user = request.form['count']
             return redirect(url_for('success2' , text = user))
if __name__ == '__main__' :
       app.run(host='0.0.0.0', debug=True)
