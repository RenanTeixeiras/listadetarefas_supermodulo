from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/inicio', methods=['GET','POST'])
def inicio():
    if request.method == "POST":
        nomeNoPython = request.form.get('nomeUsuario').upper()
        return render_template('index.html', nomeHTML=nomeNoPython)
    else:
        return render_template('index.html')

usuarios = [{'nome': 'Renan', 'email':'renan@email.com','idade':'23'},
            {'nome':'Vinicius','email':'vinicius@email.com','idade':'28'},
            {'nome':'Miguel','email':'miguel@email.com','idade':'14'},
            {'nome':'Jayme','email':'jayme@email.com','idade':'22'},
            ]
            
@app.route('/v1/user/idade/<nome>')
def index(nome: str):
    idade = []
    for usuario in usuarios:
        if nome == usuario['nome']:
            idade.append(usuario['idade'])
        else:
            continue
    if len(idade) == 0:
        return 'Usuario não encontrado' 
    else:
        return f'Idade: {idade[0]}'


if __name__ == "__main__":
    app.run(debug=True)