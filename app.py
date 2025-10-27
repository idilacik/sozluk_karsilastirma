from flask import Flask, render_template, request
import sozlukler
from sozlukler import kubbealtiSozluk

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ =="_main_":
    app.run(host='0.0.0.0', debug=True)
@app.route('/result', methods=['POST',"GET"])

def result():
    output = request.form
    kelime = output["girilen"].lower()
    tdkAnlamlar = sozlukler.tdkSozluk(kelime)
    kubbealtiAnlamlar = sozlukler.kubbealtiSozluk(kelime)
    from itertools import zip_longest
    anlamlar = list(zip_longest(tdkAnlamlar, kubbealtiAnlamlar, fillvalue=""))




    return render_template("index.html", sonuc = kelime, anlamlar=anlamlar,)