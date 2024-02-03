<template>
  <nav class="navbar navbar-dark navbar-expand-md mb-4">
    <div class="container-fluid">
      <a class="navbar-brand" href="/" style="font-family: Monaco"
        ><img alt="Logo" src="../assets/plant.png" width="20" height="30"/>GROW-<i>sure</i></a
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link" href="/login" v-if="!visible">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/register" v-if="!visible">Sign Up</a>
          </li>
        </ul>
      </div>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link" href="/products" v-if="visible">Products</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/categories" v-if="visible">Categories</a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              href="/approvals"
              v-if="visible && role == 'admin'"
              >Approvals</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" :href="cart" v-if="visible && role == 'user'"
              >Cart</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" :href="orders" v-if="visible && role == 'user'"
              >Orders</a
            >
          </li>
          <li></li>
        </ul>
        <h6
          class="nav-item d-flex flex-row-reverse"
          style="color: rgb(226, 237, 247); font-family: Monaco"
          v-if="visible"
        >
          Hi, {{ user_name }}
        </h6>
        &nbsp;&nbsp;&nbsp; 
        <button
          class="btn btn-outline-success"
          type="submit"
          v-if="visible"
          @click.prevent="logout"
        >
          Logout
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      cart: "/cart/".concat(localStorage.getItem("user_id")),
      orders: "/orders/".concat(localStorage.getItem("user_id")),
      role: localStorage.getItem("role"),
      user_name: localStorage.getItem("user_name"),
    };
  },
  computed: {
    visible() {
      return localStorage.getItem("accessToken") == null ? 0 : 1;
    },
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({ path: "/login" });
    },
  },
};
</script>

<style>
.navbar {
  background-color: #2b6519;
}
</style>
