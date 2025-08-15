# ETL-google-sheets

<code style="color : red">Lecença | GPL-3.0 license | GNU GENERAL PUBLIC LICENSE (https://github.com/mateusdev08/ETL-google-sheets/blob/main/LICENSE)</code>

Objetivo: Fazer o ETL dos dados de uma planilha do google sheets, para o banco de dados de produção, e posteriormente, fazer o ETL para o DW.

## Ferramentas Utilizadas

<ul>
    <li>Sistema Operacional: Windows 11</li>
    <li>Python: Utilizado para extrair, transformar, modelar e carregar os dados no processo do ETL. <code style="color : aqua;">Versão 3.10.7</code></li>
    <li>SQLITE 3: Banco de produção OLTP (Foi utilizado pois o sistema só é utilizado por 1 usuário).</li>
    <li>DBeaver: Editor de código SQL, para gerenciar as consultas no banco de dados do SQLITE 3. <code style="color : name_color">Versão 25.0.3</code></li>
    <li>MySQL: Banco de dados OLAP, utilizado para armazenar os dados do data mart. <code style="color : name_color">Versão 8.0.37</code></li>
</ul>

## Processo de instalação

<ol>
    <li>Instale o Python (Em caso de erro, use a mesma versão do Python mencionada anteriormente)</li>
    <li>Instale o MySQL (Pode utilizar outro SBGD, verifique a sintaxe dos códigos SQL nos arquivos)</li>
    <li>Instale o DBeaver (Pode utilizar outra ferramenta que gerencie arquivos do SQLITE)</li>
    <li>Após fazer o clone do repositório, crie um ambiente virtual com o seguinte comando no terminal: <code style="color : name_color">python -m venv venv</code></li>
    <li>Ative o ambiente virtual com o seguinte comando no terminal (Comando para Windows): <code style="color : name_color">.\venv\Scripts\Activate.ps1</code></li>
    <li>Instale as bibliotecas utilizadas no projeto, que estão no arquivo requirements.txt, utilize o comando no terminal: <code style="color : name_color">pip freeze -r requirements.txt</code></li>
    <li>Faça uma cópia do arquivo arquivo .env_exemplo e renomeie para .env e configure os valores das variáveis de ambiente (Pode apagar os comentários)</li>
    <li>Configure a API do Google Drive e Google Sheets, para ter acesso a sua client_secret.json e token.json (Sem esse passo, o código não funciona)</li>
</ol>
