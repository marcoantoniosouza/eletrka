from base import Session, engine, Base

from Fatura import Fatura

# Base.metadata.create_all(engine)
# session = Session()

# q = session.query(Fatura).all()

# for x in q:
# 	print(x.mes, x.uc, x.total)

# session.close()

print(Fatura.all('12618390'))