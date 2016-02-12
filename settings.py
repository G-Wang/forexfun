from decimal import Decimal
import os

Access_token = "44cb8414522399b7fc2df5633db21e1f-27c0c7bca98da03adb063443a9695a54"
Account_ID = 1800486

ENVIRONMENTS = { 
    "streaming": {
        "real": "stream-fxtrade.oanda.com",
        "practice": "stream-fxpractice.oanda.com",
        "sandbox": "stream-sandbox.oanda.com"
    },
    "api": {
        "real": "api-fxtrade.oanda.com",
        "practice": "api-fxpractice.oanda.com",
        "sandbox": "api-sandbox.oanda.com"
    }
}

CSV_DATA_DIR = os.environ.get('QSFOREX_CSV_DATA_DIR', "/home/gary/projects/FOREX/csv_backup")
OUTPUT_RESULTS_DIR = os.environ.get('QSFOREX_OUTPUT_RESULTS_DIR', "home/gary/projects/FOREX/output_results")

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]
ACCESS_TOKEN = os.environ.get('OANDA_API_ACCESS_TOKEN', Access_token)
ACCOUNT_ID = os.environ.get('OANDA_API_ACCOUNT_ID', Account_ID)

BASE_CURRENCY = "USD"
EQUITY = Decimal("10000.00")
