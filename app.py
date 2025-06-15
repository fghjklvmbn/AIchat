from flask import Flask, request, jsonify
from functions.Chatbot import chat

# 현재 파일 위치
app = Flask(__name__)

# 챗봇 대화 기능
@app.route("/ai/chat", methods=["POST"])
def chatting():
    data = request.get_json()
    user_input = data.get('input', '')
    
    if not user_input:
        return jsonify({'error': 'Empty input'}), 400

    try:
        response = chat(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/ai", methods=["GET"])
def index():
    return jsonify({"message": "정상작동"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
