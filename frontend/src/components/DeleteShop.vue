<template>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent >
        <template v-slot:activator="{ props }">
          <button v-bind="props" class="delete-shop-btn">
            -
          </button>
        </template>
        <v-card class="dialog" style=" border-radius: 1.6pc;">
          <v-card-title style="text-align: center;font-weight: 800;padding-top: 1.3pc;font-size: 25px;">
            Delete Shop
          </v-card-title>
          <p style="font-size: 15px;text-align: center;">Delete this shop from the undrawn list</p>
          <v-card-actions>
            <v-spacer></v-spacer>
            <button class="dialog-btn" @click="dialog = false"> Cancel </button>
            <button class="dialog-btn" style="background-color: #7FB02F;" @click="redrawAll()"> Confirm </button>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </template>
  <script>
    export default {
      data () {
        return {
          dialog: false,
        }
      },
      methods: {
        redrawAll() {
            this.dialog = false,
            // window.location.reload(true);
            console.log("confirm to redrawAll from tag ID: "+localStorage.getItem('dropDownID') )

        },
      }
    }
  </script>
<style>
.delete-shop-btn {
  color: white;
  text-align: center;
  cursor: pointer;
  background-color: #FF472E;
}
.delete-shop-btn:hover {
  color: #FF472E;
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