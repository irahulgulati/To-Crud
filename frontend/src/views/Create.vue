<template>
  <div class="about">
    <div class="codehandler" v-if="code">{{code}}</div>
    <addpatient v-bind:processing="processing" v-on:newPatient="createPatient" />
  </div>
</template>
<script>
import addpatient from "../components/addpatient.vue";
import axios from "axios";
export default {
  name: "create",
  components: {
    addpatient
  },
  data() {
    return {
      code: "",
      processing: "",
      patientdata: []
    };
  },
  methods: {
    createPatient(newPatient) {
      const { location, streetname, status } = newPatient;
      const name = newPatient.name.toLowerCase();
      this.code = "Processing request";
      this.processing = true;
      axios
        .get("http://192.168.99.100/api/patients")
        .then(() => {
          axios
            .post("http://192.168.99.100/api/patients", {
              name,
              location,
              streetname,
              status
            })
            .then(res => {
              if (res.data.name == "patient already exists") {
                this.code = "Patient already exists";
                this.processing = "";
              } else {
                this.patientdata = [...this.patientdata, res.data];
                this.processing = "";
                this.code = "Patient record added to database";
              }
              this.processing = "";
            })
            .catch(err => console.log(err));
        })
        .catch(() => {
          this.processing = "";
          this.code = "404! Connection timed out";
        });
    }
  }
};
</script>

