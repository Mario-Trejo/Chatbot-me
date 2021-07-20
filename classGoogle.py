
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

#Clases propias
from classbody import body
from classbody import Addresses




# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts']

class Google:

    def __init__(self):
        
        self.creds = None
            
        if os.path.exists('token.json'):
                self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                
                self.creds = flow.run_local_server(port=0)
      
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
        
        self.service = build('people', 'v1', credentials=self.creds)


    def Check(self,busqueda:str):
        
        results = self.service.people().connections().list(resourceName='people/me',personFields='names,emailAddresses').execute()

        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:  
                if (names[0].get('displayName') == busqueda):
                    return True 
        return False  


    def create(self,databody:body):
        self.service.people().createContact(body=databody.JsonBody()).execute()
            
        
    


    def resourceName(self,name:str):     
        results = self.service.people().connections().list(resourceName='people/me',personFields='names,emailAddresses').execute()
        
        connections = results.get('connections', [])
        
        for person in connections:  
            
            names = person.get('names', [])
            
            if names:  
                if (names[0].get('displayName') == name):
                    return person.get('resourceName')
        return None


    def delete(self,name):

        if( self.Check(name) ):  
        
            service = build('people', 'v1', credentials=self.creds) #Crea un objeto tipo people
        
            service.people().deleteContact(resourceName=self.resourceName(name) ).execute() #borra el contacto a partir de su resourceName
        
            print('Contacto eliminado')   #Indica que se ha eliminado el contacto
        
        else:
        
            print('Contacto NO encontrado') #Indica si el contacto no fue encontrado
    
    def update(self,name:str,databody:body):
        self.service.people().updateContact(body=databody.JsonBody(),resourceName=self.resourceName(name),updatePersonFields= "phoneNumbers").execute() 


name = "Martin Saul Villegas Quiroz"

chatbot = Google()

dirrecion = Addresses("Oriente 166 420","CDMX","Venustiano Carranza","15530","Mexico","+52")
Bodyname = body("Martin Saul","Villegas Quiroz","+52"+"5529369253","saul.villegasq@gmail.com",dirrecion)
'''if(not chatbot.Check(name)):
    chatbot.create(Bodyname)
    print("Creado")'''
chatbot.update(name,Bodyname)

#print(chatbot.Check(name))

#chatbot.delete(name)

