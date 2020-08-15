from PIL import Image #pip install Pillow
import glob
    
if __name__ == "__main__":
	#obtiene un arreglo de imagenes.PNG
	archivos=glob.glob('*.PNG')

	#abre los archivos como imagenes
	files=[Image.open(images) for images in archivos ]

        #convierte las imagenes
	outlist=[item.convert('RGB') for item in files ]
        
        #guarda las imagenes en un solo pdf
	outlist[0].save(r'out.pdf',save_all=True,append_images=outlist[1:])



        
