<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <p v-if="!no_tag_id" style="color: white;font-weight: 600;font-size: 20px;position: relative; top: -2pc;">ร้านค้าที่ยังไม่ถูกจับฉลาก หมวด{{ this.dropDownText }}</p>
        <v-alert v-else text="เลือกหมวดหมู่ร้านค้าก่อน" type="error" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>

        <div class="table-container">
          <table v-if="length!=0" class="shop-info-table">
          <thead>
            <tr>
              <th style="text-align: center;width: 40%;">ชื่อ</th>
              <th style="text-align: center">รายละเอียด</th>
              <th style="text-align: center;width: 1%;"></th>
              <!-- Add more headers as needed -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="(info, index) in shopInfo" :key="index">
              <td>
                <div v-if="info.shop_count==1">{{ info.name }}</div>
                <div v-else>
                  <p v-for="(line, i) in this.seperate_line(info.name)" :key="i">{{ i+1 }}. {{ line }}</p>
                </div>
              </td>
              <td>
                <div v-if="info.shop_count==1">
                  {{ info.description }}
                </div>
                <div v-else>
                  <p  v-for="(line, i) in this.seperate_line(info.description)" :key="i">- {{ line }}</p>
                </div>
              </td>
              <td class="delete" @click="deleteShop(info.id)">x</td>
            </tr>
          </tbody>
        </table>
        <p v-else-if="!no_tag_id" style="color: white;text-align: center;font-size: 2pc;">-</p>
        <DeleteAllInThisType />
        </div>
      </div>
    </div>
    <p style="color: white;position: relative; left: 1.5pc;bottom: 1.5pc;">เหลือ {{ this.length }} ร้านค้า</p>

  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import DeleteAllInThisType from '@/components/DeleteAllInThisType.vue'
  import DeleteShop from '@/components/DeleteShop.vue'

  import axios from 'axios';
  export default {
    name: "Main",
    components: {Navbar,DeleteAllInThisType,DeleteShop},
    data(){
      return{
        dropDownText: "",
        dropDownID: null,
        shopInfo: {},
        length: 0,
        no_tag_id: false,
      }

    },
    methods: {
      fetchData(){
        this.dropDownID = localStorage.getItem('dropDownID');
        if (!this.dropDownID) {this.no_tag_id = true}
        this.dropDownText = localStorage.getItem('dropDownText');
        axios.get("/api/shops/tag/"+this.dropDownID)
          .then((res)=> {
            this.shopInfo = res.data;
            this.length = res.data.length;
            console.log(res.data)
          })
      },
      seperate_line(text){
        return text.split('\n')
      },
      deleteShop(shopID){
        axios.delete("/api/shops/"+shopID)
          .then((res)=>
            this.fetchData()
          )
      },
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


.table-container{
  width: 90vw;
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
</style>
