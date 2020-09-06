from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from requests import get

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/info")
def info():
    username = request.args.get("username")
    if not username:
        return "not username"
    soup = BeautifulSoup(get(f"https://rubika.ir/{username}").text, "html.parser")
    name = soup.find("div", attrs={"class": "rlp-content-caption-wrap"}).text.strip()
    image = soup.find("img", attrs={"class": "profile-img"})['src']
    bio = soup.find("span", attrs={"class": "rlp-content-info"}).text
    fallow = soup.find("span", attrs={"class": "rlp-content-peer number-persian"}).text    
    return render_template('info.html',soup=soup,name=name,img=image,bio=bio,fallow=fallow)



app.run(debug=True)