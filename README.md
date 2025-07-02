This is a local hosted text to speech solution

# Setup
To get started you need two things:
- Ollama
- Python

1. Go to https://ollama.com/ to download ollama. After running the setup/installation, go to the terminal and run:
   ```
   ollama run [model]
   ```
   [model] = any model you want from their list of models. For a simple model, I recommend `tinyllama`
3. After installing said model, clone this repo
4. After cloning the repo you can install a models for the text to speech. The tts the project uses is from 'piper' (https://github.com/rhasspy/piper). Each model filename has a `'.onnx'` extension and a corresponding config file that ends in `'.onnx.json'`. Go to https://github.com/rhasspy/piper/blob/master/VOICES.md to get a list of models to download. Once you've downloaded your model and its config file, go to the next step.
5. Open the project/models and paste in your model with the config there.
6. Now open the project in your code editor of choice and run `pip -r requirements.txt` then go to the `main.py` file. It looks like this:
   ```python
   import ollama
   import subprocess

   client = ollama.Client()

   model = "tinyllama"
   prompt = "What is C++?"

   response = client.generate(model=model, prompt=prompt)

   print(response.response)

   voice_model_path = 'models/en_GB-alan-medium.onnx'
   voice_model_config_path = 'models/en_GB-alan-medium.onnx.json'

   subprocess.Popen('echo ' + str(response.response) + ' | piper/piper.exe --model ' + str(voice_model_path) + ' --config ' + str(voice_model_config_path) + ' --output_file output/output.wav', shell=True)
   ```
7. Now, set your ollama 'model', 'prompt', 'voice_model_path' and the 'voice_model_config_path'. All that's left to do now is `python main.py` and you're good!
8. The output of the prompt will be written in the terminal and the output.wav file will be generated in the project/output folder.


   Before running though, make sure you're ollama server is running locally (on windows, you'll see the ollama app in the tray when you open the ollama app).
   
   That's all I got! 🚀🎙️🎤
