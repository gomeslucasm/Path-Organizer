# Organizador de arquivos

<p> 
Script em python para organizar os arquivos em pastas conforme seu tipo.
</p>

## Como usar?

<ul>
  <li>
  </li>
   <li>
     Abra o cmd.
  </li>
  <li>
    Execute o comando "pip install -r requirements.txt" para instalar as bibliotecas necessárias.
  </li>
  <li>
    Execute o comando "python main.py --path Diretorio da sua escolha"
  </li>
</ul>  

### Organização das pastas

- 'PDF':['/*.pdf',]
- 'Executaveis':['/*.exe','/*.msi']
- 'Imagens':['/*.jpg','/*.png','/*.gif','/*.jpeg','/*.bmp']
- 'Videos':['/*.avi','/*.mp4','/*.wmv','/*.flv','/*.mpeg4','/*.mkv','/*.mpeg']
- 'CSVs':['/*.csv','/*.xlsx']
- 'Word':['/*.doc','/*.docx','/*.rtf']
- 'Zip':['/*.zip','/*.rar']
- 'Bloco de notas':['/*.txt']
- 'Matlab':['/*.m',]
- 'Python':['/*.py',]
- 'Audio':['/*.mp3','/*.wav']
- Obs: Arquivos de tipos que não estão contidos na descrição de cada pasta serão movidos para a pasta Outros.

### Comandos adicionais

## Escolher tipos de pastas para separar os arquivos

- "python main.py --path Diretorio de sua escolha --type tipo de arquivo"

- exemplo: "python main.py --path Downloads --type PDF --type Executaveis --type Imagens --type Videos"

- Obs: Arquivos de tipos que não estão contidos na descrição de cada pasta serão movidos para a pasta Outros.
  
