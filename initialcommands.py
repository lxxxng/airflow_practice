#### conda env with python 3.6, using ubuntu 
# source venv/bin/activate

#### install airflow from official github repo 

#### for current dir
# export AIRFLOW_HOME=$(pwd)   // everytime u reopen wsl
# airflow db init
# airflow webserver -p 8080 
# airflow users create --username admin --firstname firstname --lastname lastname --role Admin --email admin@domain.com --password password

### open another terminal and run the scheduler
# airflow scheduler