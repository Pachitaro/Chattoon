<template>
  <v-app>
    <v-app-bar :elevation="4" class="bg-blue">

      <v-overlay :value="drawer"> <!-- --> </v-overlay>
      <v-toolbar-title>Chattoon</v-toolbar-title>
    </v-app-bar>

    
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="6">
            <v-card color="blue-grey-lighten-5" fill-height="true" style="max: width 100%;" >

              <v-card-title>あなた</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-row>
                  <v-col >
                    <v-container ref="scrollTarget" style="height: 500px" class="overflow-y-auto">
                      <v-row v-for="(msg, i) in messages" :key="i" dense>
                        <v-col>
                          <div class="balloon_r">
                            <v-avatar color="teal">
                              <v-icon icon="mdi-face"></v-icon>
                            </v-avatar>
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
                  <v-col cols="2">
                    <v-btn :disabled="loading" :loading="loading" icon="mdi-send" color="blue" small class="round"
                      @click="send_onclick">

                    </v-btn>
                  </v-col>
                  <v-col>
                    <v-text-field autofocus="true" placeholder="メッセージを入力" v-model="message" clearable="true"
                      @keyup.enter="send_onclick"></v-text-field>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="6">
            <v-card color="blue-grey-lighten-5" fill-height="ture" style="max: width 100%;">
              <v-card-title>AI</v-card-title>
              <v-divider></v-divider>
              <v-card-text >
                <v-row>
                  <v-col >
                    <v-container ref="scrollTarget" style="height: 500px" class="overflow-y-auto">

                      <v-row v-for="(msg_ai, i) in messages_ai" :key="i" dense>
                        <v-col>
                          <div class="balloon_r">

                            <v-avatar color="blue">
                              <v-icon icon="mdi-emoticon-happy"></v-icon>
                            </v-avatar>

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

        <v-btn icon class="mx-4" variant="plain" size="small" href="https://github.com/Pachitaro" target="_blank">
          <v-icon>mdi-github</v-icon>
        </v-btn>
      </div>

      <div class="px-4 py-2 bg-blue text-center w-100">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </div>
    </v-footer>
  </v-app>
</template>



<script>
import axios from "axios";

export default {
  data: () => ({

    messages: [],
    messages_ai: [],
    message: "",
    loading: false,
  }),
  methods: {
    async send_onclick() {
      this.loading = true;

      // ユーザーのメッセージを追加
      this.messages.push({
        name: "あなた",
        avatar_color: "blue",
        message: this.message,
      });



      // ChatGPT APIにリクエストを送信
      try {//webでログを見るためにtry-catchを使用している
        // eslint-disable-next-line
        const response = axios.post('https://chattoon.onrender.com', {
          message: this.message
        },
          { headers: { 'Content-Type': 'application/json' } },
        )
          .then(response => {
            const ai_message = response.data.message;

            // AIのメッセージを追加
            this.messages_ai.push({
              message: ai_message,
            });
          })

        this.message = "";



      } catch (error) {
        console.error("Error in API request:", error);
      }
      this.loading = false;
    },
  },
}
</script>

<style>
.balloon_l {
  position: relative;
  display: inline-block;
  margin: 8px 0;
  padding: 10px;
  background-color: lightgreen;
  border-radius: 10px;
  width: 100%;
}


.balloon_r {
  position: relative;
  display: inline-block;
  margin: 8px 0;
  padding: 10px;
  background-color: lightblue;
  border-radius: 10px;
  width: 100%;
}

.says {
  position: relative;
  display: inline-block;
  margin: 8px 0;
  padding: 10px;
  background-color: lightblue;
  border-radius: 10px;
  width: 100%;
}
</style>