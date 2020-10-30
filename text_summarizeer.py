from flask import Flask, render_template,request,redirect,url_for
from googlesearch import search
import flask
import json
from flask import Response
app = Flask(__name__,template_folder='template')
def search_web(query):
    res=[]
    for j in search(query, num=10, stop=10, pause=2): 
        res.append(j)
    type(res)
    return res

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/search',methods=['POST','GET'])
def searchFun():
    if request.method=='POST':
        res=search_web(request.form['search_ip'])
        return render_template('search.html',flag=True,result=res) 
    
    return render_template('search.html') 


@app.route('/summarizer',methods=['POST','GET'])
def summ():
    if request.method=='POST':
        return render_template('formPage.html',data=request.form['input'],flag=True)
    
    return render_template('formPage.html')



@app.route('/test',methods=['GET'])
def test():
    ''' 
    GET: Receives the request in /test route and returns a response containing {"response": "test"}
    '''
    resp = Response(response=json.dumps({"response": "test"}), status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(debug = True)
 