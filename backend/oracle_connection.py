import oracledb
from config import ORACLE_USERNAME, ORACLE_PASSWORD, ORACLE_DSN

def get_connection():
    try:
        connection = oracledb.connect(
            user=ORACLE_USERNAME,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN
        )
        return connection
    except Exception as e:
        print("Oracle Connection Error:", e)
        return None
