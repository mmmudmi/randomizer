<template>
  <nav class="Navbar">
    <v-row align="center">
      <div>
        <button class="Navbar-btn" 
          :class="{'Navbar-btn Hightlighted': $route.name === 'main'}"
          @click="navigateTo('main')">จับฉลาก</button>
      </div>

      <div class="left-side-Navbar">
          <div class="dropdown">
            <button @click="dropDown()" class="dropbtn">
              {{ dropDownText }}
              <i class="fa fa-caret-down" style="position: absolute; right: 1.5pc;top: 1pc"></i>
            </button>
            <div id="myDropdown" class="dropdown-content">
              <a v-if="dropDownContents.length==0" style="text-align: center; color: gray;"> ไม่มี </a>
              <a v-for="(link, index) in dropDownContents" :key="index" @click="handleDropDownClick(link.id,link.name)">
                {{ link.name }}
              </a>
            </div>
          </div>
          <button class="Navbar-btn" 
          :class="{'Navbar-btn Hightlighted': $route.name === 'tag'}"
          @click="navigateTo('tag')">แก้ไขหมวดหมู่</button>
          <button class="Navbar-btn" 
          :class="{'Navbar-btn Hightlighted': $route.name === 'add'}"
          @click="navigateTo('add')">+ เพิ่ม</button>
          <button class="Navbar-btn" 
          :class="{'Navbar-btn Hightlighted': $route.name === 'remaining'}"
          @click="navigateTo('remaining')">รายชื่อที่เหลือ</button>
          <div class="dropdown">
            <button @click="historyDropDown()" class="dropbtn" style="width: 7pc;">
              ประวัติ
              <i class="fa fa-caret-down" style="position: absolute; right: 1.5pc;top: 1pc"></i>
            </button>
            <div id="myHistoryDropdown" class="dropdown-content" style="width: 7.3pc;">
              <a v-for="(link, index) in historyContents" :key="index" @click="navigateTo(link.path)">
                {{ link.name }}
              </a>
            </div>
          </div>

      </div>
    </v-row>
  </nav>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Navbar',
  data() {
    return {
      dropDownText: localStorage.getItem('dropDownText') || "เลือกหมวด",
      dropDownContents: {},
      historyContents: [
        {'name': 'จับฉลากแล้ว','path':'history'},
        {'name': 'ลบล่าสุด','path':'deleted'}
      ]
    };
  },
  beforeMount() {
  },
  methods: {
    dropDown() {
      document.getElementById("myDropdown").classList.toggle("show");
      window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
          var dropdowns = document.getElementsByClassName("dropdown-content");
          var i;
          for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
            }
          }
        }
      }
    },
    historyDropDown() {
      document.getElementById("myHistoryDropdown").classList.toggle("show");
      window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
          var dropdowns = document.getElementsByClassName("dropdown-content");
          var i;
          for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
            }
          }
        }
      }
    },
    handleDropDownClick(id,name) {
      this.dropDownText = name;
      localStorage.setItem('dropDownID', id)
      localStorage.setItem('dropDownText', name)
      window.location.reload(true);
    },
    getAllTypes(){
      axios.get('/api/tags')
            .then((res) => {
              this.dropDownContents = res.data;
            })
    },
    navigateTo(where){
      this.$router.push(where);
    },
  },
  beforeMount() {
    this.getAllTypes();
    localStorage.setItem('recentDrawn','-')
  }
};
</script>

<style scoped>
.Navbar {
  background-color: #000000;
  padding: 1.5pc 2pc 1.5pc 2pc;
  /* box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2); */
  z-index: 10;
  height: 5.5pc;
}

.left-side-Navbar{
  position: absolute;
  right: 1pc;
  top: 1pc;
}


.logo {
  width: 6pc;
  cursor: pointer;
  transition: 0.3s ease;
}
.logo:hover{
  width: 6.2pc;
}

.Navbar-btn {
  border-radius: 30px;
  background-color: #000000;
  color: #ffffff;
  padding: 12px 17px 12px 17px;
  font-size: 14px;
  font-weight: 700;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  border: 1.6px solid #ffffff ;
  transition: padding 0.3s ease;
}
.Hightlighted {
  background-color: #ffffff;
  color: #000000;
}
.Navbar-btn:hover {
  background-color: #ffffff;
  color: #000000;
}

/* Dropdown Button */
.dropbtn {
  border-radius: 30px;
  background-color: #000000;
  color: #ffffff;
  padding: 12px 17px 12px 17px;
  width: 9pc;
  font-size: 14px;
  font-weight: 700;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  border: 1.6px solid #ffffff ;
  transition: padding 0.3s ease;
}

/* Dropdown button on hover & focus */
.dropbtn:hover, .dropbtn:focus {
  background-color: #ffffff;
  color: #000000;}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  margin-top: 1pc;
  background-color: #000000;
  width: 9.1pc;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border: 1.6px solid #ffffff ;
  border-radius: 30px;
  max-height: 10pc; 
  overflow-y: auto;
  overflow-x: auto;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: rgb(255, 255, 255);
  padding: 12px 16px;
  display: block;
  font-size: 0.9pc;
  cursor: pointer;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  font-size: 1pc;
  background-color: #1a1a1a;
  border-radius: 30px;
}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {display:block;}

.x-btn{
  position: absolute;
  right: 0.5pc;
  height: 1.4pc;
  width: 1.4pc;
  border-radius: 50%;
  z-index: 2;
}
.x-btn:hover {
  background-color: white;
  color: #000000;
}
</style>
