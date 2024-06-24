from airflow.models.dag import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule= "0 2 * * 1",
    start_date=pendulum.datetime(2024, 4, 4, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    regist_t1 = PythonOperator(
       task_id = 'regist2_t1',
       python_callable= regist2,
       op_args= ['hjkim', 'man', 'kr', 'seoul']
       op_kwargs= {'email': 'wow@naver.com', 'phone': '010'}
    )

    regist2_t1
