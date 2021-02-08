##############################################
# # # LIBRERIAS # # #

from pdf2docx import Converter
import os

##############################################
# # # CARGA DE TEXTOS # # # 

# # # Definición del directorio donde se alojarán los textos convertidos # # #

path_input = '/pdftodocx/input/'
path_output = '/pdftodocx/output/'

# # # Loop para leer todos los documentos, reconvertirlos y guardarlos # # #

for file in os.listdir(path_input):
	cv = Converter(path_input+file)
	cv.convert(path_output+file+'.docx', start=0, end=None) # Hay que corregir el quitar '.pdf' ya que queda en el nombre del archivo
	cv.close()
	print(file)


###############################################
"""
El resultado es la lectura de todas los archivos disponibles en PDF y guardandolos
en formato .docx para poder ser editados
"""
###############################################
print("Fin del Proceso")
