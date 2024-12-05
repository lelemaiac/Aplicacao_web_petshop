from models import Veterinario, Animal, Consulta, Cliente, db_sesion
from sqlalchemy import select


# Inserir dados na tabela
# def inserir_veterinario():
#     veterinario = Veterinario(nome=(input('Nome completo: ')),
#                               CRMV=(input('CRMV: ')),
#                               data_de_emissao=(input('Data de emissão: ')),
#                               telefone=(int(input('Telefone: '))),
#                               endereco=(input('Endereço: ')),
#                               salario=(float(input('Salário: '))),
#                               cpf=(input('CPF: ')),
#                              )
#     print(veterinario)
#     veterinario.save()


# def consultar_veterinario():
#     var_veterinario = select(Veterinario)
#     var_veterinario = db_sesion.execute(var_veterinario).all()
#     print(var_veterinario)


# def atualizar_veterinario():
#     var_veterinario = select(Veterinario).where(Veterinario.nome == (input('Nome: ')))
#     var_veterinario = db_sesion.execute(var_veterinario).scalar()
#     print(var_veterinario)
#     var_veterinario.nome = str(input('Novo Nome: '))
#     var_veterinario.save()


# remove pessoas

# def deletar_veterinario():
#     veterinario = Veterinario.query.filter_by(nome=str(input('Nome: '))).first()
#     print(veterinario)
#     veterinario.delete()

def inserir_animal():
    animal = Animal(nome=(input('Nome: ')),
                              anoNasci3=(input('Ano de nascimento: ')),
                              raca3=(input('Raça: ')),
                                cliente_id=int(input("Id do cliente: "))
                             )
    print(animal)
    animal.save()


def consultar_animal():
    var_animal = select(Animal)
    var_animal = db_sesion.execute(var_animal).all()
    print(var_animal)


def atualizar_animal():
    var_animal = select(Animal).where(Animal.nome == (input('Nome: ')))
    var_animal = db_sesion.execute(var_animal).scalar()
    print(var_animal)
    var_animal.nome = str(input('Novo Nome: '))
    var_animal.save()


# remove pessoas

def deletar_animal():
    animal = Animal.query.filter_by(nome=str(input('Nome: '))).first()
    print(animal)
    animal.delete()

# def inserir_cliente():
#     cliente = Cliente(nome=(input('Nome completo: ')),
#                               telefone=(int(input('Telefone: '))),
#                               endereco=(input('Endereço: ')),
#                               cpf=(input('Email: ')),
#                                 animal_id=(int(input('Id do Animal: '))),
#                              )
#     print(cliente)
#     cliente.save()


# def consultar_cliente():
#     var_cliente = select(Cliente)
#     var_cliente = db_sesion.execute(var_cliente).all()
#     print(var_cliente)


# def atualizar_cliente():
#     var_cliente = select(Cliente).where(Cliente.nome == (input('Nome: ')))
#     var_cliente = db_sesion.execute(var_cliente).scalar()
#     print(var_cliente)
#     var_cliente.nome = str(input('Novo Nome: '))
#     var_cliente.save()


# remove pessoas

# def deletar_cliente():
#     cliente = Cliente.query.filter_by(nome=str(input('Nome: '))).first()
#     print(cliente)
#     cliente.delete()

def inserir_consulta():
    consulta = Consulta(data1=(input('Dia: ')),
                              hora1=(input('Horário: ')),
                              motivo_id1=(input('Motivo: ')),
                                idAnimal1=(int(input('Id do Animal: '))),
                                idVeterinario1=(int(input('Id do Veterinário: '))),
                             )
    print(consulta)
    consulta.save()


def consultar_consulta():
    var_consulta = select(Consulta)
    var_consulta = db_sesion.execute(var_consulta).all()
    print(var_consulta)


