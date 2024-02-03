<template>
  <div class="d-flex justify-content-center">
    <h2>Your Orders</h2>
  </div>
  <br />
  <div
    class="row justify-content-center row-cols-1 row-cols-md-1 mb-2 text-center"
  >
    <div
      class="card mb-4 rounded-3 shadow-sm center"
      v-for="(order, index) in orders"
      :key="order.id"
      style="width: 85rem;"
    >
      <div class="card-header py-3">
        <h4 class="my-0 fw-normal">
          <u>Order # {{ index + 1 }} - Rs. {{ order.total }}</u>
        </h4>
      </div>
      <div class="card-body">
        <h5 class="card-title pricing-card-title">{{ order.time }}</h5>
        <div class="row row-cols-3 row-cols-md-3 mb-2 text-center">
          <div
            class="card mb-4 rounded-3 shadow-sm center"
            v-for="item in order.items"
            :key="item.id"
          >
            <div class="card-header py-3">
              <h4 class="my-0 fw-normal">
                {{ item.name }} | {{ item.category }}
              </h4>
            </div>
            <div class="card-body">
              <ul class="list-unstyled mt-1 mb-1">
                <li>Rs. {{ item.price }}</li>
                <li>Quantity {{ item.amount_to_buy }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      orders: [],
    };
  },
  methods: {
    getOrders() {
      const u_id = localStorage.getItem("user_id");
      fetch("http://127.0.0.1:5000/api/orders/".concat(u_id), {
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
          this.orders.push(...data);
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getOrders();
  },
};
</script>

<style></style>
