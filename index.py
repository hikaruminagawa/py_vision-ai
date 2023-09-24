import os
from google.cloud import vision

# Set the environment variable for the credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './sage-now-400008-2a8dc09dc9d8.json'

#image.jpgを開いて読み込む
with open('./image.jpg', 'rb') as image_file:
    content = image_file.read()

#vision APIが扱える画像データに変換する
image = vision.Image(content=content)

#ImageAnnotatorClientのインスタンスを作成する
annotator_client = vision.ImageAnnotatorClient()

#画像からラベルを検出する
response_data = annotator_client.label_detection(image=image)
labels = response_data.label_annotations

#検出したラベルとそのスコアを表示する
print('----RESULT----')
for label in labels:
    print(label.description, ":", round(label.score*100,2), '%')
print('----RESULT----')