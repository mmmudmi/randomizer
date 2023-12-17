<template>
  <nav class="Navbar">
    <v-row align="center">
      <div>
        <!-- Logo on the left -->
        <v-img class="logo" src="https://scontent.fbkk5-3.fna.fbcdn.net/v/t39.30808-6/411397878_2581798595320282_3495311650992476261_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=3635dc&_nc_ohc=yvPyeLXO5NsAX8ghSzX&_nc_ht=scontent.fbkk5-3.fna&oh=00_AfCfd4N2_FrAT9iD0DFHQlDsUIkW-XqqusarO01j3n23jQ&oe=6582D3EA"></v-img>
      </div>

      <div class="left-side-Navbar">
          <div class="dropdown">
            <button @click="dropDown()" class="dropbtn">
              {{ dropDownText }}
              <i class="fa fa-caret-down" style="position: absolute; right: 1.5pc;top: 1pc"></i>
            </button>
            <div id="myDropdown" class="dropdown-content">

              <a v-for="(link, index) in dropDownContents" :key="index" @click="handleDropDownClick(link.id,link.name)">
                {{ link.name }}
                <button class="x-btn">x</button>
              </a>
              <a>+ เพิ่มหมวด</a>
            </div>
          </div>
          
          <button class="Navbar-btn">+ เพิ่ม</button>
          <button class="Navbar-btn">รายชื่อที่เหลือ</button>
          <button class="Navbar-btn">ประวัติ</button>

      </div>
    </v-row>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      dropDownText: "เลือกหมวด",
      dropDownID: 0 ,// if so alert เลือกหมวกก่อน
      dropDownContents: {
        0: {'id':1 , 'name':'อาหาร'},
        1: {'id':2 , 'name':'น้ำ'},
        2: {'id':3 , 'name':'กิ๊ฟช็อป'}
      },
    };
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
    handleDropDownClick(id,name) {
      this.dropDownText = name;
      this.dropDownID = id;
    }
  },
};
</script>

<style scoped>
.Navbar {
  background-color: #000000;
  padding: 1.2pc;
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
  z-index: 10;
  height: 5.5pc;
}

.left-side-Navbar{
  position: fixed;
  right: 0;
}


.logo {
  width: 6pc;
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
.Navbar-btn:hover {
  background-color: #1a1a1a;
  padding: 14px 19px 14px 19px;
}

/* Dropdown Button */
.dropbtn {
  border-radius: 30px;
  background-color: #000000;
  color: #ffffff;
  padding: 12px 17px 12px 17px;
  width: 11pc;
  font-size: 14px;
  font-weight: 700;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  border: 1.6px solid #ffffff ;
  transition: padding 0.3s ease;
}

/* Dropdown button on hover & focus */
.dropbtn:hover, .dropbtn:focus {
  background-color: #1a1a1a;
}

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
  min-width: 183px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border: 1.6px solid #ffffff ;
  border-radius: 30px;
  max-height: 10pc; 
  overflow-y: auto;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: rgb(255, 255, 255);
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  font-size: 0.9pc;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  /* font-size: 1.1pc; */
  background-color: #1a1a1a;
  border-radius: 30px;
}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {display:block;}

.x-btn{
  position: absolute;
  right: 0.4pc;
  height: 1.4pc;
  width: 1.4pc;
  border-radius: 50%;
}
.x-btn:hover {
  background-color: white;
  color: #000000;
}
</style>
