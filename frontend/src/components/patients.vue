<template>
  <div class="patientcontainer">
    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Location</th>
          <th scope="col">Street Name</th>
          <th scope="col">Status</th>
        </tr>
      </thead>
      <tbody v-if="patientdata.length!==0">
        <tr v-for="patient in patientdata" v-bind:key="patient.name">
          <td>{{patient.name}}</td>
          <td>{{patient.location}}</td>
          <td>{{patient.streetname}}</td>
          <td>{{patient.status}}</td>
          <button @click="$emit('delrecord', {'name':patient.name,'id':patient.id})" class="del">x</button>
        </tr>
      </tbody>
      <tbody v-else>
        <tr>
          <td>
            <small>
              <i>Names will appear here</i>
            </small>
          </td>
          <td>
            <small>
              <i>Locations will appear here</i>
            </small>
          </td>
          <td>
            <small>
              <i>Streets will appear here</i>
            </small>
          </td>
          <td>
            <small>
              <i>Status will appear here</i>
            </small>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "patients",
  data() {
    return {
      name: ""
    };
  },
  props: ["patientdata"]
};
</script>

<style scoped>
.del {
  background: #212529;
  color: #fff;
  border: none;
  padding-right: 6px;
  cursor: pointer;
  float: right;
  margin-top: 10px;
  margin-right: 12px;
  text-decoration: none;
}
.patientcontainer {
  position: relative;
}
.del:hover {
  background: rgb(224, 20, 20);
  /* color: #000; */
  cursor: pointer;
  size: 200%;
}
</style>
