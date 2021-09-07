from os import path
from os import listdir

import pandas as pd
from datetime import datetime

import pymysql

def get_files():
    output_path = './output'

    list_files = []
    if(path.isdir(output_path)):
        for file in listdir(output_path):
            if(path.isfile(f'{output_path}/{file}') and file.endswith('.csv')):
                list_files.append(file)
    else:
        print('A pasta com os arquivos não existe!')

    return list_files

def format_data(data):
    new_data = datetime.strptime(data, '%d.%m.%Y').strftime('%Y-%m-%d')
    return new_data

def create_table(nome):
    sql = f'''CREATE TABLE IF NOT EXISTS `{nome}`(
                data DATE NOT NULL,
                ultimo DOUBLE NOT NULL,
                abertura DOUBLE NOT NULL,
                maxima DOUBLE NOT NULL,
                minima DOUBLE NOT NULL,
                volume TEXT NOT NULL,
                var_porcnt TEXT NOT NULL,
                
                PRIMARY KEY(data)
            )'''
    return sql

def insert_into(nome, row):
    sql = f'''INSERT INTO `{nome}`(data, ultimo, abertura, maxima, minima, volume, var_porcnt)
              VALUES ('{row['Data']}', {row['Último']}, {row['Abertura']}, {row['Máxima']}, {row['Mínima']}, '{row['Vol.']}', '{row['Var%']}')'''

    return sql

def select_last_data(nome):
    sql = f'''SELECT data FROM `{nome}` ORDER BY data DESC'''

    return sql

def main():
    dict_dfs = {}
    list_files = get_files()

    user = 'root'
    passw = 'master'
    host = 'localhost'

    if (len(list_files) != 0):
        for file in list_files:
            df = pd.read_csv(f'./output/{file}', sep=';', decimal=',')
            df['Data'] = df['Data'].apply(format_data)
            dict_dfs[file[:-4]] = df

        conn = pymysql.connect(host = host, user = user, password = passw)

        try:
            cursor = conn.cursor()
            cursor.execute('CREATE SCHEMA IF NOT EXISTS investing')
            cursor.execute('USE investing')

            for nome, df in dict_dfs.items():
                cursor.execute(create_table(nome))
                cursor.execute(select_last_data(nome))

                row = cursor.fetchone()
                
                if(row):
                    if (True in (df['Data'] == f'{row[0]}').unique()):
                        index = (df.index[df['Data'] == f'{row[0]}']).tolist()[0]
                        df = df.loc[:index-1]

                        if(not df.empty):
                            for i in range(len(df.index)):
                                cursor.execute(insert_into(nome, df.loc[i]))
                            print(f'Os dados da tabela {nome} foram atualizados')                        
                        else:
                            print(f'A tabela {nome} já está atualizada')
                    else:
                        for i in range(len(df.index)):
                            cursor.execute(insert_into(nome, df.loc[i]))
                        print(f'Os dados da tabela {nome} foram atualizados')                        
                else:
                    for i in range(len(df.index)):
                        cursor.execute(insert_into(nome, df.loc[i]))
                    print(f'Os dados da tabela {nome} foram inseridos no BD')

            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f'Houve um erro ao realizar as operações no BD! {e}')
        finally:
            conn.close()
    else:
        print('Nenhum arquivo encontrado!')

main()