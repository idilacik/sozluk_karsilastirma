from flask import Flask, render_template, request
import sozlukler
from itertools import zip_longest

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/result', methods=['POST',"GET"])
def result():
    output = request.form
    kelime = output["girilen"].lower()
    tdkAnlamlar = sozlukler.tdkSozluk(kelime)
    kubbealtiAnlamlar = sozlukler.kubbealtiSozluk(kelime)
    anlamlar = list(zip_longest(tdkAnlamlar, kubbealtiAnlamlar, fillvalue=""))

    return render_template("index.html", sonuc = kelime, anlamlar=anlamlar,)

if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)
