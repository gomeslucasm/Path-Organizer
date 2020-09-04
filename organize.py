import glob
from pathlib import Path
from glob import glob
import shutil 
import os
import PyPDF2

def Organize_dir(dir_org,inc_type, exc_type):

    diretorio = dir_org

    tipos_de_arquivos_default = {
        'PDF':['/*.pdf',],
        'Executaveis':['/*.exe','/*.msi'],
        'Imagens':['/*.jpg','/*.png','/*.gif','/*.jpeg','/*.bmp'], 
        'Videos':['/*.avi','/*.mp4','/*.wmv','/*.flv','/*.mpeg4','/*.mkv','/*.mpeg'],
        'CSVs':['/*.csv','/*.xlsx'],
        'Word':['/*.doc','/*.docx','/*.rtf'],
        'Zip':['/*.zip','/*.rar'],
        'Bloco de notas':['/*.txt'],
        'Matlab':['/*.m',],
        'Python':['/*.py',],
        'Audio':['/*.mp3','/*.wav']
        }
    if inc_type:
        tipos_de_arquivos = dict()
        for inc in inc_type:
            if inc in tipos_de_arquivos_default.keys():
                tipos_de_arquivos[inc] = tipos_de_arquivos_default[inc]
            else:
                pass
    else:
        if exc_type:
            tipos_de_arquivos = tipos_de_arquivos_default
            for exc in exc_type:
                if exc in tipos_de_arquivos.keys():
                    tipos_de_arquivos.pop()
                else:
                    pass
        else:
            tipos_de_arquivos = tipos_de_arquivos_default


    for tipos, pasta in zip(tipos_de_arquivos.values(),tipos_de_arquivos.keys()):
        
        cache_arq = []
        for tipo in tipos:
            if glob(str(diretorio) + tipo):
                cache_arq = cache_arq + glob(str(diretorio) + tipo)

        if len(cache_arq)>0:
            if os.path.isdir(diretorio / pasta):
                pass
            else:
                os.mkdir(diretorio / pasta)

            if type(cache_arq) is list:
                for arq in cache_arq:
                    try:
                        shutil.move(arq, diretorio / pasta)
                    except:
                        print(arq)
            else:
                try:
                    shutil.move(cache_arq, diretorio / pasta)
                except:
                    print(arq)
        else:
            pass

    outros_arquivos = os.listdir(str(diretorio))

    if os.path.isdir(diretorio / 'Outros'):
        pass
    else:
        os.mkdir(diretorio / 'Outros')
        outros_arquivos.remove('Outros')


    not_move = ['.crdownload','.tmp']
    for filename in diretorio.glob('*'):
        if filename.suffix in not_move:
            pass
        else:
            if filename in list(tipos_de_arquivos.keys()):
                pass
            elif os.path.isdir(str(diretorio / filename)):
                pass
            else:
                try:
                    shutil.move(str(diretorio / filename), str(diretorio / 'Outros'))
                except:
                    print(filename)
    
    pass