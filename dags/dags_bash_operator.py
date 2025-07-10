from __future__ import annotations

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator",
    schedule=None,
    # start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2", "study"],
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo 'Hello World!'",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2