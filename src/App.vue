<template>
  <v-app>
    <v-app-bar :elevation="4" class="bg-blue">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-overlay :value="drawer"> <!-- --> </v-overlay>
      <v-toolbar-title>Chattoon</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" :app="false">
      <!--  -->
    </v-navigation-drawer>




    <v-main>
      <v-container>
        <v-row>
          <v-col cols="6">
            <v-card color="blue-grey-lighten-5" fill-height="ture">

              <v-card-title>あなた</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-container ref="scrollTarget" style="height: 500px" class="overflow-y-auto">
                      <v-row v-for="(msg, i) in messages" :key="i" dense>
                        <v-col>
                          <div class="ballon_l">
                            <div class="face_icon">
                              <v-avatar :color="msg.avatar_color">
                                <span class="white--text">
                                  {{ msg.name }}
                                </span>
                              </v-avatar>
                            </div>
                            <p class="says">
                              {{ msg.message }}
                            </p>
                          </div>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-text>
                <v-row>
                  <v-col cols="1">
                    <v-btn icon="mdi-send" color="blue"  small @click="send_onclick">
                      
                    </v-btn>
                  </v-col>
                  <v-col>
                    <v-text-field autofocus="true" label="メッセージを入力" v-model="message" clearable="true"
                      @keyup.enter="send_onclick"></v-text-field>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="6">
            <v-card color="blue-grey-lighten-5" fill-height="ture">
              <v-card-title>AI</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-container
                      ref="scrollTarget"
                      style="height: 500px"
                      class="overflow-y-auto"
                      >
                    <v-row v-for="(msg_ai, i) in messages_ai" :key="i" dense>
                      <v-col>
                        <div class="balloon_r">
                          <div class="face_icon">
                            <v-avater :color="msg_ai.avatar_color">
                              <span class="white--text">
                                {{ msg_ai.name }}
                              </span>
                            </v-avater>
                          </div>
                          <p class="says">
                            {{ msg_ai.message }}
                          </p>
                        </div>
                      </v-col>
                    </v-row>
                    </v-container>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>


    <v-footer app class="d-flex flex-column">
      <div class="bg-teal d-flex w-100 align-center px-4">

        <v-btn v-for="icon in icons" :key="icon" class="mx-4" :icon="icon" variant="plain" size="small"></v-btn>
      </div>

      <div class="px-4 py-2 bg-blue text-center w-100">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    icons: [
      'mdi-account-circle',
      // 'mdi-twitter',
      'mdi-github',
    ],
    items: [
      { title: 'Item 1' },
      { title: 'Item 2' },
      { title: 'Item 3' },
      { title: 'Item 4' },
    ],
  }),
}
</script>