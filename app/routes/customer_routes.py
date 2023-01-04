from app import db
from app.models.customer import Customer
import app.models.model_helpers
from flask import Blueprint, jsonify, abort, make_response, request

customers_bp = Blueprint("customers_bp", __name__, url_prefix="/customers")

@customers_bp.route("", methods=["POST"])
def create_customer():
    customer_data = request.get_json()

    new_customer = Customer(
        name = customer_data["name"],
        postal_code = customer_data["postal_code"],
        phone = customer_data["phone_number"],
        videos_checked_out_count = 0
    )

    db.session.add(new_customer)
    db.session.commit()

    return make_response(f"Customer {new_customer.name} created", 201)

@customers_bp.route("", methods=["GET"])
def get_customers():
    customer_query = Customer.query

    customers = customer_query.all()
    customer_response = []

    for customer in customers:
        customer_response.append({
            "id": customer.id,
            "name": customer.name,
            "registered_at": customer.registered_at,
            "postal_code": customer.postal_code,
            "phone": customer.phone,
            "videos_checked_out_count": customer.videos_checked_out_count
        })
    
    return jsonify(customer_response)