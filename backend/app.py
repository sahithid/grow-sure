from flask import Flask, jsonify, render_template, send_file
from models import db, bcrypt, ma
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_cors import CORS
from resources import api
from werkzeug import exceptions
from tasks import daily_reminders, create_csv, monthly_report
from celery.schedules import crontab
from models.productModel import Product1, product_schema
from models.userModel import User, user_schema
from models.orderModel import Order, order_schema
from celery.result import AsyncResult
from worker import celery_init_app
from sqlalchemy.sql import text
import time
from models.create_admin import create_admin
import pandas as pd
from jwt_decorators import manager_required
#from flask_caching import Cache


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
    app.config["JWT_SECRET_KEY"] = "superduper-secret-key"
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    bcrypt.init_app(app)
    ma.init_app(app)
    jwt = JWTManager(app)
    api.init_app(app)
    CORS(app)
    app.app_context().push()
    create_admin("admin@email.com")
    return app


app = create_app()
celery_app = celery_init_app(app)


@manager_required()
@app.route("/product-csv/")
def download_csv():
    task = create_csv.delay()
    return jsonify({'task_id': task.id, 'msg':'Successfully Downloaded'})



@app.get("/monthly_report/<task_id>")
def monthly_report(task_id):
    result = AsyncResult(task_id)
    if result.ready():
        filename = result.result
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({"message": "Task Pending"}), 404



if __name__ == "__main__":
    app.run(debug=True)
