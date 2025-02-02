import logging
import azure.functions as func
import random

def main(mytimer: func.TimerRequest) -> None:
    logging.info('DailySalesReportFunction triggered.')

    try:
        sales_count = random.randint(1, 100)
        logging.info(f"Daily sales report: {sales_count} sales made today.")

    except Exception as e:
        logging.error(f"Error: {str(e)}")