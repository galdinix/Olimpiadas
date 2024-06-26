from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Medalha(Base):
    __tablename__ = 'medalha'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_medalha = Column(String, nullable=True)

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_evento = Column(String, nullable=False)
    esporte_id = Column(Integer, ForeignKey('esporte.id'), nullable=False)
    esporte = relationship("Esporte")

class Esporte(Base):
    __tablename__ = 'esporte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_esporte = Column(String, nullable=False)

    def __str__(self):
        return f'{self.nome_esporte}'

class Jogos(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ano_jogos = Column(Integer, nullable=False)
    nome_jogos = Column(String, nullable=False)
    estacao = Column(String, nullable=False)

class Cidade(Base):
    __tablename__ = 'cidade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_cidade = Column(String, nullable=False)

class JogosCidade(Base):
    __tablename__ = 'jogos_cidade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    jogos_id = Column(Integer, ForeignKey('jogos.id'), nullable=False)
    cidade_id = Column(Integer, ForeignKey('cidade.id'), nullable=False)

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome_completo = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    altura = Column(Integer, nullable=True)
    peso = Column(Integer, nullable=True)

class NocRegiao(Base):
    __tablename__ = 'noc_regiao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    noc = Column(String, nullable=False)
    nome_regiao = Column(String, nullable=False)

class PessoaRegiao(Base):
    __tablename__ = 'pessoa_regiao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'), nullable=False)
    regiao_id = Column(Integer, ForeignKey('noc_regiao.id'), nullable=False)

class JogosCompetidor(Base):
    __tablename__ = 'jogos_competidor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    jogos_id = Column(Integer, ForeignKey('jogos.id'), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'), nullable=False)
    idade = Column(Integer, nullable=True)

class CompetidorEvento(Base):
    __tablename__ = 'competidor_evento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey('evento.id'), nullable=False)
    competidor_id = Column(Integer, ForeignKey('pessoa.id'), nullable=False)
    medalha_id = Column(Integer, ForeignKey('medalha.id'), nullable=True)
