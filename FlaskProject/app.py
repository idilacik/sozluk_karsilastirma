from flask import Flask, render_template, request
import sozlukler
from sozlukler import kubbealtiSozluk

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/result', methods=['POST',"GET"])
def result():
    output = request.form
    kelime = output["girilen"]
    tdkAnlamlar = sozlukler.tdkSozluk(kelime)
    kubbealtiAnlamlar = sozlukler.kubbealtiSozluk(kelime)
    from itertools import zip_longest
    anlamlar = list(zip_longest(tdkAnlamlar, kubbealtiAnlamlar, fillvalue=""))

    #kubbealtiAnlamlar = sozlukler.kubbealtiSozluk(kelime)
    #, kubbealtiAnlamlar = kubbealtiAnlamlar, lenkubbe = len(kubbealtiAnlamlar)



    return render_template("index.html", sonuc = kelime, anlamlar=anlamlar,)