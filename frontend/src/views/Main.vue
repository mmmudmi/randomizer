<template>
  <div class="page">
    <Navbar :dropDownID="dropDownID" />
    <div class="content">
      <div class="info">
        <button class="yellow-btn">สุ่มร้านค้า</button>
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
    computed: {
    },
    components: {Navbar,DeleteAll},
    data(){
      return{
        dropDownID: 0,
      }
    },
    methods: {

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

</style>
