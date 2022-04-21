from funcoes import knapSack, mudarValoresKnapSack, Graphico, vetorPontosTuristicos, mudarValoresArestas
from cgitb import html
from webbrowser import get
from flask import Flask, render_template, request, flash, redirect, url_for
import random


# -- Estruturas---


adj_list = {
    "1": ["2", "7", "8"],
    "2": ["7", "1", "8"],
    "3": ["7"],
    "4": ["6", "8"],
    "5": ["5", "10"],
    "6": ["4", "5"],
    "7": ["1", "3", "4"],
    "8": ["1", "4", "9"],
    "9": ["8"],
    "10": ["5"],

}
# ---  Variaveis Globais ---
global val
val = [1, 6, 18, 22, 26]
global wt
wt = [1, 2, 5, 6, 7]
global W
W = 11
global n
n = len(val)
global aresta1
global aresta2
global aresta3
global aresta4
global aresta5
global aresta6
global aresta7
global aresta8
global aresta9
global aresta10
global aresta11
global aresta12
global aresta13
global aresta14
global aresta15
global aresta16
global aresta17
global aresta18
global aresta19
aresta1 = 37
aresta2 = 20
aresta3 = 12
aresta4 = 13
aresta5 = 9
aresta6 = 40
aresta7 = 36
aresta8 = 2
aresta9 = 51
aresta10 = 4
aresta11 = 28
aresta12 = 29
aresta13 = 45
aresta14 = 52
aresta15 = 27
aresta16 = 6
aresta17 = 18
aresta18 = 25
aresta19 = 33

# --- Aplicacao ---

app = Flask(__name__)  # sempre ao iniciar um site
app.config['SECRET_KEY'] = "minha-palavra-secreta"

# criar a primeira página do site
# route -> caminho que vem depois do dominio

# funcao -> o que quero exibir naquela página
# template


@app.route('/', methods=['GET', 'POST'])
def homepage():
    no = "1"
    if request.method == "GET":
        return render_template("homepage.html", no=no)

    else:

        palpite = str(request.form.get("name"))

        if (palpite in adj_list[no]):
            no = palpite
            return redirect(url_for('knapsack', no_destino=no))
        else:
            return redirect(url_for('errou'))


@app.route('/knapsack/<no_destino>', methods=['GET', 'POST'])
def knapsack(no_destino):
    no = no_destino
    global val
    global wt
    global W
    global n
    resposta = knapSack(W, wt, val, n)
    if request.method == "GET":
        return render_template("knapsack.html", no=no,
                               valor0=val[0], peso0=wt[0],
                               valor1=val[1], peso1=wt[1],
                               valor2=val[2], peso2=wt[2],
                               valor3=val[3], peso3=wt[3],
                               valor4=val[4], peso4=wt[4],
                               resposta=resposta, peso=W
                               )

    else:
        try:
            valor = int(request.form.get("valor"))
            if(valor == resposta):
                flash("Resposta Certa!", "success")
                return redirect(url_for('knapsack', no_destino=no))
            if(valor != resposta):
                flash("Resposta errada! Tente de Novo!", "warning")
                return redirect(url_for('knapsack', no_destino=no))
        except:
            palpite = str(request.form.get("name"))
            if (palpite == "10" and palpite in adj_list[no]):
                return redirect(url_for('vitoria'))
            if (palpite in adj_list[no]):
                no = palpite
                W, wt, val, n = mudarValoresKnapSack(W, wt, val, n)
                return redirect(url_for('knapsack', no_destino=no))
            else:
                return redirect(url_for('errou'))


@app.route('/prim/<no_destino>', methods=['GET', 'POST'])
def prim(no_destino):
    no = no_destino
    global aresta1
    global aresta2
    global aresta3
    global aresta4
    global aresta5
    global aresta6
    global aresta7
    global aresta8
    global aresta9
    global aresta10
    global aresta11
    global aresta12
    global aresta13
    global aresta14
    global aresta15
    global aresta16
    global aresta17
    global aresta18
    global aresta19
    g = Graphico(10)
    g.graph = [[0, aresta1, aresta2, 0, 0, 0, 0, aresta3, 0, 0],
               [aresta1, 0, aresta4, aresta5, 0, 0, 0, 0, 0, 0],
               [aresta2, aresta4, 0, aresta14, 0, 0, 0, aresta19, 0, 0],
               [0, aresta5, aresta6, 0, aresta7, aresta8, 0, 0, 0, 0],
               [0, 0, aresta14, aresta7, 0, aresta9,
                   aresta10, aresta12, aresta13, 0],
               [0, 0, 0, aresta8, aresta9, 0, aresta11, 0, 0, 0],
               [0, 0, 0, 0, aresta10, aresta11, 0, aresta15, aresta16, 0],
               [aresta3, 0, aresta19, 0, aresta15,
                   0, aresta17, 0, aresta16, 0],
               [0, 0, 0, 0, aresta13, 0, aresta16, aresta17, 0, aresta18],
               [0, 0, 0, 0, 0, 0, 0, 0, aresta18, 0], ]
    resultado = g.primMST()
    total = g.primMST1()
    if request.method == "GET":
        return render_template("prim.html", no=no, aresta1=aresta1,
                               aresta2=aresta2,
                               aresta3=aresta3,
                               aresta4=aresta4,
                               aresta5=aresta5,
                               aresta6=aresta6,
                               aresta7=aresta7,
                               aresta8=aresta8,
                               aresta9=aresta9,
                               aresta10=aresta10,
                               aresta11=aresta11,
                               aresta12=aresta12,
                               aresta13=aresta13,
                               aresta14=aresta14,
                               aresta15=aresta15,
                               aresta16=aresta16,
                               aresta17=aresta17,
                               aresta18=aresta18,
                               aresta19=aresta19,
                               resultado=resultado,
                               total=total)
    else:
        try:
            valor = int(request.form.get("valor"))
            if(valor == total):
                flash("Resposta Certa!", "success")
                return redirect(url_for('prim', no_destino=no))
            if(valor != total):
                flash("Resposta errada! Tente de Novo!", "warning")
                return f"{valor} {total}"
        except:
            palpite = str(request.form.get("name"))
            if (palpite == "10" and palpite in adj_list[no]):
                return redirect(url_for('vitoria'))
            if (palpite in adj_list[no]):
                no = palpite
                aresta1, aresta2, aresta3, aresta4, aresta5, aresta6, aresta7, aresta8, aresta9, aresta10, aresta11, aresta12, aresta13, aresta14, aresta15, aresta16, aresta17, aresta18, aresta19 = mudarValoresArestas()
                return redirect(url_for('prim', no_destino=no))
            else:
                return redirect(url_for('errou'))


@app.route('/errou', methods=['GET', 'POST'])
def errou():
    return render_template("errou.html")


@app.route('/vitoria', methods=['GET', 'POST'])
def vitoria():
    return render_template("vitoria.html")


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
