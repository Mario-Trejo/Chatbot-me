'''Funciones Chatbot - Google
Autores: Mario Tonatiuh Trejo Barrera
         Saul Villegas
Este programa incluye las funciones principales para el Chatbot de SISCOM con la API de Google People
fecha de creación: 20/07/2021
fecha de última compilación: 20/07/2021 14:40 hrs'''
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts']


def Inicia():
    # busqueda es la persona que buscas
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
    return creds


def Check(busqueda, creds):
    service = build('people', 'v1', credentials=creds)
    # Aquí se realiza la búsqueda
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses').execute()
    # Obtiene la lista de contactos completa
    connections = results.get('connections', [])
    for person in connections:  # recorre toda la lista de contactos
        # obtiene el nombre de cada contacto (encriptado)
        names = person.get('names', [])
        if names:  # Si existe el contacto
            # Obtiene el nombre del contacto en string y lo compara con el nombre que se busca
            if (names[0].get('displayName') == busqueda):
                return True  # Si lo encuentra retorna True
    return False  # Si no lo encuentra retorna False


def create(name,creds):
    service = build('people', 'v1', credentials=creds) #construye objeto tipo people
    #newContact contiene todos los parametros que requerimos para crear un nuevo contacto
    newContact = {
        "names": [
            {
                'givenName': name,
                "familyName": "Villegas"
            }
        ],
        "phoneNumbers": [
            {
                'value': "+525529369255"
            }
        ],
        "emailAddresses": [
            {
                'value': "saul.villegasq@gmail.com"
            }
        ],
        "addresses": [
            {
                "streetAddress": "So 1 ngo 85 Lang dsdfsd",
                "extendedAddress": "Ba Dinh",
                "city": "Ha Noi",
                "region": "Ha Noi",
                "postalCode": "10000",
                "country": "Vietnam",
                "countryCode": "84"
            }
        ]
    }
    service.people().createContact(body=newContact).execute()    #Crea el nuevo contacto a partir del diccionario newContact


def resourceNam(name, creds):     #Esta funcion te otorga el resourceName de un contacto específico a partir de su nombre
    service = build('people', 'v1', credentials=creds)
    # Aquí se realiza la búsqueda
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses').execute()
    # Obtiene la lista de contactos completa
    connections = results.get('connections', [])
    for person in connections:  # recorre toda la lista de contactos
        # obtiene el nombre de cada contacto (encriptado)
        names = person.get('names', [])
        if names:  # Si existe el contacto
            # Obtiene el nombre del contacto en string y lo compara con el nombre que se busca
            if (names[0].get('displayName') == name):
                return person.get('resourceName')  #retorna el nombre del contacto en resourceName 


def delete(name, creds):
    if(Check(name, creds)): #Revisa que el contacto exista 
        service = build('people', 'v1', credentials=creds) #Crea un objeto tipo people
        service.people().deleteContact(resourceName=resourceNam(name, creds)).execute() #borra el contacto a partir de su resourceName
        print('Contacto eliminado')   #Indica que se ha eliminado el contacto
    else:
        print('Contacto NO encontrado') #Indica si el contacto no fue encontrado


creds = Inicia()
create ("Saul",creds)
#delete("John Doe", creds)
#print("Contacto: {}".format(resourceNam("Mario Trejo Barrera",creds)))
