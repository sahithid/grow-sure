from celery import shared_task
from models.userModel import User, user_schema
from models.productModel import Product1, product_schema
from models.orderModel import Order, order_schema, OrderItem, order_item_schema
from models import db
from emails import send_email
import pandas as pd
import datetime
from jinja2 import Template
from datetime import datetime
from sqlalchemy import and_
import json
from os.path import dirname,abspath


# DAILY USER EMAIL REMINDERS
@shared_task(ignore_result=False)
def daily_reminders(subject="Check out GROW!"):
    all_users = db.session.query(User).filter_by(role="user").all()
    user_ids = user_schema.dump(all_users, many=True)
    users = [u_id["id"] for u_id in user_ids]
    today = str(datetime.now())[:10]
    visited_orders = (
        db.session.query(Order)
        .filter(and_(Order.user_id.in_(users), Order.created_at.contains(today)))
        .all()
    )
    visited_users = order_schema.dump(visited_orders, many=True)
    visited = list(set([i["user_id"] for i in visited_users]))

    unvisited_users = [i for i in users if i not in visited]
    u = db.session.query(User).filter(User.id.in_(unvisited_users))
    unvisited_users = user_schema.dump(u, many=True)
    emails = [i["email"] for i in unvisited_users]
    names = [i["name"] for i in unvisited_users]

    for each in range(len(emails)):
        with open("templates/email_template.html", "r") as f:
            temp = Template(f.read())
            email_content = temp.render(name=names[each])
            send_email(emails[each], subject, email_content)

    return "Daily Reminders Sent!"


def get_user_orders(user):
    user_orders = db.session.query(Order).filter_by(user_id=user)
    orders = order_schema.dump(user_orders, many=True)
    result = []
    total_expenditure = 0
    cat = {}
    for i in range(len(orders)):
        this_order = {}
        order_id = orders[i]["id"]
        total = orders[i]["total"]
        time = orders[i]["created_at"][:16]
        this_order["order_id"] = order_id
        this_order["total"] = total
        this_order["time"] = time
        total_expenditure = total_expenditure + total
        items_ = db.session.query(OrderItem).filter_by(order_id=order_id)
        items = order_item_schema.dump(items_, many=True)
        items_ = []
        for i in range(len(items)):
            product = db.session.query(Product1).get(items[i]["product_id"])
            p = product_schema.dump(product)
            p["amount_to_buy"] = items[i]["quantity"]
            items_.append(p)
            if p["category"] in cat.keys():
                cat[p["category"]] = cat[p["category"]] + (
                    items[i]["quantity"] * p["price"]
                )
            else:
                cat[p["category"]] = items[i]["quantity"] * p["price"]
        this_order["items"] = items_
        result.append(this_order)
    return result, total_expenditure, cat


# MONTHLY ORDER REPORT FOR USERS
@shared_task(ignore_result=False)
def monthly_report(subject="Your GROW Orders This Month!"):
    this_month = "-" + str(datetime.now().date().month) + "-"
    all_users = db.session.query(User).filter_by(role="user").all()
    user_ids = user_schema.dump(all_users, many=True)
    users = [u_id["id"] for u_id in user_ids]
    visited_orders = (
        db.session.query(Order)
        .filter(and_(Order.user_id.in_(users), Order.created_at.contains(this_month)))
        .all()
    )
    visited_users = order_schema.dump(visited_orders, many=True)
    visited = list(set([i["user_id"] for i in visited_users]))
    u = db.session.query(User).filter(User.id.in_(visited))
    visited_users_ = user_schema.dump(u, many=True)
    emails = [i["email"] for i in visited_users_]
    names = [i["name"] for i in visited_users_]
    u_ids = [i["id"] for i in visited_users_]

    for each in range(len(u_ids)):
        user_order, total, cat = get_user_orders(u_ids[each])
        with open("templates/monthly_report.html", "r") as f:
            temp = Template(f.read())
            email_content = temp.render(
                month=datetime.now().date().month,
                info=user_order,
                name=names[each],
                total=total,
                cat=json.dumps(cat),
                categories=list(cat.keys()),
                prices=list(cat.values()),
            )
            send_email(emails[each], subject, email_content)

    return "Monthly Report Sent!"


#MANAGER-TRIGGERED PRODUCT CSV
@shared_task(ignore_result=False)
def create_csv():
    filename = "products_" + str(datetime.now()) + ".csv"
    pro = db.session.query(Product1).all()
    columns = Product1.__table__.columns.keys()
    products = product_schema.dump(pro, many=True)
    df = pd.DataFrame.from_records(products, columns=columns)
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    # parent_dir = dirname(dirname(abspath(__file__)))
    #path = os.path.dirname(current_dir)
    df.to_csv(filename)

    return filename
