# Organizador de arquivos

Script em python que monitora os arquivos adicionados ou movidos em uma pasta, e os organiza conforme seu tipo. Para o fazer o monitoramento da pasta é utilizada a biblioteca `watchdog`.


## Como usar?

- Abra o cmd.

- Instale as bibliotecas necessárias `pip install -r requirements.txt`

- `python main.py --path Diretorio da sua escolha`

- Ex.: `python main.py --path Downloads`


## Gerando executável

- `pyintaller --onefile --noconsole .\main.py`

- É interessante adicionar o .exe gerado na inicialização do sistema para que seus arquivos estejam sempre organizados.

- Obs.: O comando `--noconsole` é opcional e serve para gerar um executável que não abre a janela do cmd, ou seja, fica funcionando em segundo plano.


## Organização das pastas

- ```'PDF':['/*.pdf',]
  'Executaveis':['/*.exe','/*.msi']
  'Imagens':['/*.jpg','/*.png','/*.gif','/*.jpeg','/*.bmp']
  'Videos':['/*.avi','/*.mp4','/*.wmv','/*.flv','/*.mpeg4','/*.mkv','/*.mpeg']
  'CSVs':['/*.csv','/*.xlsx']
  'Word':['/*.doc','/*.docx','/*.rtf']
  'Zip':['/*.zip','/*.rar']
  'Bloco de notas':['/*.txt']
  'Matlab':['/*.m',]
  'Python':['/*.py',]
  'Audio':['/*.mp3','/*.wav']
- Obs: Arquivos de tipos que não estão contidos na descrição de cada pasta serão movidos para a pasta Outros.

### Comandos adicionais

#### Escolher tipos de pastas para separar os arquivos

- `python main.py --path Diretorio de sua escolha --type tipo de arquivo`

- Ex.: `python main.py --path Downloads --type PDF --type Executaveis --type Imagens --type Videos`
  
 #### Excluir um tipo de pasta 
 
 - `python main.py --path Diretorio de sua escolha --exclude tipo de arquivo`

- Exemplo: `python main.py --path Downloads --exclude Executaveis --exclude PDF`


