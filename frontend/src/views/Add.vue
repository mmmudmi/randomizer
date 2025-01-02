<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <v-alert v-if="showCopySuccess" text="เพิ่มร้านค้าสำเร็จ" type="success" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>
        <v-alert v-if="showCopyFail" text="ใส่ข้อมูลร้านค้าก่อนจ้า" type="warning" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>
        <v-alert v-if="no_chosen_tag_id" text="เลือกหมวดหมู่ร้านค้าก่อน" type="error" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>
        <v-text-field label="ชื่อ" single-line v-model="name_input" variant="solo" v-if="this.add_one_isActivate" style="width: 60vw;" @input="this.add_one_input_handle()"></v-text-field>
        <v-text-field label="คำอธิบาย" single-line v-model="description_input" variant="solo" v-if="this.add_one_isActivate" style="width: 60vw;"></v-text-field>
        <v-textarea
        v-model="shops_input"
        label="ชื่อ คำอธิบาย (ใส่หลายร้านพร้อมกันได้)"
        single-line
        class="custom-textarea"
        v-if="add_many_isActivate"
      ></v-textarea>
      <v-textarea
        v-model="group_input"
        label="ชื่อ คำอธิบาย (สำหรับร้านค้าที่ต้องการติดกัน)"
        single-line
        class="custom-textarea"
        v-if="add_group_isActivate"
      ></v-textarea>
      <div>
        <div>
          <!-- add one -->
          <button class="dialog-btn" @click="add_one_prep()" v-if="this.add_one_isActivate">+เพิ่ม</button>
          <button class="nonactivate-dialog-btn" @click="add_one_handle" v-else>เพิ่มทีละร้าน</button>
          <!-- add many -->
          <button class="dialog-btn" @click="add_many_prep()" v-if="this.add_many_isActivate"> + เพิ่ม </button>
          <button class="nonactivate-dialog-btn" @click="add_many_handle" v-else>เพิ่มหลายร้าน</button>
          <!-- add group -->
          <button class="dialog-btn" @click="add_group_prep()" v-if="this.add_group_isActivate">+เพิ่ม</button>
          <button class="nonactivate-dialog-btn" @click="add_group_handle" v-else>เพิ่มร้านติดกัน</button>
        </div>
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
        shops_input: "",
        group_input: "",
        name_input: "",
        description_input: "",
        shops: [],
        showCopySuccess: false,
        showCopyFail: false,
        no_chosen_tag_id: false,
        add_one_isActivate: false,
        add_many_isActivate: true,
        add_group_isActivate: false,
      }
    },
    methods: {
      add_many_handle(){
        this.add_one_isActivate = false;
        this.add_many_isActivate = true;
        this.add_group_isActivate = false;
      },
      add_many_prep(){
        this.no_tag_id_check();
        if (this.shops_input.length==0) {
          this.showCopyFail = true
          setTimeout(() => {
                this.showCopyFail = false;
              }, 1000);
        } else {
          this.shops = [];
          for (let line of this.shops_input.split('\n')) {
            let split = line.split('\t')
            if (split.length == 1 ) {
              this.shops.push({"name":split[0],"description":"-"})
            }else{
              this.shops.push({"name":split[0],"description":split[1]})
            }
          }
          this.add(this.shops)
        }
      },
      add_one_handle(){
        this.add_one_isActivate = true;
        this.add_many_isActivate = false;
        this.add_group_isActivate = false;
      },
      add_group_handle(){
        this.add_one_isActivate = false;
        this.add_many_isActivate = false;
        this.add_group_isActivate = true;
      },
      add(shops){
        let data = {
          "shops" : shops,
          "tag_id": localStorage.getItem('dropDownID')
        }
        axios.post("/api/shops/",data)
          .then ((res) => {
            this.shops_input = "";
            this.showCopySuccess = true;
            setTimeout(() => {
              this.showCopySuccess = false;
            }, 1000);
          })
      },
      no_tag_id_check(){
        if (!localStorage.getItem('dropDownID')) {
          this.no_chosen_tag_id = true;
          setTimeout(() => {
                this.no_chosen_tag_id = false;
              }, 1000);
        }
      },
      add_one_input_handle(){
        let split = this.name_input.split('\t')
        if (split.length > 1) {
          this.name_input = split[0]
          this.description_input = split[1]
        } 
      },
      add_one_prep(){
        this.no_tag_id_check();
        if (this.name_input.length==0 & this.description_input.length==0) {
          this.showCopyFail = true
          setTimeout(() => {
                this.showCopyFail = false;
              }, 1000);
          return;
        }
        let shops = []
        shops.push({"name":this.name_input,"description":this.description_input})
        this.add(shops)
        this.name_input = ""
        this.description_input = ""
      },
      add_group_prep(){
        this.no_tag_id_check();
        if (this.group_input.length==0) {
          this.showCopyFail = true
          setTimeout(() => {
                this.showCopyFail = false;
              }, 1000);
        } else {
          let shops = [];
          for (let line of this.group_input.split('\n')) {
            let split = line.split('\t')
            if (split.length == 1 ) {
              shops.push({"name":split[0],"description":"-"})
            }else{
              shops.push({"name":split[0],"description":split[1]})
            }
          }
          let data = {
            "shops" : shops,
            "tag_id": localStorage.getItem('dropDownID')
          }
          axios.post("/api/shops/group/",data)
            .then ((res) => {
              this.group_input = "";
              this.showCopySuccess = true;
              setTimeout(() => {
                this.showCopySuccess = false;
              }, 1000);
            })
        }
      }
      
    },
    beforeMount() {

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
  font-size: 20px;
  font-weight: 800;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 7pc;
  margin: 0.5pc;
}
.dialog-btn:hover{
  font-size: 22px;
  width: 8pc;
  background-color: #ff7b00;
}
.nonactivate-dialog-btn{
  border-radius: 40px;
  background-color: #3e3e3e;
  color: #ffffff;
  padding: 10px 15px 10px 15px;
  font-size: 14px;
  font-weight: 600;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 7pc;
  margin: 0.5pc;
}
.nonactivate-dialog-btn:hover{
  font-size: 15px;
  width: 8pc;
  background-color: #262626;
}
</style>
