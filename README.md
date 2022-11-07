# O intuito deste código, é realizar uma leitura dentro de 6 planilhas diferente, um valor específico que é o vendedor que vendeu mais de 55000 no mês
# Assim que ele achar essa informação, atravéz do twilio ele manda um SMS para o meu número de celular, dizendo o mês, o nome do vencedor e o valor da venda.

#   Bibliotecas utilizadas:

#   pandas --> parte da integração com excel
#   openpyxl --> parte da integração com o excel
#   twilio --> intergação com SMS

import pandas as pd
from twilio.rest import Client

account_sid = "AC9b54b583f56fe8534d78dfd204367a99"
auth_token = "c4f9df7c8acd4c616a8133dcddd6e187"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # Verificar se algum valor na coluna Vendas na base é maior que 55 mil
    if (tabela_vendas['Vendas'] > 55000).any():
    #   Caso for menor que 55 000 não fazer nada    
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, "Vendas"].values[0]
        # Se for maior que 55.000.00 -> envia um SMS para o meu número com o nome, o mes e as vendas do vendedor                           
        print(
            f'No mês de {mes} alguem bateu a meta.     Vendedor: {vendedor}    Vendas: {vendas}')
        message = client.messages.create(
            to="+5514991519731",
            from_="+18563861147",
            body=f'No mês de {mes} alguem bateu a meta.     Vendedor: {vendedor}    Vendas: {vendas}')
        print(message.sid)
