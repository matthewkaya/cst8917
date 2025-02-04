import azure.functions as func
import jwt
import re
from datetime import datetime, timedelta

app = func.FunctionApp()

@app.function_name(name="login")
@app.route(route="login", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
def login(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse request body
        req_body = req.get_json()
        username = req_body.get("username")
        password = req_body.get("password")

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            return func.HttpResponse("Invalid email format.", status_code=400)

        # Mock authentication (replace with database check)
        if username != "user@example.com" or password != "password123":
            return func.HttpResponse("Invalid credentials.", status_code=401)

        # Generate JWT (replace 'SECRET_KEY' with a secure secret)
        payload = {
            "sub": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256")
        return func.HttpResponse(token, mimetype="text/plain")

    except ValueError:
        return func.HttpResponse("Invalid request body.", status_code=400)