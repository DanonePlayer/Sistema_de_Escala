from datetime import date
from calendar import monthrange

data_atual = date(2023, 10, 1)
# monthrange retorna o último dia do mês, basta setá-lo na data e pronto
last_date = data_atual.replace(day=monthrange(data_atual.year, data_atual.month)[1])
print(last_date) # 2022-05-31