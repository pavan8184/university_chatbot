from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)
 
# Sample Q&A data
qa_data = {
    "what is your name": "I am a simple Q&A chatbot.",
    "what is flask": "Flask is a micro web framework written in Python.",
    "who created you": "I was created by my Guru RAJA.",
    "what is a university": "A university is an institution of higher education and research which grants academic degrees in various subjects.",
    "why should I choose this university": "This university offers a wide range of academic programs, has excellent faculty, and provides numerous opportunities for student growth and development.",
    "what are the admission requirements": "Admission requirements typically include standardized test scores, transcripts, letters of recommendation, and sometimes an interview.",
    "what majors does this university offer": "This university offers majors in fields such as Computer Science, Biology, History, Psychology, and many others.",
    "what extracurricular activities are available": "Students can participate in clubs, sports teams, community service projects, cultural events, and more.",
    "how can I apply for financial aid": "Information on applying for financial aid can be found on the university's website or by contacting the financial aid office.",
    "where can I find information about campus housing": "Details about campus housing options, including residence halls and apartments, can be found on the university's housing website."
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
