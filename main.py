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