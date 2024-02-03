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
        class="w-30 btn btn-lg btn-outline-success"
        v-show="role == 'admin'"
        @click="$router.push('/categories/add')"
      >
        Add Category +
      </button>
      <button
        type="button"
        class="w-30 btn btn-lg btn-outline-success"
        v-show="role == 'manager'"
        @click="$router.push('/categories/request/add')"
      >
        Request to Add Category +
      </button>
    </div>
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      <div
        class="card mb-4 rounded-3 shadow-sm"
        v-for="category in categories"
        :key="category.id"
      >
        <div class="card-header py-3">
          <h4 class="my-0 fw-normal">{{ category.name }}</h4>
        </div>
        <div class="card-body">
          <h5 class="card-title pricing-card-title"></h5>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-success"
            v-show="role == 'admin'"
            @click="$router.push('/categories/edit/'.concat(category.id))"
          >
            Edit
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-danger"
            v-show="role == 'admin'"
            @click.prevent="removeCategory(category.id)"
          >
            Remove
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-secondary"
            v-show="role == 'manager'"
          >
            Request to Edit
          </button>
          <button
            type="button"
            class="w-50 btn btn-lg btn-outline-secondary"
            v-show="role == 'manager'"
          >
            Request to Remove
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
      categories: [],
      name: "",
      id: "",
      role: localStorage.getItem("role"),
    };
  },
  methods: {
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
    // addCategory() {
    //   fetch("http://127.0.0.1:5000/api/categories", {
    //     method: "POST",
    //     //mode: "cors",
    //     headers: {
    //       "Content-Type": "application/json",
    //       "Access-Control-Allow-Origin": "*",
    //       Authorization: "Bearer " + localStorage.getItem("accessToken"),
    //     },
    //     body: JSON.stringify({
    //       name: this.name,
    //     }),
    //   })
    //     .then((res) => res.json())
    //     .then((data) => {
    //       console.log(data);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },
    removeCategory(c_id) {
      if (confirm("Are you sure you want to delete this?")) {
        fetch("http://127.0.0.1:5000/api/categories/".concat(c_id), {
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
            alert(data['msg']);
            //console.log(data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
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
          comp: "Category1",
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data["msg"]) {
            alert(data["msg"]);
          } else {
            this.categories = [];
            this.categories.push(...data);
          }
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getCategories();
  },
};
</script>

<style>
.container {
  max-width: 940px;
}

.pricing-header {
  max-width: 600px;
}
</style>
