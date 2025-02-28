<template>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent >
        <template v-slot:activator="{ props }">
          <button v-bind="props" class="delete-all-btn">
            Delete all in this category
          </button>
        </template>
        <v-card class="dialog" style=" border-radius: 1.6pc;">
          <v-card-title style="text-align: center;font-weight: 800;padding-top: 1.3pc;font-size: 25px;">
            Delete All
          </v-card-title>
          <p style="font-size: 15px;text-align: center;">This action cannot be undone!</p>

          <v-card-actions>
            <v-spacer></v-spacer>
            <button class="dialog-btn" @click="dialog = false"> Cancel </button>
            <button class="dialog-btn" style="background-color: #7FB02F;" @click="deleteAll()"> Confirm </button>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </template>
  <script>
    import axios from 'axios';
    export default {
      data () {
        return {
          dialog: false,
        }
      },
      methods: {
        deleteAll() {
            this.dialog = false,
            axios.delete("/api/deleted/tag/"+localStorage.getItem('dropDownID'))
              .then ((res) => {
                window.location.reload(true);
              })
        },
      }
    }
  </script>
<style>
.delete-all-btn {
  border-radius: 30px;
  background-color: #000000;
  color: #545454;
  padding: 12px 17px 12px 17px;
  font-size: 13px;
  font-weight: 700;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  border: 1.6px solid #545454 ;
  transition: padding 0.3s ease;
  position: absolute;
  right: 1pc;
  bottom: 1pc;
  z-index: 1;
}
.delete-all-btn:hover {
  background-color: #000000;
  border: 1.6px solid #ffffff ;
  color: #ffffff;
  padding: 14px 19px 14px 19px;
}
.dialog{
    width: 100%;
    max-width: 23pc;
    background-color: #ffffff;
    align-items: center;
    align-self: center;
}

.dialog-btn{
  border-radius: 40px;
  /* 7FB02F */
  background-color: #FF472E;
  color: #ffffff;
  padding: 10px 15px 10px 15px;
  font-size: 15px;
  font-weight: 800;
  margin-left: 0.3pc;
  margin-right: 0.3pc;
  transition:  0.3s ease;
  width: 6pc;
  margin: 0.5pc;
}
.dialog-btn:hover{
  font-size: 16px;
  width: 7pc;
}

</style>