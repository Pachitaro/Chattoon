<template>
  <v-app >
    
    <v-navigation-drawer v-model="drawer" :app="false">
      <!--  -->
    </v-navigation-drawer>

    <v-app-bar :elevation="4" class="bg-blue">
      <v-app-bar-nav-icon @click="drawer = !drawer" ></v-app-bar-nav-icon>
      <v-overlay :value="drawer"> <!-- --> </v-overlay>
      <v-toolbar-title>Chattoon</v-toolbar-title>
    </v-app-bar>

    
      
  
    
    <v-main>
      <v-text-field rows: height="500px" width="500px"></v-text-field>
    </v-main>
    <v-footer class="d-flex flex-column">
    <div class="bg-teal d-flex w-100 align-center px-4">

      <v-btn
        v-for="icon in icons"
        :key="icon"
        class="mx-4"
        :icon="icon"
        variant="plain"
        size="small"
      ></v-btn>
    </div>

    <div class="px-4 py-2 bg-blue text-center w-100">
      {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
    </div>
  </v-footer>
  </v-app>
</template>

<script>
  export default {
    data: () => ({ drawer: null ,
      icons: [
        'mdi-account-circle',
        // 'mdi-twitter',
        'mdi-github',
      ],
    }),
  }
</script>