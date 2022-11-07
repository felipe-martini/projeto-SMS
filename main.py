import pandas as pd
from twilio.rest import Client

account_sid = "AC9b54b583f56fe8534d78dfd204367a99"
auth_token = "c4f9df7c8acd4c616a8133dcddd6e187"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, "Vendas"].values[0]
        print(
            f'No mês de {mes} alguem bateu a meta.     Vendedor: {vendedor}    Vendas: {vendas}')
        message = client.messages.create(
            to="+5514991519731",
            from_="+18563861147",
            body=f'No mês de {mes} alguem bateu a meta.     Vendedor: {vendedor}    Vendas: {vendas}')
        print(message.sid)
# Para cada arquivo:

# Verificar se algum valor na coluna Vendas na base é maior que 55 mil

# Se for maior que 55.000.00 -> envia um SMS para o meu número com o nome, o mes e as vendas do vendedor

#   Caso for menor que 55 000 não fazer nada

#   Bibliotecas utilizadas:

#   pandas --> parte da integração com excel
#   openpyxl --> parte da integração com o excel
#   twilio --> intergação com SMS
