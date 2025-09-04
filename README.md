# Organizador de Artigos

## Descrição
Script Python para organizar artigos científicos com base em um arquivo CSV de controle, movendo automaticamente os artigos com status "FICA" da pasta `lidos` para a pasta `ler`.

## Funcionalidades
- Lê arquivo CSV com informações dos artigos
- Filtra artigos com status "FICA"
- Normaliza títulos removendo acentos e caracteres especiais
- Busca e copia arquivos correspondentes entre pastas
- Relatório de artigos encontrados e não encontrados


## Como usar
1. Certifique-se de ter o arquivo `leitura.csv` com as colunas necessárias
2. Execute o script: `python artigos.py`
3. Os artigos serão copiados automaticamente para a pasta `ler`

## Dependências
- pandas
- unicodedata (biblioteca padrão)
- os (biblioteca padrão)
- shutil (biblioteca padrão)

## Instalação
```bash
pip install pandas# organize_articles
