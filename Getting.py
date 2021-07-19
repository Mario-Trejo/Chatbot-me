'''Getting
Mario Tonatiuh Trejo Barrera // Google quickstart
Este programa es para comprobar si un contacto existe en nuestra lista de contactos
fecha de creación: 19/07/2021
fecha de última compilación: 19/07/2021 14:30 hrs'''
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts']

def Check(busqueda):
    #busqueda es la persona que buscas
    creds = None
    """Lo siguiente es para inicializar el Json"""
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
       # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('people', 'v1', credentials=creds)

    # Aquí se realiza la búsqueda
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses').execute()
    connections = results.get('connections', []) #Obtiene la lista de contactos completa
    for person in connections: #recorre toda la lista de contactos
        names = person.get('names', []) #obtiene el nombre de cada contacto (encriptado)
        if names: #Si existe el contacto 
            if (names[0].get('displayName') == busqueda): #Obtiene el nombre del contacto en string y lo compara con el nombre que se busca
                return True  #Si lo encuentra retorna True
    return False #Si no lo encuentra retorna False
if (Check("Pablo")):
    print("Contacto encontrado")
else:
    print("Contacto NO encontrado")