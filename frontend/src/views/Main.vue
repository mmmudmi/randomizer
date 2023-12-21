<template>
  <div class="page">
    <Navbar v-model="dropDownID" />
    <div class="content">

      <div class="info">
        <v-alert v-if="showCopySuccess" text="Copied to clipboard!" type="success" style="position: fixed; top: 1pc; z-index: 10;"></v-alert>
        <v-alert v-if="showCopyError" text="ไม่มีร้านค้าให้จับฉลาก" type="error" style="position: fixed; top: 1pc; z-index: 10;"></v-alert>
        <button v-if="isDrawing" class="yellow-btn" @click="random()">สุ่มร้านค้า</button>
        <div v-else class="show-result" >
          <div v-if="this.shop_count==1">
            <div>
              <button class="info-frame" style="height: 3.5pc;" @click="copyToClipboard(this.name)">{{ this.name }}</button>
              <button v-if="this.name!=null" @click="readText(this.name)">
                <i class="gg-play-button-o" style="cursor: pointer;color: white; position: relative; top: 0.3pc;"></i>
              </button>
            </div>
            <div>
              <button class="info-frame" style="height: 3.5pc;" @click="copyToClipboard(this.description)">{{ this.description }}</button>
              <button v-if="this.name!=null" @click="readText(this.description)">
                <i class="gg-play-button-o" style="cursor: pointer;color: white; position: relative; top: 0.3pc;"></i>
              </button>
            </div>
          </div>
          <div v-else>
            <div>
              <button class="info-frame" @click="copyToClipboard(this.each_shop[0])">
                <p class="single-line" v-for="(line, i) in this.each_shop" :key="i">{{ i+1 }}. {{ line }}</p>
              </button>
              <button v-if="this.name!=null" @click="readText(this.name)">
                <i class="gg-play-button-o" style="cursor: pointer;color: white; position: relative; top: 0.3pc;"></i>
              </button>
            </div>
            <div>
              <button class="info-frame" @click="copyToClipboard(this.each_description[0])">
                <p class="single-line" v-for="(line, i) in this.each_description" :key="i">{{ i+1 }}. {{ line }}</p>
              </button>
              <button v-if="this.name!=null" @click="readText(this.description)">
                <i class="gg-play-button-o" style="cursor: pointer;color: white; position: relative; top: 0.3pc;"></i>
              </button>
            </div>
          </div>
          <div>
            <button class="dialog-btn" @click="random()"> จับใหม่ </button>
            <button class="dialog-btn" style="background-color: #7FB02F;" @click="confirmDrawing()"> ยืนยัน </button>
          </div>
        </div>
        <DeleteAll />
      </div>
    </div>
    <p style="color: white;position: relative; left: 1.5pc;bottom: 1.5pc;font-size: 13px;cursor: pointer;" @click="copyToClipboard(this.prevDrawn)">จับล่าสุด: {{ this.prevDrawn }}</p>
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
        showCopyError: false,
        name: null,
        shop_count: 1,
        description: null,
        currentShopID: null,
        prevDrawn: localStorage.getItem('recentDrawn'),
        each_shop: [],
        each_description: [],
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
              this.shop_count = res.data.shop_count;
              this.seperate_line();
            })
            .catch((error) => {
              this.showCopyError = true;
                setTimeout(() => {
                  this.showCopyError = false;
                }, 1000);
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
          }, 700);
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
        this.prevDrawn = this.name;
        localStorage.setItem('recentDrawn',this.prevDrawn)
      },
      readText(textToRead) {      
        const synth = window.speechSynthesis;
        const utterance = new SpeechSynthesisUtterance(textToRead);
        utterance.lang = 'th-TH';
        utterance.rate = 1.4;
        synth.speak(utterance);
      },
      seperate_line(){
        this.each_shop = this.name.split('\n')
        this.each_description = this.description.split('\n')
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
  /* height: 3.5pc; */
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
.gg-play-button-o:hover{
  border: #FF472E;border: 2px solid;
}
</style>
