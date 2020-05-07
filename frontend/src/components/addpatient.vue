<template>
    <div class="container">
  <form @submit="addPatient">
    <div class="row">
      <div class="col-25">
        <label for="name">Name</label>
      </div>
      <div class="col-75">
        <input type="text" id="name" name="name" placeholder="Patient's name.." v-model="name" maxlength="25">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="loc">Location</label>
      </div>
      <div class="col-75">
        <input type="text" id="loc" name="lastname" placeholder="Patient's location" v-model="location" maxlength="15">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="street">Street Name</label>
      </div>
      <div class="col-75">
        <input type="text" id="street" name="lastname" placeholder="Patient's Street Address" v-model="streetname" maxlength="15">
      </div>
    </div>
    <div class="row">
      <div class="col-25">
        <label for="subject">Covid Status</label>
      </div>
      <div class="col-75">
        <input type="text" id="lname" name="lastname" placeholder="Patient's Covid Status" v-model="status" maxlength="10">
      </div>
    </div>
    <div class= "row" v-if="processing === true">
      <button class="btn btn-success btn-lg" id="disabledbtn" value="Processing" disabled>Processing</button>
    </div>
    <div class= "row" v-else>
      <button class="btn btn-success btn-lg" value="Create Record" >Create Record</button>
    </div>
  </form>
    </div>
</template>
<script>
export default {
    name: 'addpatient',
    data() {
        return {
            name: '',
            location: '',
            streetname:'',
            status:''
        }
        
    },
    props: ["processing"],
    methods: {
        addPatient(e){
            if(this.name !== ''&& this.location !== ''&& this.streetname !== ''&&this.status !== ''){
                const newPatient = {
                  name: this.name,
                  location:this.location,
                  streetname:this.streetname,
                  status:this.status
                }
                this.$emit('newPatient',newPatient)
                this.name = ''
                this.location= '',
                this.streetname='',
                this.status=''
            }
            else{
                alert("Please enter all the details")
            }
            e.preventDefault();

            // console.log(newPatient)
            

        }
    }
    
}
</script>
<style scoped>
#disabledbtn{
  cursor: wait;
}
.success {
    color: #fff;
}
input[type=text], select, textarea {
  width: 80%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
  color: #fff;
}

input[type=submit] {
  background-color: #42b983;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  float: right;
  margin-top:10px;
}

input[type=submit]:hover {
  background-color: #26b977;
}

.container {
  border-radius: 5px;
  background-color: #343a40;
  padding: 20px;
  position:relative;
}

.col-25 {
  float: left;
  width: 25%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 75%;
  margin-top: 6px;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .col-25, .col-75 {
    width: 100%;
    margin-top: 0;
  }
  input[type=submit] {
    width:80%;
    margin-top:20px;
    margin-left:auto;
    margin-right: auto;
  }
}
</style>