
from flask import Flask, redirect,render_template,request

from bs4 import BeautifulSoup
import requests

def htmlDe(url):
    data=requests.get(url)
    htmlContent=data.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    return(soup)
    # return(soup.prettify())

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    yourTag=''
    if request.method=='POST':
        link=request.form['link']
        tag=request.form['tag']
        try:
            if tag:
                stuff=htmlDe(link)
                yourTag=stuff.find_all(tag)
            else:
                yourTag=htmlDe(link).prettify()
        except:
            return redirect('/')
        # else:return redirect('/')
            

    return render_template('index.html',toscrape=yourTag)





if __name__=='__main__':
    app.run(debug=True)
