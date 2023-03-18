from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    
    # ChatGPT APIにリクエストを送信
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは私のフレンドリーな友達です。軽い口調で会話します。"},
            {"role": "user", "content": f"{user_message}"},
        ]
    )

    ai_message = response.choices[0]["message"]["content"].strip()
    return jsonify({"message": ai_message})
    


if __name__ == '__main__':
    app.run(debug=True)
