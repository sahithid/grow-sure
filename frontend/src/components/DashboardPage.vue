<template>
  <div>
    <div class="d-flex justify-content-center">Dashboard</div>
    Dashboard
    <button
      class="btn btn-outline-primary my-2 my-sm-0"
      type="submit"
      v-if="role == 'manager'"
      @click.prevent="exportCSV"
    >
      Product Summary
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      role: localStorage.getItem("role"),
    };
  },
  methods: {
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
          alert(data['msg']);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
