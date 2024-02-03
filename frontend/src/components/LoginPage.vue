<template>
  <main class="form-signin w-100 m-auto">
      <form @submit.prevent="login">
        <h1 class="h3 mb-3 fw-normal">Login</h1>

        <div class="form-floating">
          <input
            type="email"
            class="form-control"
            id="floatingInput"
            placeholder="name@example.com"
            v-model="email"
          />
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating">
          <input
            type="password"
            class="form-control"
            id="floatingPassword"
            placeholder="Password"
            v-model="password"
          />
          <label for="floatingPassword">Password</label>
        </div>
        <button class="btn btn-primary w-100 py-2" type="submit">
          Sign in
        </button>
      </form>
      <br />
      <div class="d-flex justify-content-center">
        Don't have an account? &nbsp; <a href="/register"> Sign Up </a>
      </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
      fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          if (data["code"] == 200) {
            localStorage.setItem("accessToken", data["access_token"]);
            localStorage.setItem("role", data["role"]);
            localStorage.setItem("user_id", data["id"]);
            localStorage.setItem("user_name", data["name"]);
            if (data["role"] == "admin") {
              //window.location.reload();
              this.$router.push({ path: "/categories" });
            } else {
              //window.location.reload();
              this.$router.push({ path: "/products" });
            }
          } else {
            //window.location.reload();
            this.$router.push({ path: "/login" });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.btn {
  background-color: white !important;
  color: #2b6519 !important;
  border-color: #2b6519 !important;
}
.btn:hover,
.btn:active,
.btn:visited,
.btn:focus,
.btn:active:focus {
  background-color: #2b6519 !important;
  color: white !important;
  border-color: white !important;
}
</style>
