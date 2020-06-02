from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import json
from base import Session, engine, Base


class Unidade(Base):
    __tablename__ = 'tb_unidade'
    uc = Column(Integer, primary_key=True)
    endereco = Column(String)

    def __init__(self, uc, endereco):
        self.uc = uc
        self.endereco = endereco

    def all():
        Base.metadata.create_all(engine)
        session = Session()

        q = session.query(Unidade).all()

        dict_uc = {}

        for x in q:
            dict_uc[x.uc] = x.endereco

        session.close()

        return json.dumps(dict_uc)