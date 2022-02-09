# BIBLIOTECAS
# Utilidades
import os
import sys
from pathlib import Path
from datetime import datetime

# Airflow
from airflow.decorators import dag


PROJECT_NAME = '{{cookiecutter.nome_do_projeto}}'
local = str(Path(__file__).parent.parent.resolve())

# Importa as tasks da pasta do projeto
sys.path.insert(0, os.path.join(local, 'scripts', PROJECT_NAME, 'src'))

default_args = {
    'owner': '{{cookiecutter.dono_do_projeto}}',
    'depends_on_past': False,
    'email': ['{{cookiecutter.dono_do_projeto}}@uninove.br'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0
}


@dag(
    default_args=default_args,
    description='{{cookiecutter.descricao_do_projeto}}',
    schedule_interval='0 0 * * *',
    start_date=datetime(2020, 1, 1),
    tags=[{{cookiecutter.tags}}]
)
def {{cookiecutter.nome_do_projeto}}_dag():

    # Importar tasks
    # from nome_do_arquivo import nome_da_task

    # INICIE SEU CODIGO AQUI!
    print('{{cookiecutter.nome_do_projeto}}')


{{cookiecutter.nome_do_projeto}}_dag()
