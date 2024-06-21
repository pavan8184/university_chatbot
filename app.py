from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)
 
# Sample Q&A data
qa_data = {
    "what is your name": "I am a simple Q&A chatbot.",
    "what is flask": "Flask is a micro web framework written in Python.",
    "who created you": "I was created by my Guru RAJA."
}
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
 
@app.route('/chatbot_response', methods=['POST'])
def chatbot_response():
    user_message = request.json.get('message').lower()
    bot_response = qa_data.get(user_message, "Sorry, I don't understand that question.")
    return jsonify({"response": bot_response})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
