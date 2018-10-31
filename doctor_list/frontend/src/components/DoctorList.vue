<template>
  <div>
    <h1>Doctor List</h1>
    <div v-for="doc in doctor_list">
       <b-button @click = "getPatients(doc)">
         {{ doc[0] }}
       </b-button>
    </div>
    <div>
      <h1>Patient List</h1>
       <div v-for="patient in patient_list">
         {{ patient }}
       </div>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'DoctorList',
  data() {
    return {
      doctor_list: [],
      patient_list:[]
    }
  },
  created() {
     this.get_doctor_list();
  }, 
  methods: {
    get_doctor_list() {
        this.$http.get('api/doclist').then(response => {
            console.log("doclist grabbed!");
            this.temp_list = response.body['doc_list'];
            for (var i = 0; i < this.temp_list.length; i++) {
              this.doctor_list.push([this.temp_list[i], i + 1]);
            }
            console.log(this.doctor_list)
        }, error => {
            console.log(error);
        });
    },
   
    getPatients(doc) {
      this.$http.get('api/patientlist/' + doc[1]).then(response => {
        console.log("patient list grabbed!!!");
        this.patient_list = []
        this.temp_patient_list = response.body['patient_list']
        for (var i = 0; i < this.temp_patient_list.length; i++) {
           this.patient_list.push(this.temp_patient_list[i]);
        } 
      }, error => {
         console.log(error);
      });
    }
  },
}
</script>
