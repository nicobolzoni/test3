import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC341124b5853921ad6b4a2a33feab880b"
# Your Auth Token from twilio.com/console
auth_token  = "de92fa4429a016732a5439d44f89b2b9"
client = Client(account_sid, auth_token)

# Open all 6 Excel files
month_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for month in month_list:
    sales_table = pd.read_excel(f'{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any():
        vendedor = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'On the month of {month} someone has reached the target. Sales: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+447730049308",
            from_="+19854418183",
            body=f'On the month of {month} someone has reached the target. Sales: {vendedor}, Vendas: {vendas}')
        print(message.sid)





# For each file:

# Check if any value in Vendas column is higher than 55.000

# If higher than 55.000 -> Send sms with name, month and sales

# If lower than 55.000, dont do anything.
