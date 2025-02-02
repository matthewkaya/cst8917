import logging
import azure.functions as func
import re
import jwt
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
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