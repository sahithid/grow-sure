<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="signup">
      <h1 class="h3 mb-3 fw-normal">Sign Up</h1>

      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="floatingInput"
          placeholder="Username"
          v-model="name"
        />
        <label for="floatingInput">Username</label>
      </div>

      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          id="floatingEmail"
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

      <div class="form-floating">
        <select
          class="form-control"
          id="floatingSelect"
          placeholder="Role"
          v-model="role"
        >
          <option>user</option>
          <option>manager</option>
        </select>
        <label for="floatingInput">Role</label>
      </div>

      <p></p>
      <button class="btn btn-outline-success w-100 py-2" type="submit">
        Register
      </button>
    </form>
    <br />
    <div class="d-flex justify-content-center">
      Already a member? &nbsp; <a href="/login"> Login In </a>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      role: "",
    };
  },
  methods: {
    signup() {
      fetch("http://127.0.0.1:5000/api/register", {
        method: "POST",
        //mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({
          name: this.name,
          email: this.email,
          password: this.password,
          role: this.role,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          this.$router.push({ path: "/login" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    //this.signup();
  },
};
</script>

<style>
.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
