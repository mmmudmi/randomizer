<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <v-alert v-if="showCopySuccess" text="เพิ่มร้านค้าสำเร็จ" type="success" style="position: fixed; top: 1pc; z-index: 10;"></v-alert>
        <v-textarea
        v-model="input"
        label="ชื่อ คำอธิบาย"
        single-line
        class="custom-textarea"
      ></v-textarea>
      <div>
          <button class="dialog-btn" @click="prep()"> + เพิ่ม </button>
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
    components: {Navbar},
    data(){
      return{
        input: "",
        shops: [],
        showCopySuccess: false,
      }
    },
    methods: {
      prep(){
        this.shops = [];
        for (let line of this.input.split('\n')) {
          let split = line.split('\t')
          this.shops.push({"name":split[0],"description":split[1]})
        }
        this.add()
      },
      add(){
        let data = {
          "shops" : this.shops,
          "tag_id": localStorage.getItem('dropDownID')
        }
        console.log(data)

        axios.post("http://localhost:80/api/shops/",data)
          .then ((res) => {
            this.input = "";
            this.showCopySuccess = true;
            setTimeout(() => {
              this.showCopySuccess = false;
            }, 600);
          })
      }
    }

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
.custom-textarea {
  color: rgb(255, 255, 255);
  /* border: 1px solid #ffffff; */
  border-radius: 5px;
  font-size: 16px;
  width: 70vw;
  /* background-color: rgb(255, 255, 255); */
  /* border: 1.6px dashed #ffffff ; */
}
.dialog-btn{
  border-radius: 40px;
  background-color: #FF922E;
  color: #ffffff;
  padding: 10px 15px 10px 15px;
  font-size: 16px;
  font-weight: 800;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 7pc;
  margin: 0.5pc;
}
.dialog-btn:hover{
  font-size: 17px;
  width: 8pc;
  background-color: #ff7b00;

}
</style>
