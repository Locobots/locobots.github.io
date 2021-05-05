# <font color = 'red'>Loco</font>bots site

Esse o projeto para o site da locobots hospedado no GitHub pages. O principal objetivo desse site é divulgar informações sobre o núcleo de desenvolvimento mais <b>LOCO</b> da UFOP.

<img src = 'https://raw.githubusercontent.com/Locobots/locobots.github.io/content/content/images/siteCe.png'/>

<img src = 'https://raw.githubusercontent.com/Locobots/locobots.github.io/content/content/images/sitePC.png'/>


<hr>

## Instalar

Use o package manager [pip](https://pip.pypa.io/en/stable/installing/) para intalar:


```bash
pip3 install virtualenv
```

## Configurando o ambiente

Clone o repositorio e execute os comandos

```bash
git fetch origin content:content
```

```bash
git checkout content
```


```bash
virtualenv ENV 
#criando ambiente virtual

#No Windows:
python -m venv ENV
```

```bash
source ENV/bin/activate 
#ativando ambiente virtual 
#deactivate

#No Windows:
ENV/Scripts/Activate.bat
```

```bash
pip install -r requirements.txt
```

<hr>

##Arvore de arquivos 

```
├── content
│   ├── artigle
│   ├── imagens
│   ├── pages
│   ├── static
│       └── custom.css
├── pelican-addon-clones
│   └── pelican-themes-extra
│        └── flex
├── pelicanconf.py
├── requirements.txt
├── .gitignore
```

<hr>

## Modificando o site

<h4>Criando conteudo</h4>

😍 Adicione arquivos .md em suas categorias na pasta  <i>/content</i> 

```bash
pelican content 
# Compilando o site
``` 

``` bash
pelican --autoreload --listen 
# http://localhost:8000/
``` 

<h4>Publicando site</h4>

``` bash
pelican content -o output -s pelicanconf.py
``` 

``` bash
ghp-import output
``` 

``` bash
git push origin gh-pages:master --force
``` 

<h4>Intalando tema</h4>

```bash
git clone https://github.com/repositorio
```

```bash
pelican-themes --install ~/caminho/do/repositorio/salvo --verbose

#pelican-themes -l
#pelican-themes --remove Flex
```

Caso tenha intalado novas bibliotecas atualize o requirements.txt  :D

```bash
pip freeze > requirements.txt
```


## Contribuições
Pull requests são bem vindos. Porfavor, tenha certeza que o update esteja apropriados

- [Alexander Marx](https://www.instagram.com/marx_al172/)
- [Jamisson Jader](https://github.com/jjader)


## Referências legais

- [Pelican documentation](http://docs.getpelican.com/en/3.6.3/index.html)
- [VirtualEnv documentation](https://virtualenv.pypa.io/en/latest/)
- [Python e virtualEnv](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)
- [Deploy no Github Pages](https://caiocarrara.com.br/blog/migrando-do-wordpress-para-o-pelican.html)
- [Repositório do tema Flex](https://github.com/alexandrevicenzi/Flex)
