'''
    pip install qrcode
    pip install qrcode[pil]

    pip install git+git://github.com/ojii/pymaging.git#egg=pymaging
    pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png
'''
import qrcode

img = qrcode.make('Pão de Batata')
img.save('teste.png')