# ETL-google-sheets

Objetivo: Fazer o ETL dos dados de uma planilha do google sheets, para o banco de dados de produção, e posteriormente, fazer o ETL para o DW.

# Ferramentas Utilizadas

Sistema Operacional: Windows 11
Python: Utilizado para extrair, transformar, modelar e carregar os dados no processo do ETL. Versão 3.10.7
SQLITE 3: Banco de produção OLTP (Foi utilizado pois o sistema só é utilizado por 1 usuário).
DBeaver: Editor de código SQL, para gerenciar as consultas no banco de dados do SQLITE 3. Versão 25.0.3
MySQL: Banco de dados OLAP, utilizado para armazenar os dados do data mart. Versão 8.0.37

# Processo de instalação

1- Instale o Python (Em caso de erro, use a mesma versão do Python mencionada anteriormente)
2- Instale o MySQL (Pode utilizar outro SBGD, verifique a sintaxe dos códigos SQL nos arquivos)
3- Instale o DBeaver (Pode utilizar outra ferramenta que gerencie arquivos do SQLITE)
4- Após fazer o clone do repositório, crie um ambiente virtual com o seguinte comando no terminal: python -m venv venv
5- Ative o ambiente virtual com o seguinte comando no terminal (Comando para Windows): .\venv\Scripts\Activate.ps1
6- Instale as bibliotecas utilizadas no projeto, que estão no arquivo requirements.txt, utilize o comando no terminal: pip freeze -r requirements.txt
7- Faça uma cópia do arquivo arquivo .env_exemplo e renomeie para .env e configure os valores das variáveis de ambiente (Pode apagar os comentários)
8- Configure a API do Google Drive e Google Sheets, para ter acesso a sua client_secret.json e token.json (Sem esse passo, o código não funciona)