from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

#'sqlite:///nome.sqlite3' = nome do meu banco de dados
#configurar banco de dados
#criando conexão
engine = create_engine('sqlite:///base_vet.sqlite3')
db_sesion = scoped_session(sessionmaker(bind=engine))

#ela permite que você defina classes Python que representam tabelas de banco de dados
#de forma declarativa, sem a necessidade de configurar manualmente a relação entre as classes e tabelas
Base = declarative_base()
Base.query = db_sesion.query_property()


# class = representação do que tem no banco de dados
# class sempre com letra maiuscula e no singular
# index é para fazer pesquisa
# string é o texto, o que tá dentro do (), significa a quantidade de letras que o texto pode ter


class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id = Column(Integer, primary_key=True)
    Nome2 = Column(String(40), nullable=False, index=True)
    telefone = Column(Integer, nullable=False, index=True)
    CPF = Column(String(11), nullable=False, index=True, unique=True)
    Profissao2 = Column(String(50), nullable=False, index=True)
    Area2 = Column(String(40), nullable=False, index=True)

 # representação classe
    def __repr__(self):
        return '<Cliente: Nome:  {} Telefone:  {}>'.format(self.Nome2, self.telefone)

     # função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
         dados_cliente = {
             "id_user": self.id,
             "Nome2": self.Nome2,
             "telefone": self.telefone,
             "CPF": self.CPF,
            "Profissao2": self.Profissao2,
            "animal_id": self.animal_id,
            "animal": self.animal
         }
         return dados_cliente


class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id = Column(Integer, primary_key=True, index=True)
    nome_animal = Column(String(40), nullable=False, index=True)
    anoNasci3 = Column(Integer, nullable=False, index=True)
    raca3 = Column(String(40), nullable=False, index=True)
    cliente_id = Column(Integer, ForeignKey('TAB_CLIENTE.id'))
    cliente = relationship('Cliente')

    #representação classe
    def __repr__(self):
        return '<Cliente: Nome:  {} Raça:  {}>'.format(self.nome_animal, self.raca3)

    #função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
        dados_animal = {
            "id": self.id,
            "nome_animal": self.nome_animal,
            "anoNasci3": self.anoNasci3,
            "raca3": self.raca3,
            "cliente_id": self.cliente_id,
            "cliente": self.cliente
        }
        return dados_animal


class Veterinario(Base):
    __tablename__ = 'TAB_VETERINARIO'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    CRMV = Column(Integer, nullable=False, index=True, unique=True)
    salario = Column(Float, nullable=False, index=True)
    v_consulta2 = Column(Float, nullable=False, index=True)
#representação classe

    def __repr__(self):
         return '<Veterinario: Nome:  {} CRMV:  {}>'.format(self.nome, self.CRMV)

     #função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
         db_sesion.delete(self)
         db_sesion.commit()

    def serialize_user(self):
        dados_veterinario = {
            "id": self.id,
            "nome": self.nome,
            "CRMV": self.CRMV,
            "salario": self.salario,
            "v_consulta2": self.v_consulta2,
        }
        return dados_veterinario


class Consulta(Base):
    __tablename__ = 'TAB_CONSULTA'
    idConsulta = Column(Integer, primary_key=True)
    data1 = Column(String(40), nullable=False, index=True)
    hora1 = Column(Integer, nullable=False, index=True)
    motivo_id1 = Column(Integer, ForeignKey('TAB_MOTIVO.id'))
    motivo = relationship('Motivo')
    minuto = Column(Integer, nullable=False, index=True)
    idAnimal1 = Column(Integer, ForeignKey('TAB_ANIMAL.id'))
    idAnimais = relationship('Animal')
    idVeterinario1 = Column(Integer, ForeignKey('TAB_VETERINARIO.id'))
    idVeterinarios = relationship('Veterinario')

# representação classe
    def __repr__(self):
        return '<Consulta: Animal_id:  {} Dia: {}  Horário: {} >'.format(self.idAnimal1, self.data1, self.motivo_id1)

    # função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
        dados_consulta = {
            "idConsulta": self.idConsulta,
            "data1": self.data1,
            "hora1": self.hora1,
            "motivo_id1": self.motivo_id1,
            "idAnimal1": self.idAnimal1,
            # "idVeterinario1": self.idVeterinario1

        }
        return dados_consulta


class Motivo(Base):
    __tablename__ = 'TAB_MOTIVO'
    id = Column(Integer, primary_key=True)
    nome_motivo = Column(String(40), nullable=False, index=True)
    motivo_categoria = Column(String(40), nullable=False, index=True)
    valor_motivo = Column(Float, nullable=False, index=True)

    #representação classe
    def __repr__(self):
        return '<Motivo: Nome_motivo:  {} Categoria_motivo: {} >'.format(self.nome_motivo, self.motivo_categoria)

    #função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
        dados_motivo = {
            "id_user": self.id,
            "nome_motivo": self.nome_motivo,
            "motivo_categoria": self.motivo_categoria,
            "valor_motivo": self.valor_motivo,
        }
        return dados_motivo

class Categoria(Base):
    __tablename__ = 'TAB_CATEGORIA'
    id = Column(Integer, primary_key=True)
    nome_categoria = Column(String(40), nullable=False, index=True)
    #representação classe
    def __repr__(self):
        return '<Categoria: Nome_categoria:  {}>'.format(self.nome_categoria)

    #função paea salvar no banco
    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
        dados_categoria = {
            "id": self.id,
            "nome_categoria": self.nome_categoria,
        }
        return dados_categoria

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
