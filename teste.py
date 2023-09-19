import bd_sistemas_de_escala as bd
from datetime import datetime, timedelta

# Conecte-se ao seu banco de dados aqui (substitua com sua própria lógica de conexão)

# Recupere os dados da escala e dos funcionários
escala = bd.consultar_usuarios("SELECT * FROM escala WHERE escala_id = 4;")
print(escala)

funcionarios = bd.consultar("SELECT * FROM usuario;")

data_inicio_escala = datetime.strptime(str(escala[3]), '%d/%m/%Y')
data_fim_escala = datetime.strptime(str(escala[4]), '%d/%m/%Y')

# # Calcule o número de dias totais na escala
dias_totais = (data_fim_escala - data_inicio_escala).days + 1
print(f"Dias totais da escala: {dias_totais}")
#
# # Calcule a quantidade de dias que cada funcionário deve ter inicialmente
dias_por_funcionario = dias_totais // len(funcionarios)

print(f"Dias por funcionario: {dias_por_funcionario}")
#
# Distribua os dias da escala entre os funcionários
dias_restantes = dias_totais

for funcionario in funcionarios:
    if dias_restantes > 0:
        dias_atribuidos = min(dias_por_funcionario, dias_restantes)
        data_inicio = data_inicio_escala + timedelta(days=dias_totais - dias_restantes)
        data_fim = data_inicio + timedelta(days=dias_atribuidos - 1)
        print(f"\nData inicio: {data_inicio}")
        print(f"\nData fim: {data_fim}")

        # Insira os dados na tabela ESCALA_USUARIO
        # cursor.execute(
        #     "INSERT INTO ESCALA_USUARIO (id_usuario, id_escala, atribuido, prioridade, data_inicio_servico, data_fim_servico) VALUES (?, ?, ?, ?, ?, ?);",
        #     (funcionario['usuario_id'], sua_escala_id, True, funcionario['prioridade'], data_inicio, data_fim))

        dias_restantes -= dias_atribuidos

print(f"Dias que sobraram: {dias_restantes}")
#
# # Commit as alterações no banco de dados
# conn.commit()
#
# # Feche a conexão com o banco de dados
# conn.close()