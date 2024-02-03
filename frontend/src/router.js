import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./components/HomePage.vue";
import LoginPage from "./components/LoginPage.vue";
import Sign2Up from "./components/Sign2Up.vue";
import CategoryPage from "./components/CategoryPage.vue";
import AddCategory from "./components/AddCategory.vue";
import ProductPage from "./components/ProductPage.vue";
import AddProduct from "./components/AddProduct.vue";
import ApprovalPage from "./components/ApprovalPage.vue"
import ShoppingCart from "./components/ShoppingCart.vue"
import OrdersPage from "./components/OrdersPage.vue"
import DashboardPage from "./components/DashboardPage.vue"

const routes = [
  { path: "/", name: "home", component: HomePage },
  { path: "/login", name: "login", component: LoginPage },
  { path: "/register", name: "signup", component: Sign2Up },
  { path: "/categories", name: "category", component: CategoryPage },
  { path: "/categories/add", name: "add_category", component: AddCategory },
  { path: "/categories/edit/:id", name: "category.edit", component: AddCategory },
  { path: "/products", name: "product", component: ProductPage },
  { path: "/products/add", name: "add_product", component: AddProduct },
  { path: "/products/edit/:id", name: "product.edit", component: AddProduct },
  { path: "/approvals", name: "approvals", component: ApprovalPage },
  { path: "/cart/:id", name: "cart", component: ShoppingCart},
  { path: "/orders/:id", name: "orders", component: OrdersPage},
  { path: "/dashboard", name: "dashboard", component: DashboardPage}, 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
