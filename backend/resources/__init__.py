from flask_restful import Api
from .user import SignUp, Login, PendingApprovals
from .product import Product
from .category import Category
from .shoppingCart import ShoppingCartFunc
from .order import OrderResource
from .search import Search
#from .celery_task import UserTriggeredCSV
#from .celery import DownloadProductInfo,GetUnvisitedUsers 

api = Api(prefix="/api")

api.add_resource(SignUp, '/register')
api.add_resource(Login, '/login')
api.add_resource(PendingApprovals, '/approvals', '/approvals/<int:u_id>')

api.add_resource(Product, '/products', '/products/<int:p_id>')
api.add_resource(Category, '/categories', '/categories/<int:c_id>')

api.add_resource(OrderResource, '/orders', '/orders/<int:user>') 
api.add_resource(ShoppingCartFunc, '/cart', '/cart/<int:user>', '/cart/<int:user>/<int:item_id>')

api.add_resource(Search, '/search')
#api.add_resource(UserTriggeredCSV, '/download_csv')
# api.add_resource(DownloadProductInfo, '/download-info')
# api.add_resource(GetUnvisitedUsers,'/unvisited_users')


#api.add_resource(LoginTwo, '/testing')



