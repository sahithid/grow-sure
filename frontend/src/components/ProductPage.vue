<template>
  <div>
    <div class="d-flex justify-content-center">
      <input
        class="form-control mr-sm-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        v-model="search"
        style="width: 30rem"
      />
      <button
        class="btn btn-outline-success my-2 my-sm-0"
        type="submit"
        @click.prevent="searchPage"
      >
        Search
      </button>
    </div>
    <br />
    <div class="d-flex justify-content-center">
      <button
        type="button"
        class="w-30 btn btn-lg btn-outline-success justify-content-center"
        v-show="role == 'manager'"
        @click="$router.push('/products/add')"
      >
        Add Product +
      </button>
      <button
        class="btn btn-outline-success my-2 my-sm-0"
        type="submit"
        v-if="role == 'manager'"
        @click.prevent="exportCSV"
      >
        Product Summary
      </button>
    </div>
    <p></p>
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      <div
        class="card mb-4 rounded-3 shadow-sm"
        v-for="product in products"
        :key="product.id"
      >
        <div class="card-header py-3">
          <h4 class="my-0 fw-normal">{{ product.name }}</h4>
        </div>
        <div class="card-body">
          <h6>
            <u>{{ product.category }} </u>
          </h6>
          <ul class="list-unstyled mt-3 mb-4">
            <li>
              <b v-show="role != 'user'">Stock : {{ product.stock }}</b>
            </li>
            <li>Rs. {{ product.price }}</li>
            <li>Units : {{ product.quantity }} {{ product.units }}</li>
            <li>Manufacture date : {{ product.manufacture_date }}</li>
            <li>Expiry date: {{ product.expiry_date }}</li>
            <li>stock : {{ product.stock }}</li>
          </ul>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-success"
            v-if="role == 'user' && product.stock > 0"
            @click.prevent="addToCart(product.id)"
          >
            Add to Cart
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-success disabled"
            v-if="role == 'user' && product.stock == 0"
          >
            Out of Stock
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-success"
            v-show="role == 'manager'"
            @click="$router.push('/products/edit/'.concat(product.id))"
          >
            Edit
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-danger"
            v-show="role == 'manager'"
            @click.prevent="removeProduct(product.id)"
          >
            Remove
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: [],
      name: "",
      id: 0,
      role: localStorage.getItem("role"),
      search: "",
      search_flag: true,
    };
  },
  methods: {
    getProducts() {
      fetch("http://127.0.0.1:5000/api/products", {
        method: "GET",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
      })
        .then((res) => res.json())
        .then((data) => {
          this.products.push(...data);
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    //for managers
    removeProduct(p_id) {
      if (confirm("Are you sure you want to delete this? ")) {
        fetch("http://127.0.0.1:5000/api/products/".concat(p_id), {
          method: "DELETE",
          //mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            Authorization: "Bearer " + localStorage.getItem("accessToken"),
          },
        })
          .then((res) => res.json())
          .then((data) => {
            alert(data["msg"]);
            //console.log(data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    //for user
    addToCart(product_id) {
      console.log(product_id);
      const u_id = localStorage.getItem("user_id");
      fetch("http://127.0.0.1:5000/api/cart/".concat(u_id), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          product_id: product_id,
          quantity: 1,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    searchPage() {
      fetch("http://127.0.0.1:5000/api/search", {
        method: "POST",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          search: this.search,
          comp: "Product1",
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data["msg"]) {
            alert(data["msg"]);
          } else {
            this.products = [];
            this.products.push(...data);
          }
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    exportCSV() {
      fetch("http://127.0.0.1:5000/product-csv/", {
        method: "GET",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getProducts();
  },
};
</script>

<style>
.card-header {
  background-color:#dcf1dc !important;
}
</style>
