<template>
  <div class="d-flex justify-content-center">
    <h2>Your Shopping Cart</h2>
  </div>
  <br />
  <div
    class="row justify-content-center row-cols-1 row-cols-md-1 mb-2 text-center"
  >
    <div
      class="card mb-4 rounded-3 shadow-sm center"
      style="width: 50rem"
      v-for="(item, index) in cart_items"
      :key="index"
    >
      <div class="card-header py-3">
        <h4 class="my-0 fw-normal">{{ item.name }} | ({{ item.category }})</h4>
      </div>
      <div class="card-body">
        <h5 class="card-title pricing-card-title"></h5>
        <ul class="list-unstyled mt-3 mb-4">
          <li>Rs. {{ item.price }}</li>
          <li>Quantity: {{ item.amount_to_buy }}</li>

          <li v-if="input_visible">
            <div class="d-flex justify-content-center">
              <div class="form-floating">
                <input
                  type="number"
                  class="form-control text-center"
                  style="width: 5rem"
                  id="floatingInput"
                  v-model="item.amount_to_buy"
                />
                <label class="text-center" for="floatingInput">Quantity</label>
              </div>
            </div>
          </li>
        </ul>
        <button
          type="button"
          class="btn btn-outline-success m-2"
          v-if="!input_visible"
          @click.prevent="edit(true)"
        >
          Edit
        </button>
        <button
          type="button"
          class="btn btn-outline-success m-2"
          v-if="input_visible"
          @click.prevent="edit(false)"
        >
          Save
        </button>
        <button
          type="button"
          class="btn btn-outline-danger m-2"
          @click.prevent="removeItem(item.id)"
        >
          Remove
        </button>
      </div>
    </div>
  </div>

  <div class="d-flex justify-content-center" v-if="cart_items.length != 0">
    <h3>Total - Rs. {{ calculateTotal() }}</h3>
  </div>
  <div class="d-flex justify-content-center">
    <button
      type="button"
      class="btn btn-success"
      v-if="cart_items.length != 0"
      @click.prevent="buyCart"
    >
      Buy All
    </button>
    <button
      type="button"
      class="btn btn-outline-success"
      v-else
      @click="$router.push('/products')"
    >
      Add to Cart +
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cart_items: [],
      input_visible: false,
    };
  },
  methods: {
    calculateTotal() {
      let t = 0;
      for (let i = 0; i < this.cart_items.length; i++) {
        t += this.cart_items[i].price * this.cart_items[i].amount_to_buy;
      }
      return t;
    },
    getItems() {
      const u_id = localStorage.getItem("user_id");
      fetch("http://127.0.0.1:5000/api/cart/".concat(u_id), {
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
          this.cart_items.push(...data);
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    removeItem(item_id) {
      if (confirm("Are you sure you want to delete this item? ")) {
        const u_id = localStorage.getItem("user_id");
        const path = "http://127.0.0.1:5000/api/cart/".concat(
          u_id,
          "/",
          item_id
        );
        fetch(path, {
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
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    edit(flag) {
      this.input_visible = flag;
    },
    buyCart() {
      if (confirm("Confirm to place an order")) {
        const u_id = localStorage.getItem("user_id");
        const path = "http://127.0.0.1:5000/api/orders/".concat(u_id);
        fetch(path, {
          method: "POST",
          //mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            Authorization: "Bearer " + localStorage.getItem("accessToken"),
          },
          body: JSON.stringify({
            total: this.calculateTotal(),
          }),
        })
          .then((res) => res.json())
          .then((data) => {
            alert(data["msg"]);
          })
          .catch((error) => {
            console.log(error);
          });
        //now clear the cart
        this.deleteEntireCart();
      }
    },
    deleteEntireCart() {
      const u_id = localStorage.getItem("user_id");
      const path = "http://127.0.0.1:5000/api/cart/".concat(u_id);
      fetch(path, {
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
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getItems();
    this.calculateTotal();
  },
};
</script>

<style>
.card {
  width: 18rem;
}
</style>
