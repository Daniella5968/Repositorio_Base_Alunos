import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Configuraçao da conexao: troque CRIE_UMA_SENHA por 1234
DATABASE_URT = "postgresql://postgres:CRIE_UMA_SENHA@localhost:5432/postgres"
# A engine cria a conexao com o banco
engine= create_engine(DATABASE_URT)
# configuraçao da sessao (que é a área de trabalho para conversar com o banco de dados)
SessionLocall=sessionmaker(autocommit=False,autoflush=False, bind=engine)
#Aqui temos a base declarativa, elaliga nossas entidades e as tabelas do banco.
Base= declarative_base()

class usuario(Base):
    __tablename__= "usuarios"
    id= Column(integer,primary_ket=True,index=True, autoincrement=True)
    nome= Column(String(255), nullable=False)
    email= Column(String(2025),nullable=False) 
    senha_hash= column(String(255), nullable=False)
    criado_em= column(DateTime(timezone=True), default=datetime.detetime.now)

    notas= relationship("Nota", back_populates="autor")
    usuario_enderecos = relationship("Enderecos")   
    back_populates="moradores"

class Nota(Base):
    __tablename__= "notas"
    id= column(Integer, primary_ket=True, autoincrement=True)
    id_usuario= column(String(255), nullable=False)
    titulo= column(String(255), nullable=False)
    conteudo_em= column(DateTime(timezone=True), defaul=datetime.datetime.now)
    modificado_em= column(DateTime(timezone=True),default=datetime.datetime.now)
    autor=relationship("usuario",back_populates="notas")