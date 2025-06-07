import time
from etl import run_etl
from datetime import datetime

if __name__ == "__main__":
    while True:
        print(f"🕒 Running daily ETL at {datetime.now()}")
        run_etl()
        print("✅ ETL done. Sleeping for 24 hours.\n")
        time.sleep(86400)  # Wait for 24 hours
