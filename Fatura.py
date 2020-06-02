from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import json
from base import Session, engine, Base


class Fatura(Base):
    __tablename__ = 'tb_fatura'
    uc = Column(Integer, primary_key=True)
    mes = Column(String, primary_key=True)
    periodo = Column(String)
    total = Column(Numeric)
    vencimento = Column(String)
    cod_barras = Column(String)
    consumo = Column(Numeric)

    def __init__(self, uc, mes, periodo, total, vencimento, cod_barras, consumo, status):
        self.uc = uc
        self.mes = mes
        self.periodo = periodo
        self.total = total
        self.vencimento = vencimento
        self.cod_barras = cod_barras
        self.consumo = consumo
        self.status = status

    def all(uc):
        Base.metadata.create_all(engine)
        session = Session()

        q = session.query(Fatura).filter(Fatura.uc == uc).all()

        lista = []

        for x in q:
            dados = {}
            dados['uc'] = x.uc
            dados['mes'] = x.mes
            dados['periodo'] = x.periodo
            dados['total'] = float(x.total)
            dados['vencimento'] = x.vencimento
            dados['cod_barras'] = x.cod_barras
            dados['consumo'] = float(x.consumo)
            dados['status'] = x.status

            lista.append(dados)

        session.close()

        return json.dumps(lista)
