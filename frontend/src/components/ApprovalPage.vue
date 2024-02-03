<template>
  <div class="d-flex justify-content-center">
    <h2>Store Managers Pending Approval</h2>
  </div>
  <div class="d-flex justify-content-center">
    <button type="button" class="btn btn-success" @click.prevent="approveAll">
      Approve All
    </button>
  </div>
  <div
    class="row justify-content-center row-cols-1 row-cols-md-2 mb-2 text-center"
  >
    <div
      class="card mb-4 rounded-3 shadow-sm center"
      style="width : 50rem;"
      v-for="approval in approvals"
      :key="approval.id"
    >
      <div class="card-header py-3">
        <h4 class="my-0 fw-normal">{{ approval.id }} | {{ approval.name }}</h4>
      </div>
      <div class="card-body">
        <h5 class="card-title pricing-card-title">{{ approval.email }}</h5>
        <button
          type="button"
          class="btn btn-success mr-1"
          @click.prevent="actionApproval('approve', approval.id)"
        >
          Approve
        </button>
        <button
          type="button"
          class="btn btn-danger m-2"
          @click.prevent="actionApproval('reject', approval.id)"
        >
          Reject
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      approvals: [],
      action: "",
    };
  },
  methods: {
    getPendingApprovals() {
      fetch("http://127.0.0.1:5000/api/approvals", {
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
          this.approvals.push(...data);
          //console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    actionApproval(act, id) {
      const path = "http://127.0.0.1:5000/api/approvals/".concat(id);
      fetch(path, {
        method: "PUT",
        //mode: "cors",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("accessToken"),
        },
        body: JSON.stringify({
          action: act,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          alert(data['msg']);
          //eslint-disable-next-line
          //window.top.location = window.top.location;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    approveAll() {
      fetch("http://127.0.0.1:5000/api/approvals", {
        method: "PUT",
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
          //eslint-disable-next-line
          window.top.location = window.top.location;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getPendingApprovals();
  },
};
</script>

<style>
.themed-grid-col {
  padding-top: 15px;
  padding-bottom: 15px;
  background-color: rgba(86, 61, 124, 0.15);
  border: 1px solid rgba(86, 61, 124, 0.2);
}
</style>
