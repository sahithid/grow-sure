<template>
  <main class="form-signin w-100 m-auto">
    <form>
      <h1 class="h3 mb-3 fw-normal" v-if="action == 'add'">Add Category</h1>
      <h1 class="h3 mb-3 fw-normal" v-else>Edit Category</h1>

      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="floatingInput"
          v-model="name"
        />
        <label for="floatingInput">Category Name</label>
      </div>

      <p></p>
      <button
        class="btn btn-outline-success w-100 py-2"
        type="submit"
        v-if="action == 'add'"
        @click.prevent="addCategory"
      >
        Add Category
      </button>
      <button
        class="btn btn-outline-success w-100 py-2"
        type="submit"
        v-else
        @click.prevent="editCategory(this.$route.params.id)"
      >
        Edit Category
      </button>
    </form>
  </main>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      role: localStorage.getItem("role"),
      action: window.location.href.split("/").pop(),
    };
  },
  methods: {
    addCategory() {
      fetch("http://127.0.0.1:5000/api/categories", {
        method: "POST",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          name: this.name,
          approved: 1,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          this.$router.push("/categories");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editCategory(c_id) {
      fetch("http://127.0.0.1:5000/api/categories/".concat(c_id), {
        method: "PUT",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          name: this.name,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data["msg"]);
          this.$router.push("/categories");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCatInfo(c_id) {
      fetch("http://127.0.0.1:5000/api/categories/".concat(c_id), {
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
          console.log(data["name"]);
          this.name = data["name"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    if (this.action != "add") {
      this.getCatInfo(this.$route.params.id);
    }
  },
};
</script>

<style></style>
