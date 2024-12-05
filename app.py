from flask import Flask, render_template, url_for, request, redirect, flash
from sqlalchemy import select
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'


@app.route("/")
def index():
    return render_template("pagina_inicial.html")


# @app.route('/veterinarios', methods=['GET'])
# def veterinarios():
#     sql_veterinarios = select(criar_veterinario)
#     resultado_veterinarios = db_sesion.execute(sql_veterinarios).scalars()
#     lista_veterinarios = []
#     for x in resultado_veterinarios:
#         lista_veterinarios.append(x.serialize_user())
#         print(lista_veterinarios[-1])
#     return render_template("lista_veterinarios.html",
#                            veterinarios_banco=lista_veterinarios)
# @app.route('/novo_veterinario', methods=["POST", "GET"])
# def criar_veterinario():
#     if request.method == "POST":
#         if not request.form["form_nome"]:
#             flash("Preencher o nome completo", "error")
#
#         if not request.form["form_crmv"]:
#             flash("Preencher o CRMV", "error")
#
#         if not request.form["form_data_emissao"]:
#             flash("Preencher a data de emissão", "error")
#
#         if not request.form["form_telefone"]:
#             flash("Preencher o telefone", "error")
#
#         if not request.form["form_endereco"]:
#             flash("Preencher o endereço", "error")
#
#         if not request.form["form_salario"]:
#             flash("Preencher o salário do veterinário", "error")
#
#         if not request.form["form_cpf"]:
#             flash("Preencher o CPF", "error")
#
#         else:
#             form_criar = Veterinario(nome=request.form.get('form_nome'),
#                                 CRMV=request.form.get('form_crmv'),
#                                 data_de_emissao=request.form.get('form_data_emissao'),
#                                 telefone=request.form.get('form_telefone'),
#                                 endereco=request.form.get('form_endereco'),
#                                 salario=request.form.get('form_salario'),
#                                 cpf=request.form.get('form_cpf')
#                                 )
#             form_criar.save()
#             db_sesion.close()
#             flash("Evento criado!!", "success")
#
#             return redirect(url_for('veterinarios'))
#
#     return render_template('novo_veterinario.html')

@app.route('/consultas', methods=['GET'])
def consultas():
    sql_consultas = (select(Consulta, Animal, Veterinario)
                     .join(Animal, Consulta.idAnimal1 == Animal.id)
                     .join(Veterinario, Consulta.idVeterinario1 == Veterinario.id))

    resultado_consultas = db_sesion.execute(sql_consultas).scalars().all()
    print(resultado_consultas)
    return render_template('lista_consulta.html',
                           consultas_banco=resultado_consultas)


@app.route('/nova_consulta', methods=["POST", "GET"])
def criar_consulta():
    if request.method == "POST":

        if not request.form['form_dia'] or not request.form['form_ano_horario'] or not request.form[
            'form_minuto'] or not request.form['form_motivo'] or not request.form['form_animal_id'] or not request.form[
            'form_veterinario_id']:
            flash("Preencher os campos em branco!!", "error")

        else:
            form_criar = Consulta(data1=request.form.get('form_dia'),
                                  hora1=int(request.form.get('form_horario')),
                                  minuto=int(request.form.get('form_minuto')),
                                  motivo_id1=int(request.form.get('form_motivo')),
                                  idAnimal1=int(request.form.get('form_animal_id')),
                                  idVeterinario1=int(request.form.get('form_veterinario_id')),
                                  )
            form_criar.save()
            db_sesion.close()
            flash("Evento criado!!", "success")

            return redirect(url_for('consultas'))

    return render_template('nova_consulta.html')


