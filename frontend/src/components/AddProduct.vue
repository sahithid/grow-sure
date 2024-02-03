<template>
  <main class="form-signin w-100 m-auto">
    <form>
      <h1 class="h3 mb-3 fw-normal" v-if="action == 'add'">Add Product</h1>
      <h1 class="h3 mb-3 fw-normal" v-else>Edit Product</h1>
      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="floatingInput"
          v-model="name"
        />
        <label for="floatingInput">Product Name</label>
      </div>
      <div class="form-floating">
        <select class="form-control" id="floatingSelect" v-model="category">
          <option v-for="cat in categories" :key="cat.id">
            {{ cat.name }}
          </option>
        </select>
        <label for="floatingInput">Category</label>
      </div>
      <div class="form-floating">
        <input
          type="number"
          class="form-control"
          id="floatingInput"
          v-model="stock"
        />
        <label for="floatingInput">Stock</label>
      </div>
      <div class="form-floating">
        <input
          type="number"
          step="0.01"
          class="form-control"
          id="floatingInput"
          v-model="price"
        />
        <label for="floatingInput">Price in Rs.</label>
      </div>
      <div class="form-floating">
        <input
          type="date"
          class="form-control"
          id="floatingInput"
          v-model="manufacture_date"
        />
        <label for="floatingInput">Manufature Date </label>
      </div>
      <div class="form-floating">
        <input
          type="date"
          class="form-control"
          id="floatingInput"
          v-model="expiry_date"
        />
        <label for="floatingInput">Expiry Date </label>
      </div>
      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="floatingInput"
          v-model="units"
        />
        <label for="floatingInput">Units (kgs, ltrs, etc.)</label>
      </div>
      <div class="form-floating">
        <input
          type="number"
          class="form-control"
          id="floatingInput"
          v-model="quantity"
        />
        <label for="floatingInput">Quantity (kg, ltr, etc.)</label>
      </div>
      <div class="form-floating">
        <input
          type="number"
          class="form-control"
          id="floatingInput"
          v-model="sold"
        />
        <label for="floatingInput"># Sold</label>
      </div>

      <p></p>
      <button
        class="btn btn-outline-success w-100 py-2"
        type="submit"
        v-if="action == 'add'"
        @click.prevent="addProduct2"
      >
        Add Product
      </button>
      <button
        class="btn btn-outline-success w-100 py-2"
        type="submit"
        v-else
        @click.prevent="editProduct(this.$route.params.id)"
      >
        Edit Product
      </button>
    </form>
  </main>
</template>

<script>
export default {
  data() {
    return {
      action: window.location.href.split("/").pop(),
      categories: [],
      name: "",
      category: "",
      stock: 0,
      price: 0.0,
      manufacture_date: "",
      expiry_date: "",
      quantity: 0,
      units: "",
      sold: 0,
    };
  },
  methods: {
    addProduct2() {
      fetch("http://127.0.0.1:5000/api/products", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          name: this.name,
          category: this.category,
          stock: this.stock,
          price: this.price,
          manufacture_date: this.manufacture_date,
          expiry_date: this.expiry_date,
          quantity: this.quantity,
          units: this.units,
          sold: this.sold,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          this.$router.push("/products");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editProduct(p_id) {
      fetch("http://127.0.0.1:5000/api/products/".concat(p_id), {
        method: "PUT",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          name: this.name,
          category: this.category,
          stock: this.stock,
          price: this.price,
          manufacture_date: this.manufacture_date,
          expiry_date: this.expiry_date,
          quantity: this.quantity,
          units: this.units,
          sold: this.sold,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          this.$router.push("/products");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getProductInfo(p_id) {
      fetch("http://127.0.0.1:5000/api/products/".concat(p_id), {
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
          //console.log(data["name"]);
          this.name = data["name"];
          this.category = data["category"];
          this.stock = data["stock"];
          this.price = data["price"];
          this.manufacture_date = data["manufacture_date"];
          this.expiry_date = data["expiry_date"];
          this.quantity = data["quantity"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCategories() {
      fetch("http://127.0.0.1:5000/api/categories", {
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
          this.categories.push(...data);
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getCategories();
    if (this.action != "add") {
      this.getProductInfo(this.$route.params.id);
    }
  },
};
</script>

<style></style>
