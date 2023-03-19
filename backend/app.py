from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

allmessages = [{"role": "system", "content": "あなたは私のフレンドリーな友達です。軽い口調で会話します。"},]

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    global allmessages
    data = request.get_json()
    user_message = data['message']

    allmessages.append({"role": "user", "content": user_message},)
    
    # ChatGPT APIにリクエストを送信
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=allmessages
    )

    ai_message = response.choices[0]["message"]["content"].strip()
    allmessages.append({"role": "system", "content": ai_message},)
    return jsonify({"message": ai_message})
    


if __name__ == '__main__':
    app.run(debug=True)
