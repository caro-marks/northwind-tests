# importa as bibliotecas requeridas
import os
import pandas as pd
from sqlalchemy import create_engine

# Para isso é necessário ter o NorthWind DB no repositório do PostGres local
engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost/NorthWind')

# Obtem todas as datas únicas da tabela 'orders'
dates = pd.read_sql_query("""
SELECT order_date
FROM orders;
""", engine)['order_date'].unique()

# Obtem os nomes de todas as tabelas públicas
tables = pd.read_sql_query("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';
""", engine)['table_name'].values

# Dicionário criado para armazenar os nomes das tabelas (keys) e seus respectivos conteúdos (values)
dataframes = {'order_details': pd.read_csv(
    '../code-challenge-main/data/order_details.csv')}

# Busca cada tabela e adiciona no dicionário 'dataframes'
for table in tables:
    dataframes[table] = pd.read_sql_table(table, engine)

# encerramento da utilização do postgres db via sqlalchemy
engine.dispose()

# função para facilitar a criação das pastas e diretórios utilizados para armazenar as tabelas e de acordo com cada data específica


def createDir(table, date):
    if table == 'order_details':
        outdir = f'./data/csv/{dia}'
    else:
        outdir = f'./data/postgres/{table}/{date}'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        return


# loop que cria dataframes temporários de acordo com cada conjunto único de tabela e data, e os armazena localmente no formato JSON
for date in dates:
    dia = str(date)

    for tabela in dataframes.keys():
        createDir(tabela, dia)

    Orders = dataframes['orders'][dataframes['orders']
                                  ['order_date'] == dia]  # orders Table
    Orders.to_json(
        f'./data/postgres/orders/{dia}/index.json', orient='table', index=False)

    order_ids = Orders['order_id']
    Order_details = dataframes['order_details'][dataframes['order_details']['order_id'].isin(
        order_ids)]  # order_details Table
    Order_details.to_json(
        f'./data/csv/{dia}/order_details.json', orient='table', index=False)

    product_ids = Order_details['product_id']
    Products = dataframes['products'][dataframes['products']
                                      ['product_id'].isin(product_ids)]  # products Table
    Products.to_json(
        f'./data/postgres/products/{dia}/index.json', orient='table', index=False)

    category_ids = Products['category_id']
    Categories = dataframes['categories'][dataframes['categories']
                                          ['category_id'].isin(category_ids)]  # categories Table
    Categories.to_json(
        f'./data/postgres/categories/{dia}/index.json', orient='table', index=False)

    supplier_ids = Products['supplier_id']
    Suppliers = dataframes['suppliers'][dataframes['suppliers']
                                        ['supplier_id'].isin(supplier_ids)]  # suppliers Table
    Suppliers.to_json(
        f'./data/postgres/suppliers/{dia}/index.json', orient='table', index=False)

    customer_ids = Orders['customer_id']
    Customers = dataframes['customers'][dataframes['customers']
                                        ['customer_id'].isin(customer_ids)]  # customers Table
    Customers.to_json(
        f'./data/postgres/customers/{dia}/index.json', orient='table', index=False)
    Customer_customer_demo = dataframes['customer_customer_demo'][dataframes['customer_customer_demo']['customer_id']
                                                                  .isin(customer_ids)]  # customer_customer_demo Table
    Customer_customer_demo.to_json(
        f'./data/postgres/customer_customer_demo/{dia}/index.json', orient='table', index=False)

    customer_type_ids = Customer_customer_demo['customer_type_id']
    Customer_demographics = dataframes['customer_demographics'][dataframes['customer_demographics']['customer_type_id']
                                                                .isin(customer_type_ids)]  # customer_demographics Table
    Customer_demographics.to_json(
        f'./data/postgres/customer_demographics/{dia}/index.json', orient='table', index=False)

    employee_ids = Orders['employee_id']
    Employees = dataframes['employees'][dataframes['employees']
                                        ['employee_id'].isin(employee_ids)]  # employees Table
    Employees.to_json(
        f'./data/postgres/employees/{dia}/index.json', orient='table', index=False)
    Employee_territories = dataframes['employee_territories'][dataframes['employee_territories']['employee_id']
                                                              .isin(employee_ids)]  # employee_territories Table
    Employee_territories.to_json(
        f'./data/postgres/employee_territories/{dia}/index.json', orient='table', index=False)

    territory_ids = Employee_territories['territory_id']
    Territories = dataframes['territories'][dataframes['territories']
                                            ['territory_id'].isin(territory_ids)]  # territories Table
    Territories.to_json(
        f'./data/postgres/territories/{dia}/index.json', orient='table', index=False)

    region_ids = Territories['region_id']
    Region = dataframes['region'][dataframes['region']
                                  ['region_id'].isin(region_ids)]  # region Table
    Region.to_json(
        f'./data/postgres/region/{dia}/index.json', orient='table', index=False)

    ship_vias = Orders['ship_via']
    Shippers = dataframes['shippers'][dataframes['shippers']
                                      ['shipper_id'].isin(ship_vias)]  # shippers Table
    Shippers.to_json(
        f'./data/postgres/shippers/{dia}/index.json', orient='table', index=False)

exit()
