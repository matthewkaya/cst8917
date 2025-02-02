import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
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