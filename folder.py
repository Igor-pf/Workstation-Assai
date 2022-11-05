from app import app
import os

app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
UPLOADER_FOLDER = os.path.join(os.getcwd(), 'upload')

file_local = UPLOADER_FOLDER+"\\dados.xlsx"

file_json = UPLOADER_FOLDER+"\\dados.json"
