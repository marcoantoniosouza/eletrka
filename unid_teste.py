from base import Session, engine, Base

from Unidade import Unidade

uc = Unidade(1, 'abc')

Base.metadata.create_all(engine)
session = Session()

session.add(uc)
session.commit()
session.close()