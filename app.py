from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/read_barcode', methods=['POST'])
def read_barcode_api():
    # Certifique-se de que a imagem foi fornecida no corpo da requisição POST
    if 'image' not in request.files:
        return jsonify({'error': 'Imagem não encontrada no corpo da requisição'}), 400

    image = request.files['image']
    
    try:
        # Ler o número de barras usando a biblioteca pyzbar
        barcode_data = decode(Image.open(image))

        # Retornar o número de barras, se houver algum
        if barcode_data:
            return jsonify({'barcode_number': barcode_data[0].data.decode('utf-8')})
        else:
            return jsonify({'message': 'Não foi possível ler o número de barras.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
