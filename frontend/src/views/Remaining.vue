<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <p style="color: white;font-weight: 600;font-size: 20px;position: relative; top: -2pc;">ร้านค้าที่ยังไม่ถูกจับฉลาก หมวด{{ this.dropDownText }}</p>
        <div class="table-container">
          <table v-if="length!=0" class="shop-info-table">
          <thead>
            <tr>
              <th style="text-align: center;width: 40%;">ชื่อ</th>
              <th style="text-align: center;width: 55%;">รายละเอียด</th>
              <th style="text-align: center;"></th>
              <!-- Add more headers as needed -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="(info, index) in shopInfo" :key="index">
              <td>{{ info.name }}</td>
              <td>{{ info.description }}</td>
              <td><p class="delete" @click="deleteShop(info.id)">-</p></td>
            </tr>
          </tbody>
        </table>
        <p v-else style="color: white;text-align: center;font-size: 2pc;">-</p>
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
      }

    },
    methods: {
      fetchData(){
        this.dropDownID = localStorage.getItem('dropDownID');
        this.dropDownText = localStorage.getItem('dropDownText');
        axios.get("http://localhost:80/api/shops/tag/"+this.dropDownID)
          .then((res)=>
            {this.shopInfo = res.data;
            this.length = res.data.length;}
          )
      },
      deleteShop(shopID){
        console.log("delete shop with ID: "+shopID)
        this.fetchData();
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
  color: #FF472E;
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

.info-frame{
  border-radius: 40px;
  color: #ffffff;
  border: 1.6px solid #ffffff ;
  padding: 11px 10px 11px 10px;
  font-size: 17px;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 39pc;
  height: 3.5pc;
  overflow: auto;
}
.table-container{
  width: 75vw;
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

  .shop-info-table td:hover {
    background-color: #101010;
  }

</style>
