from wand.image import Image
from wand.display import display as WandDisplay

from urllib.request import urlopen

#from IPython.display import Image as IPythonImageDisplay
import IPython.display as ipd
#print(dir(ipd))

from ipywidgets import interact
import ipywidgets as widgets

#import matplotlib.pyplot as plt

widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    descripton="Test:",
    disabled=False,
    orientaton="horizontal",
    readout=True,
    readout_format='d')

#print(help(ipd.Image))

url="http://www.sothebys.com/content/dam/sothebys-pages/auction-sales-slides/2019/01/302N10008_9T8WH_web.jpg"
url2="https://media.overstockart.com/optimized/cache/data/product_images/LDV1497-1000x1000.jpg"
#response = requests.get(url)

with Image(file=urlopen(url2)) as img:
    print(img.size)
    for r in 1, 2, 3:
        with img.clone() as i:
            i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
            i.rotate(90 * r)
            f='mona-lisa-{0}.png'.format(r)
            i.save(filename=f)
            WandDisplay(i)
            print(f)
            ipd.Image(f, embed=True)
            #IPythonImageDisplay(f)
    