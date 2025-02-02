import azure.functions as func
import logging
import re
import jwt
import datetime
import json
import random

app = func.FunctionApp()

# Login Function
@app.route(route="LoginFunction", auth_level=func.AuthLevel.ANONYMOUS)
def LoginFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('LoginFunction triggered.')

    try:
        req_body = req.get_json()
        username = req_body.get('username')
        password = req_body.get('password')

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            return func.HttpResponse("Invalid email format.", status_code=400)

        # Dummy authentication (replace with real logic)
        if password != "password123":
            return func.HttpResponse("Invalid credentials.", status_code=401)

        # Generate JWT
        payload = {
            "sub": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, "secret", algorithm="HS256")

        return func.HttpResponse(f"Token: {token}", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

# Order Processing Function
@app.route(route="OrderProcessingFunction", auth_level=func.AuthLevel.ANONYMOUS)
def OrderProcessingFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('OrderProcessingFunction triggered.')

    try:
        req_body = req.get_json()
        order_id = req_body.get('orderId')
        items = req_body.get('items', [])

        # Log each item
        for item in items:
            logging.info(f"{item['name']} order processing started.")

        return func.HttpResponse(f"Order {order_id} processing started.", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

# Daily Sales Report Function
@app.schedule(schedule="0 0 * * * *", arg_name="mytimer", run_on_startup=True)
def DailySalesReportFunction(mytimer: func.TimerRequest) -> None:
    logging.info('DailySalesReportFunction triggered.')

    try:
        sales_count = random.randint(1, 100)
        logging.info(f"Daily sales report: {sales_count} sales made today.")

    except Exception as e:
        logging.error(f"Error: {str(e)}")