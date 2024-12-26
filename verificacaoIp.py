#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os
import requests
import pandas as pd
import csv
from datetime import datetime, timedelta
from tqdm import tqdm  # Importando a biblioteca tqdm para barra de progresso

# URL da API
api_url = "https://login-report-api.mav.com.br:8902/login/protocolANDaccount"

# Valor fixo do token
token = "NjczOTVuZXcgdXNlciBjaGVjayB0b2tlbjEwNzkx"

# Definir protocolos fixos
protocol_list = ['pop3', 'imap', 'smtp']

# Função para ler dados do arquivo
def read_accounts_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    accounts = []
    for line in lines:
        account, start_day, end_day = line.strip().split(',')
        accounts.append((account, start_day, end_day))
    return accounts

# Caminho para o arquivo de entrada
file_path = 'accounts.txt'

# Ler os dados do arquivo
accounts_data = read_accounts_file(file_path)

# Criar diretório de saída, se não existir
output_dir = 'saida'
os.makedirs(output_dir, exist_ok=True)

# Iterar sobre as contas, protocolos, dias e fazer chamadas à API
for account, start_day, end_day in accounts_data:
    # Inicializar uma lista para armazenar os dados da conta atual
    all_data = []

    # Converte as datas de entrada em objetos datetime
    start_date = datetime.strptime(start_day, "%d%m%Y")
    end_date = datetime.strptime(end_day, "%d%m%Y")

    # Contabilizar o número de dias para a barra de progresso
    total_days = (end_date - start_date).days + 1

    # Barra de progresso para o processamento de cada conta
    with tqdm(total=total_days * len(protocol_list), desc=f"Processando conta {account}", unit=" dia") as pbar:
        for protocol in protocol_list:
            current_date = start_date
            while current_date <= end_date:
                params = {
                    'protocol': protocol,
                    'account': account,
                    'day': current_date.strftime('%d%m%Y'),
                    'token': token
                }
                response = requests.get(api_url, params=params)

                if response.status_code == 200:
                    data = response.json()
                    # Verificar duplicatas de IP no mesmo dia
                    seen_ips = set()
                    unique_data = []
                    for entry in data:
                        if entry['ip'] not in seen_ips:
                            seen_ips.add(entry['ip'])
                            unique_data.append(entry)
                    all_data.extend(unique_data)
                else:
                    print("Erro ao fazer a consulta à API para o dia {}, conta {} e protocolo {}: {}".format(
                        current_date.strftime('%d/%m/%Y'), account, protocol, response.status_code))

                # Avançar para o próximo dia
                current_date += timedelta(days=1)

                # Atualizar a barra de progresso
                pbar.update(1)

    # Criar um DataFrame a partir dos dados acumulados para a conta atual
    if all_data:
        df = pd.json_normalize(all_data)

        # Remover a coluna '_id' do DataFrame, se existir
        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)

        # Verificar se a coluna 'ip' existe no DataFrame
        if 'ip' in df.columns:
            # Aplicar formatação à coluna de IP
            df['ip'] = df['ip'].apply(lambda x: "{}".format(x))

            # Formatar a coluna de data e hora no formato brasileiro (DD/MM/YYYY HH:MM:SS AM/PM)
            if 'time' in df.columns:
                try:
                    df['time'] = pd.to_datetime(df['time'], format='%m/%d/%Y, %I:%M:%S %p', errors='coerce')
                    df['time'] = df['time'].dt.strftime('%d/%m/%Y %I:%M')
                except:
                    print("Erro ao formatar a coluna de data e hora.")

            # Salvar o DataFrame em um arquivo CSV para cada conta
            csv_file_name = "{}_report.csv".format(account)
            csv_file_path = os.path.join(output_dir, csv_file_name)
            df.to_csv(csv_file_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
            print("Dados salvos em {}".format(csv_file_path))
        else:
            print("Nenhum dado encontrado para a conta {}.".format(account))
    else:
        print("Nenhum dado encontrado para a conta {} nos protocolos especificados.".format(account))

# Informar que o script terminou
print("Script finalizado.")
