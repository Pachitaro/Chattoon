
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
            <v-card color="blue-grey-lighten-5" fill-height="ture" style="max: width 100%;">

              <v-card-title>あなた</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-container ref="scrollTarget" style="height: 500px" class="overflow-y-auto">
                      <v-row v-for="(msg, i) in messages" :key="i" dense>
                        <v-col>
                          <div class="balloon_l">
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
                    <v-btn :disabled="loading" :loading="loading" icon="mdi-send" color="blue" small class="round" @click="send_onclick">

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
              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-container ref="scrollTarget" style="height: 500px" class="overflow-y-auto">
                      
                      <v-row v-for="(msg_ai, i) in messages_ai" :key="i" dense>
                        <v-col>
                          <div class="balloon_r">
                            <div class="face_icon">
                              <v-avatar color="blue">
                                <span class="white--text">
                                  AI
                                </span>
                              </v-avatar>
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

        <v-btn v-for="icon in icons" :key="icon" icon class="mx-4" variant="plain" size="small">
          <v-icon>{{ icon }}</v-icon>
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
    messages: [],
    messages_ai: [],
    message: "",
    loading:false,
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
      try{//webでログを見るためにtry-catchを使用している
        // eslint-disable-next-line
      const response =  axios.post('http://127.0.0.1:5000/api/chat', {
        message: this.message},
        {headers: {'Content-Type': 'application/json'}},
      )
      .then(response => {
        const ai_message = response.data.message;

      // AIのメッセージを追加
      this.messages_ai.push({
        message: ai_message,
      });
      })
      
      this.message = "";

      

    }catch (error) {
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
    background-color: #be3a3a;
    border-radius: 10px;
    width: 100%;
  }

  .balloon_l::before {
    content: "";
    position: absolute;
    top: 10px;
    left: -20px;
    border-style: solid;
    border-width: 10px 20px 10px 0;
    border-color: transparent #f2f2f2 transparent transparent;
  }

  .balloon_r {
    position: relative;
    display: inline-block;
    margin: 8px 0;
    padding: 10px;
    background-color: #13dee9;
    border-radius: 10px;
    width: 100%;
  }

  .balloon_r::after {
    content: "";
    position: absolute;
    top: 10px;
    right: -20px;
    border-style: solid;
    border-width: 10px 0 10px 20px;
    border-color: transparent  #c7ecee;
  }
</style>