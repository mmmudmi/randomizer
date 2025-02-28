<template>
  <div class="page">
  <Navbar :dropDownID="dropDownID" :dropDownText="dropDownText" />
    <div class="content">
      <div class="info">
        <div style="display: flex; align-items: center;">
          <v-text-field label="Category name to add" single-line v-model="tag_input" variant="solo" style="width: 60vw;" append-inner-icon="mdi-plus" @input="search_similar()" @click:append-inner="addTag()">
          </v-text-field>
        </div>

        <div class="table-container">
          <table v-if="length!=0" class="shop-info-table">
          <thead>
            <tr>
              <th style="text-align: center;">All Categories ({{ this.length }})</th>
              <th style="text-align: center;width: 30%;">Shops</th>
              <th style="text-align: center;width: 1%;"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(info, index) in tagsInfo" :key="index">
              <td>
                <p style="cursor: pointer;" @click="pick_tag(info.id,info.name)">{{info.name}}</p>
              </td>
              <td style="text-align: center;">
                {{info.count}}
              </td>
              <td class="delete" @click="deleteTag(info.id)">x</td>
            </tr>
          </tbody>
        </table>
        <p v-else style="color: grey;text-align: center;font-size: 1.5pc;">No categories available</p>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import axios from 'axios';
  export default {
    name: "Main",
    components: {Navbar },
    data(){
      return{
        dropDownID: null,
        tagsInfo: {},
        length: 0,
        tag_input: "",
      }

    },
    methods: {
      fetchData(){
        this.dropDownID = localStorage.getItem('dropDownID');
        axios.get("/api/tagsInfo/")
          .then((res)=> {
            this.tagsInfo = res.data;
            this.length = res.data.length;
          })
      },
      seperate_line(text){
        return text.split('\n')
      },
      addTag(){
        axios.post("/api/tag/"+this.tag_input)
          .then((res)=> {
            window.location.reload(true);
          })
      },
      deleteTag(id){
        axios.delete("/api/tags/"+id)
          .then((res)=> {
            if (localStorage.getItem('dropDownID') == id) {
              localStorage.setItem('dropDownText', "Select Category")
              localStorage.removeItem('dropDownID')
              window.location.reload(true);
            } 
            window.location.reload(true);
          })
      },
      search_similar(){
        if (this.tag_input.length == 0) {
          this.fetchData()
        } else {
          const filteredList = this.tagsInfo.filter(obj => obj.name.includes(this.tag_input));
          this.tagsInfo = filteredList
        }
      },
      pick_tag(id, name){
        localStorage.setItem('dropDownText', name)
        localStorage.setItem('dropDownID', id)
        window.location.reload(true);
      } 
    },
    beforeMount() {
      this.fetchData();
    },

  }
</script>

<style scoped>
.page {
  background-color: black;
  width: 100%;
  height: 100vh;  
  display: flex;
  flex-direction: column;
}
.delete{
  color: white;
  text-align: center;
  cursor: pointer;
}
.delete:hover{
  background-color: #FF472E;
}

.content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

  .info {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .add-btn {
    border-radius: 10px;
    background-color: #FF922E;
    color: #ffffff;
    padding: 10px 15px 10px 15px;
    font-size: 20px;
    font-weight: 800;
    transition:  0.3s ease;
    width: 6pc;
    margin: 0.5pc;
  }

  .table-container{
    width: 60vw;
    height: 63vh;
    overflow: scroll;
  }
  .shop-info-table {
      width: 100%;
      border-collapse: collapse;
    }

  .shop-info-table th, .shop-info-table td {
    border: 1.1px solid #ffffff;
    text-align: left;
    padding: 8px;
  }

  .shop-info-table th {
    background-color: #ffffff;
    color: rgb(0, 0, 0);
    position: sticky;
    top: 0;
    z-index: 1;
  }

  .shop-info-table td {
    color: white;
    overflow: auto;
  }

  .single-line {
    white-space: nowrap;
    overflow-x: scroll;
    width: 100%; /* Optionally, set a specific width */
  }
  .v-text-field__append-inner .v-icon {
    cursor: pointer;
  }
</style>