# @app.route('/clientes', methods=['GET'])
# def clientes():
#     sql_clientes = select(Cliente, Animal).join(Animal, Cliente.animal_id == Animal.id)
#     resultado_clientes = db_sesion.execute(sql_clientes).fetchall()
#     print(resultado_clientes)
#     return render_template('lista_clientes.html',
#                           clientes_banco=resultado_clientes)
# @app.route('/novo_cliente', methods=["POST", "GET"])
# def criar_cliente():
#     if request.method == "POST":
#         if not request.form["form_nome"]:
#             flash("Preencher o nome completo", "error")
#
#         if not request.form["form_telefone"]:
#             flash("Preencher o telefone", "error")
#
#         if not request.form["form_cpf"]:
#             flash("Preencher o CPF", "error")
#
#         if not request.form["form_endereco"]:
#             flash("Preencher o endereço", "error")
#
#         if not request.form["form_animal_id"]:
#             flash("Preencher o Id do animal", "error")
#         else:
#             form_criar = Veterinario(nome=request.form.get('form_nome'),
#                                 telefone=request.form.get('form_telefone'),
#                                 endereco=request.form.get('form_endereco'),
#                                 animal_id=request.form.get('form_animal_id'),
#                                 cpf=request.form.get('form_cpf')
#                                 )
#             form_criar.save()
#             db_sesion.close()
#             flash("Evento criado!!", "success")
#
#             return redirect(url_for('clientes'))
#
#     return render_template('novo_cliente.html')

@app.route('/animais', methods=['GET'])
def animais():
    sql_animais = select(Animal).select_from(Animal)
    resultado_animais = db_sesion.execute(sql_animais).scalars()
    lista_animais = []
    for x in resultado_animais:
        lista_animais.append(x.serialize_user())
        print(lista_animais[-1])
    return render_template('lista_animais.html',
                           animais_banco=lista_animais)


@app.route('/novo_animal', methods=["POST", "GET"])
def criar_animal():
    if request.method == "POST":

        if not request.form['form_nome'] or not request.form['form_ano_nascimento'] or not request.form[
            'form_raca'] or not request.form['form_id_cliente']:
            flash("Preencher os campos em branco", "error")

        else:
            form_criar = Animal(nome_animal=request.form.get('form_nome'),
                                anoNasci3=int(request.form['form_ano_nascimento']),
                                raca3=request.form.get('form_raca'),
                                cliente_id=int(request.form.get('form_id_cliente')),
                                )
            form_criar.save()
            db_sesion.close()
            flash("Evento criado!!", "success")

            return redirect(url_for('animais'))

    return render_template('novo_animal.html')


@app.route('/motivos', methods=['GET'])
def motivos():
    sql_motivos = select(Motivo).select_from(Motivo)
    resultado_motivos = db_sesion.execute(sql_motivos).scalars()
    lista_motivos = []
    for x in resultado_motivos:
        lista_motivos.append(x.serialize_user())

    print(lista_motivos)
    return render_template("lista_motivo.html",
                           motivos_banco=lista_motivos)


@app.route('/novo_motivo', methods=["POST", "GET"])
def criar_motivo():
    if request.method == "POST":

        if not request.form['form_nome'] or not request.form['form_categoria'] or not request.form[
            'form_valor']:
            flash("Preencher os campos em branco!!", "error")

        else:
            form_criar = Motivo(nome_motivo=request.form.get('form_nome'),
                                motivo_categoria=request.form.get('form_categoria'),
                                valor_motivo=int(request.form.get('form_valor'))
                                )
            form_criar.save()
            db_sesion.close()
            flash("Evento criado!!", "success")

            return redirect(url_for('motivos'))

    return render_template('novo_motivo.html')


@app.route('/categorias', methods=['GET'])
def categorias():
    sql_categorias = select(Categoria).select_from(Categoria)
    resultado_categorias = db_sesion.execute(sql_categorias).scalars()
    lista_categorias = []
    for x in resultado_categorias:
        lista_categorias.append(x.serialize_user())
        print(lista_categorias[-1])
    return render_template("lista_categoria.html",
                           categorias_banco=lista_categorias)


@app.route('/nova_categoria', methods=["POST", "GET"])
def criar_categoria():
    if request.method == "POST":
        if not request.form["form_nome"]:
            flash("Preencher o nome da categoria", "error")
        else:
            form_criar = Categoria(nome_categoria=request.form.get('form_nome'),
                                   )
            form_criar.save()
            db_sesion.close()
            flash("Evento criado!!", "success")

            return redirect(url_for('categorias'))

    return render_template('nova_categoria.html')


if __name__ == '__main__':
    app.run(debug=True)
