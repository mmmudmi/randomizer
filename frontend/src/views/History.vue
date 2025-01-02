<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <v-alert v-if="showCopySuccess" text="Copied to clipboard!" type="success" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>
        <p v-if="!no_tag_id" style="color: white;font-weight: 600;font-size: 20px;position: relative; top: -2pc;">ร้านค้าที่ถูกจับฉลากแล้ว หมวด{{ this.dropDownText }}</p>
        <v-alert v-else text="เลือกหมวดหมู่ร้านค้าก่อน" type="error" style="position: fixed; top: 5pc; z-index: 10;"></v-alert>

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
        <p v-else-if="!no_tag_id" style="color: white;text-align: center;font-size: 2pc;">-</p>
        </div>
        <RedrawAll />
      </div>
    </div>
    <p style="color: white;position: relative; left: 1.5pc;bottom: 1.5pc;">จับไปแล้ว {{ this.length }} ร้านค้า</p>

  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import RedrawAll from '@/components/RedrawAll.vue'
  import axios from 'axios';
  export default {
    name: "Main",
    components: {Navbar,RedrawAll},
    data(){
      return{
        dropDownText: "",
        dropDownID: null,
        shopInfo: {},
        length: 0,
        showCopySuccess: false,
        no_tag_id: false,
      }

    },
    methods: {
      fetchData(){
        this.dropDownID = localStorage.getItem('dropDownID');
        if (!this.dropDownID) {this.no_tag_id = true}
        this.dropDownText = localStorage.getItem('dropDownText');
        axios.get("/api/history/tag/"+this.dropDownID)
          .then((res)=> {
            this.shopInfo = res.data;
            this.shopInfo.sort((a, b) => {
              return new Date(b.time_drawn) - new Date(a.time_drawn);
            });
            this.length = res.data.length;
          })
      },
      deleteShop(shopID){
        this.fetchData();
      },
      redraw(shopID){
        axios.put("/api/shops/redraw/"+shopID)
          .then((res)=> {
            this.fetchData()
          })
      },
      copyToClipboard(text){
        const textArea = document.createElement('textarea');
        textArea.value = text;
        // Make the textarea out of viewport
        textArea.style.position = 'fixed';
        textArea.style.top = '0';
        textArea.style.left = '0';
        textArea.style.width = '2em';
        textArea.style.height = '2em';
        textArea.style.padding = '0';
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';
        textArea.style.background = 'transparent';

        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
          const successful = document.execCommand('copy');
          const message = successful ? 'Copied to clipboard!' : 'Failed to copy to clipboard';
          this.showCopySuccess = true;
          setTimeout(() => {
            this.showCopySuccess = false;
          }, 700);
        } catch (err) {
          console.error('Unable to copy to clipboard', err);
        }

        document.body.removeChild(textArea);
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

.shop-info-table td:hover {
  cursor: pointer;
  font-size: 15px;
}
.redraw{
  color: white;
  cursor: pointer;
}
.redraw:hover{
  background-color: #ffaf38;
}
</style>
