import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from view import etl_tratamento
from model_etl import etl_dw

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SAMPLE_SPREADSHEET_ID = os.getenv('NOME_ARQUIVO')
SAMPLE_RANGE_NAME = os.getenv('DADOS_CELULAS')


def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        tamanho_lista = len(values) - 1
        i = 1
        while True:
            dados = values[i]
            etl_tratamento(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6],
                           dados[7], dados[8], dados[9], dados[10], dados[11], dados[12], dados[13])
            i += 1
            if i > tamanho_lista:
                break

        etl_dw()

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
