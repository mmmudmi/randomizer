<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <p style="color: white;font-weight: 600;font-size: 20px;position: relative; top: -2pc;">ลบล่าสุด หมวด{{ this.dropDownText }}</p>
        <div class="table-container">
          <table v-if="length!=0"  class="shop-info-table">
          <thead>
            <tr>
              <th style="text-align: center;width: 10%;">เวลา</th>
              <th style="text-align: center;width: 30%;">ชื่อ</th>
              <th style="text-align: center;">รายละเอียด</th>
              <th style="text-align: center;width: 1%;"></th>
              <!-- Add more headers as needed -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="(info, index) in shopInfo" :key="index">
              <td style="font-size: 12px;">{{ info.time_drawn }}</td>
              <td v-if="info.shop_count==1" @click="this.copyToClipboard(info.name)">{{ info.name }}</td>
              <td v-else @click="this.copyToClipboard(this.seperate_line(info.name)[0])">
                <div>
                  <p class="single-line" v-for="(line, i) in this.seperate_line(info.name)" :key="i">{{ i+1 }}. {{ line }}</p>
                </div>
              </td>
              <td v-if="info.shop_count==1" @click="this.copyToClipboard(info.description)">{{ info.description }}</td>
              <td v-else @click="this.copyToClipboard(this.seperate_line(info.description)[0])">
                <div>
                  <p class="single-line" v-for="(line, i) in this.seperate_line(info.description)" :key="i">{{ i+1 }}. {{ line }}</p>
                </div>
              </td>
              <td class="redraw" @click="this.redraw(info.id)">  <i class="gg-undo"></i></td>
            </tr>
          </tbody>
        </table>
        <p v-else style="color: white;text-align: center;font-size: 2pc;">-</p>
        </div>
        <EmptyDeleted />
      </div>
    </div>
    <p style="color: white;position: relative; left: 1.5pc;bottom: 1.5pc;">ลบไปแล้ว {{ this.length }} ร้านค้า</p>

  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import EmptyDeleted from '@/components/EmptyDeleted.vue'
  import axios from 'axios';
  export default {
    name: "Main",
    components: {Navbar,EmptyDeleted},
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
        axios.get("http://localhost:80/api/deleted/tag/"+this.dropDownID)
          .then((res)=> {
            this.shopInfo = res.data;
            this.shopInfo.sort((a, b) => {
              return new Date(b.time_drawn) - new Date(a.time_drawn);
            });
            this.length = res.data.length;
          })
      },
      redraw(shopID){
        axios.put("http://localhost:80/api/deleted/redraw/"+shopID)
          .then((res)=> {
            this.fetchData()
          })
      },
      seperate_line(text){
        return text.split('\n')
      },
    },
    beforeMount() {
      this.fetchData();
    },

  }
</script>

<style scoped>
.page {
  background-color: rgb(0, 0, 0);
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
    font-size: 14px;
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

  /* .shop-info-table td:hover {
    background-color: #101010;
  } */
.redraw{
  color: white;
  cursor: pointer;
}
.redraw:hover{
  background-color: #ffaf38;
}
</style>
