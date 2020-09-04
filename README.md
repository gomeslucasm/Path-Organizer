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

## Gerando executável

- "pyintaller --onefile --noconsole .\main.py".

- Obs.: O comando "--noconsole" é opcional e serve para gerar um executável que não abre a janela do cmd, ou seja, fica funcionando em segundo plano.


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

#### Escolher tipos de pastas para separar os arquivos

- "python main.py --path Diretorio de sua escolha --type tipo de arquivo"

- exemplo: "python main.py --path Downloads --type PDF --type Executaveis --type Imagens --type Videos"
  
 #### Excluir um tipo de pasta 
 
 - "python main.py --path Diretorio de sua escolha --exclude tipo de arquivo"

- exemplo: "python main.py --path Downloads --exclude Executaveis --exclude PDF"