def atualizar_consulta():
    var_consulta = select(Consulta).where(Consulta.nome == (input('Nome: ')))
    var_consulta = db_sesion.execute(var_consulta).scalar()
    print(var_consulta)
    var_consulta.nome = str(input('Novo Nome: '))
    var_consulta.save()


# remove pessoas

def deletar_consulta():
    consulta = Consulta.query.filter_by(nome=str(input('Nome: '))).first()
    print(consulta)
    consulta.delete()

def inserir_motivo():
    motivo = Motivo(data1=(input('Dia: ')),
                              hora1=(input('Horário: ')),
                              motivo_id1=(input('Motivo: ')),
                                idAnimal1=(int(input('Id do Animal: '))),
                                idVeterinario1=(int(input('Id do Veterinário: '))),
                             )
    print(motivo)
    motivo.save()


def consultar_motivo():
    var_motivo = select(Motivo)
    var_motivo = db_sesion.execute(var_motivo).all()
    print(var_motivo)


def atualizar_motivo():
    var_motivo = select(Motivo).where(Motivo.nome == (input('Nome: ')))
    var_motivo = db_sesion.execute(var_motivo).scalar()
    print(var_motivo)
    var_motivo.nome = str(input('Novo Nome: '))
    var_motivo.save()


# remove pessoas

def deletar_motivo():
    motivo = Motivo.query.filter_by(nome=str(input('Nome: '))).first()
    print(motivo)
    motivo.delete()

def inserir_categoria():
    categoria = Categoria(nome_categoria=(input('Nome da categoria: ')),
                             )
    print(categoria)
    categoria.save()


def consultar_categoria():
    var_categoria = select(Categoria)
    var_categoria = db_sesion.execute(var_categoria).all()
    print(var_categoria)


def atualizar_categoria():
    var_categoria = select(Categoria).where(Categoria.nome == (input('Nome: ')))
    var_categoria = db_sesion.execute(var_categoria).scalar()
    print(var_categoria)
    var_categoria.nome = str(input('Novo Nome: '))
    var_categoria.save()


# remove pessoas

def deletar_categoria():
    categoria = Categoria.query.filter_by(nome=str(input('Nome: '))).first()
    print(categoria)
    categoria.delete()

if __name__ == '__main__':

    while True:
        print('Menu')
        print('1- Inserir Categoria')
        print('2- Consultar Categoria')
        print('3- Atualizar Categoria')
        print('4- Deletar Categoria')
        print("")
        print('5- Inserir Animal')
        print('6- Consultar Animal')
        print('7- Atualizar Animal')
        print('8- Deletar Animal')
        print("")
        print('9- Inserir Consulta')
        print('10- Consultar Consulta')
        print('11- Atualizar Consulta')
        print('12- Deletar Consulta')
        print("")
        print('13- Inserir Motivo')
        print('14- Consultar Motivo')
        print('15- Atualizar Motivo')
        print('16- Deletar Motivo')
        print("")
        print('17- Sair')

        escolha = input('Escolha: ')

        if escolha == '1':
            inserir_categoria()

        elif escolha == '2':
            consultar_categoria()

        elif escolha == '3':
            atualizar_categoria()

        elif escolha == '4':
            deletar_categoria()
            print("Categoria deletada")

        elif escolha == '5':
            inserir_animal()

        elif escolha == '6':
            consultar_animal()

        elif escolha == '7':
            atualizar_animal()

        elif escolha == '8':
            deletar_animal()
            print("Animal deletada")

        elif escolha == '9':
            inserir_consulta()

        elif escolha == '10':
            consultar_consulta()

        elif escolha == '11':
            atualizar_consulta()

        elif escolha == '12':
            deletar_consulta()
            print("Consulta deletada")

        elif escolha == '13':
            inserir_motivo()

        elif escolha == '14':
            consultar_motivo()

        elif escolha == '15':
            atualizar_motivo()

        elif escolha == '16':
            deletar_motivo()

        elif escolha == '17':
            print("Você saiu!!")
            break