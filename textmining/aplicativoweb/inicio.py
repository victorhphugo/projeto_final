from gtts import gTTS
from flask import Flask,render_template,request
import os 

# criando o objeto flask 
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    audio_path = None
    if request.method == 'POST':
        # pegar valor do html <textfield>
        texto = request.form['texto']
    
        # configurar o idioma
        lingua = 'pt-br'

        # Criação do objeto
        tts = gTTS(text=texto,lang=lingua)

        # Nome do arquivo de audio
        audio_path = "static/audio_exemplo.mp3"

        #salvar arquivo
        tts.save(audio_path)

    return render_template('index.html',audio_path=audio_path)
if __name__ == '__main__':
    app.run(debug=True)
