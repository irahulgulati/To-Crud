<template>
  <div id="app container">
    <patients v-bind:patientdata="patientdata" v-on:delrecord="deleteRecord" />
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import patients from "../components/patients.vue";
import axios from "axios";
export default {
  name: "App",
  components: {
    patients
  },
  data() {
    return {
      patientdata: [],
      error: ""
    };
  },
  methods: {
    fetchCustomers() {
      this.error = "Fetching records";
      axios
        .get("http://192.168.99.100/api/patients")
        .then(res => {
          try {
            if (res.status == 200) {
              this.error = "";
              this.patientdata = res.data;
            } else if (res.status == 202) {
              this.error = "";
              let _tmpList = [];
              for (let i = 0; i < res.data.length; i++) {
                _tmpList.push(JSON.parse(res.data[i]));
              }
              this.patientdata = _tmpList;
            }
          } catch (e) {
            console.log(e);
          }
        })
        .catch(
          () =>
            (this.error = "umm! looks like we have a problem getting records.")
        );
    },
    deleteRecord(details) {
      axios
        .delete(`http://192.168.99.100/api/patients/${details.name}`, {
          data: {
            name: details.name,
            id: details.id
          }
        })
        .then(
          res => {
            try {
              // this.patientdata = this.patientdata.filter(
              //   patientdata => patientdata.id !== id
              // );
              if (res.status == 200) {
                this.patientdata = this.patientdata.filter(
                  patientdata => patientdata.name !== details.name
                );
                this.error = res.data.msg;
              } else {
                this.error = "Something Went wrong, we will be right back";
                console.log("Error");
              }
            } catch (e) {
              this.error = "Something Went wrong, we will be right back";
              console.log(e);
            }
          }

          // (this.patientdata = this.patientdata.filter(
          //   patientdata => patientdata.id !== id
          // ))
          // console.log(this.patientdata)
        )
        .catch(() => (this.error = "Error deleting record, please try later"));
    }
  },
  created: function() {
    this.fetchCustomers();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
