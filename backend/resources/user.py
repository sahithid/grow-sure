from flask_restful import Resource
from flask import jsonify, request
from werkzeug.exceptions import NotFound
from models import db, bcrypt
from models.userModel import User, user_schema, login_schema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from jwt_decorators import admin_required


# user, manager registration
class SignUp(Resource):
    def post(self):
        # data = user_parser.parse_args()
        inp = request.get_json()
        input = user_schema.load(inp)
        approve = True
        if input["role"] == "manager":
            approve = False
        try:
            # new_user = User(email=data.email, password=data.password, name=data.name, role=data.role, approved=data.approved)
            new_user = User(
                email=input["email"],
                password=input["password"],
                name=input["name"],
                role=input["role"],
                approved=approve,
            )
            db.session.add(new_user)
            db.session.commit()
            if input["role"] == "manager":
                return jsonify({"msg": "Signed up! Pending Admin Approval!"})
            else:
                return jsonify({"msg": "Sucessfully Signed up!"})
        except IntegrityError:
            return jsonify({"msg": "User already exists!"})


# user, manager, admin login
class Login(Resource):
    def post(self):
        inp = request.get_json()
        input = login_schema.load(inp)
        user = db.session.query(User).filter_by(email=input["email"]).first()
        if not user:
            return jsonify({"msg": "Incorrect email!", "code": 401})
        pass_ = bcrypt.check_password_hash(user.password, input["password"])

        if not pass_:
            return jsonify({"msg": "Incorrect password!", "code": 401})

        role_claim = "is_" + user.role

        if not user.approved:
            return jsonify(
                {"msg": "Store Manager sign up pending Admin approval!", "code": 401}
            )

        else:
            access_token = create_access_token(
                identity={"id": user.id, "usermail": user.email, "role": user.role},
                additional_claims={role_claim: True},
            )
            return jsonify(
                {
                    "access_token": access_token,
                    "role": user.role,
                    "id": user.id,
                    "name": user.name,
                    "msg": "Successfully logged in!",
                    "code": 200,
                }
            )


# pending registration requests for the admin from store manager sign ups
class PendingApprovals(Resource):
    @admin_required()
    def get(self):
        data = db.session.query(User).filter_by(approved=0).all()
        users = user_schema.dump(data, many=True)
        return users

    @admin_required()
    def put(self, u_id=None):
        if u_id == None:
            to_approve = db.session.query(User).filter_by(approved=0)
            users = user_schema.dump(to_approve, many=True)
            for i in range(len(users)):
                u = db.session.query(User).get(users[i]["id"])
                u.approved = True
                db.session.commit()
            return jsonify("All managers approved!")
        else:
            u = db.session.query(User).get(u_id)
            action = request.json["action"]
            if action == "approve":
                u.approved = True
                db.session.commit()
                return jsonify({"msg": "Manager with id %d approved!" % (u_id)})
            else:
                # delete the manager user
                u = db.session.query(User).filter_by(id=u_id)
                u.delete()
                db.session.commit()
                # notify the manager via email
                return jsonify({"msg": "Manager registration approval rejected!"})
