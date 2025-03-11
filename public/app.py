from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    signature_data = request.form['signatureData']

    # 署名データをデコードして画像に変換
    signature_data = signature_data.split(',')[1]
    signature_image = Image.open(BytesIO(base64.b64decode(signature_data)))

    # 画像をモデルの入力形式 (224x224x3) に変換し、余白を白で埋める
    signature_image = ImageOps.contain(signature_image, (224, 224), method=Image.BICUBIC, fillcolor='white')
    signature_array = np.array(signature_image)

    # モデルの推論を実行（ここではダミーの結果を返す）
    # 実際には、ここでモデルの推論を実行するコードを追加します
    result = {"user_id": user_id, "prediction": "dummy_result"}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)