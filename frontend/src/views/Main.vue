<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">
      <div class="info">
        <v-alert v-if="showCopySuccess" text="Copied to clipboard!" type="success" style="position: fixed; top: 1pc; z-index: 10;"></v-alert>
        <button v-if="isDrawing" class="yellow-btn" @click="random()">สุ่มร้านค้า</button>
        <div v-else class="show-result" >
          <button class="info-frame" @click="copyToClipboard(this.name)">{{ this.name }}</button>
          <button class="info-frame" @click="copyToClipboard(this.description)">{{ this.description }}</button>
          <div>
            <button class="dialog-btn" @click="random()"> จับใหม่ </button>
            <button class="dialog-btn" style="background-color: #7FB02F;" @click="confirmDrawing()"> ยืนยัน </button>
          </div>
        </div>
        <DeleteAll />
      </div>
    </div>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import DeleteAll from '@/components/DeleteAll.vue'
  import axios from 'axios';
  export default {
    name: "Main",
    components: {Navbar,DeleteAll},
    data(){
      return{
        dropDownID: null,
        isDrawing: true,
        showCopySuccess: false,
        name: "",
        description: "",
        currentShopID: null,
      }

    },
    methods: {
      random(){
        this.dropDownID = localStorage.getItem('dropDownID');
        if (this.dropDownID == null) {
          alert("เลือกหมวดร้านค้าก่อนกดสุ่ม")
        } else {
          console.log(this.dropDownID)
          axios.get('http://localhost:80/api/shops/draw/tag/'+this.dropDownID)
            .then((res) => {
              this.name = res.data.name;
              this.description = res.data.description;
              this.currentShopID = res.data.id;
              this.isDrawing = false;
            })

        }
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
          }, 600);
        } catch (err) {
          console.error('Unable to copy to clipboard', err);
        }

        document.body.removeChild(textArea);
      },
      confirmDrawing(){
        axios.put("http://localhost:80/api/shops/confirm/draw/"+this.currentShopID)
          .then((res)=>{
          })
        this.isDrawing = true;
      },
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

.info-frame{
  border-radius: 40px;
  color: #ffffff;
  border: 1.6px solid #ffffff ;
  padding: 11px 10px 11px 10px;
  font-size: 17px;
  margin: 0.5pc;
  transition:  0.3s ease;
  width: 39pc;
  height: 3.5pc;
  overflow: scroll
}
.info-frame:hover{
  background-color: #ffffff;
  color: rgb(0, 0, 0);
}

.yellow-btn{
  border-radius: 40px;
  background-color: #FF922E;
  color: #ffffff;
  padding: 12px 17px 12px 17px;
  font-size: 30px;
  font-weight: 800;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 15pc;
}
.yellow-btn:hover{
  background-color: #ff7b00;
  font-size: 32px;
  width: 16pc;
}
.show-result{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; /* Center text horizontally */
  height: 100%; }

.dialog-btn{
  border-radius: 40px;
  /* 7FB02F */
  background-color: #FF472E;
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
}
</style>
