from flask import Flask, render_template, request, flash


def load(app: Flask) -> Flask:  
    @app.route("/says")
    def says():
        phrase = '''Silvio Santos Ipsum Eu só acreditoammmm.... Vendoammmm. Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma
    você vai gerar textuans ha haae. Ma vai pra lá. É por sua conta e riscoamm? É bom ou não éam? É fácil ou não éam? É
    dinheiro ou não éam?

    Boca sujuam... sem vergonhuamm. Mah é a porta da esperançaam. É por sua conta e riscoamm? Um, dois três, quatro,
    PIM, entendeuam? Eu só acreditoammmm.... Vendoammmm. Ma! Ao adquirir o carnê do Baú, você estará concorrendo a um
    prêmio de cem mil reaisam.

    O arriscam tuduam, valendo um milhão de reaisuam. Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você
    vai gerar textuans ha haae. Patríciaaammmm... Luiz Ricardouaaammmmmm. Valendo um milhão de reaisammm. Eu não queria
    perguntar isso publicamente, ma vou perguntar. Carla, você tem o ensino fundamentauam? É fácil ou não éam?

    É bom ou não éam? É com você Lombardiam. O arriscam tuduam, valendo um milhão de reaisuam. Qual é a musicamm? Mah é
    a porta da esperançaam. É por sua conta e riscoamm?

    O Raul Gil é gayam! ... Maa O Ah Ae! Ih Ih! O Raul Gil é gayamm! Ha hai. Bem boladoam, bem boladoam. Bem gozadoam.
    Mah você mora com o papai ou com a mamãem? Boca sujuam... sem vergonhuamm. Estamos em ritmo de festamm. Ha haeeee.
    Hi hi.'''
        word_list = ["Python", "C#", "Javascript", "Java", "Elixir", "Lua", "PHP", "Kotlin"]

        return render_template("says.html", phrase=phrase, word_list=word_list)
    
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        contact = ''

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            contact= f"{name} + {email}"
   
            flash("Logado com sucesso!", 'success')

        return render_template("login.html", contact=contact)

    return app