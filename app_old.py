from PIL import Image
from pyzbar.pyzbar import decode

def read_barcode(image_path):
    # Carregar a imagem
    image = Image.open(image_path)

    # Ler o número de barras usando a biblioteca pyzbar
    barcode_data = decode(image)

    # Retornar o número de barras, se houver algum
    if barcode_data:
        return barcode_data[0].data.decode('utf-8')
    else:
        return None
    
barcode_number = read_barcode('C:\\Users\\mv.joao\\Downloads\\barcode image\\Imagem (17).tif')

if barcode_number:
    print('Código de Barras:', barcode_number)
else:
    print('Não foi possível ler o número de barras.')