from pdfrw import PdfReader, PdfWriter
import os
import sys


def listararchivos(rutadearchivoinicial):
    return os.listdir(rutadearchivoinicial)
    

def archivos(numeropaginaretirar, rutadearchivoinicial, rutadearchivofinal):
    listfiles = listararchivos(rutadearchivoinicial)
    for nombrearchivo in listfiles:
        savefiles(numeropaginaretirar, rutadearchivoinicial, nombrearchivo ,  rutadearchivofinal)


def savefiles(numeropaginaretirar, rutacompleta, nombredelarchivo, rutasalida):
    archivocompleto =(rutacompleta+"\\"+nombredelarchivo)
    reader_input = PdfReader(archivocompleto)
    writer_output = PdfWriter()
    for i in range(len(reader_input.pages)):
        if (numeropaginaretirar-1 != i):
                writer_output.addPage(reader_input.pages[i]) 
        else:
            print(f"Archivo retirado es = {archivocompleto}")

    destinoguardar = rutasalida+"\\"+nombredelarchivo
    writer_output.write(destinoguardar)



if __name__ == "__main__":
    # arg1 guarda que pagina se retira
    numeropaginaretirar = int(sys.argv[1])
    # arg2 indica la ruta de los pdf
    rutadearchivoinicial =  "D:\PDFScriptPython\RUTAINICIAL"
    # arg2 indica la ruta de guardado
    rutadearchivofinal = "D:\PDFScriptPython\RUTAFINAL"
    archivos(numeropaginaretirar, rutadearchivoinicial, rutadearchivofinal)
    
    
