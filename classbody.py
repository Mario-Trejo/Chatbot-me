
class Addresses:
    def __init__(self, streetAddress=None, extendedAddress=None, city=None, region=None, postalCode=None, country=None, countryCode=None):
        self.streetAddress = streetAddress
        self.extendedAddress = extendedAddress
        self.city = city
        self.region = region
        self.postalCode = postalCode
        self.country = country
        self.countryCode = countryCode

    def getstreetAddress(self):
        return self.streetAddress

    def getextendedAddress(self):
        return self.extendedAddress

    def getcity(self):
        return self.city

    def getregion(self):
        return self.region

    def getpostalCode(self):
        return self.postalCode

    def getcountry(self):
        return self.country

    def getcountrycode(self):
        return self.countryCode

    def setstreetAddress(self, streetAddress):
        self.streetAddress = streetAddress

    def setextendedAddress(self, extendedAddress):
        self.extendedAddress = extendedAddress

    def setcity(self, city):
        self.city = city

    def setregion(self, region):
        self.region = region

    def setpostalCode(self, postalCode):
        self.postalCode = postalCode

    def setcountry(self, country):
        self.country = country

    def setcountryCode(self, countryCode):
        self.countryCode = countryCode


class body:

    def __init__(self, givenName, familyName, phoneNumbres=None, email=None, Addr: Addresses = None):
        self.givenName = givenName
        self.familyName = familyName
        self.phoneNumbres = phoneNumbres
        self.email = email
        self.Addr = Addr

    def setEmail(self, email):
        self.email = email

    def setphoneNumbres(self, phoneNumbres):
        self.phoneNumbres = phoneNumbres    

    def setAddr(self, Addr):
        self.Addr = Addr

    def JsonBody(self):
        Contact = {
            "names": [
                {
                    "givenName": self.givenName ,
                    "familyName": self.familyName
                }
            ],
            "phoneNumbers": [
                {
                    'value': self.phoneNumbres
                }
            ],
            "emailAddresses": [
                {
                    'value': self.email
                }
            ],
            "addresses": [
                {
                    "streetAddress": self.Addr.getstreetAddress(),
                    "extendedAddress": self.Addr.getextendedAddress(),
                    "city": self.Addr.getcity(),
                    "region": self.Addr.getregion(),
                    "postalCode": self.Addr.getpostalCode(),
                    "country": self.Addr.getcountry(),
                    "countryCode": self.Addr.getcountrycode()
                }
            ]
        }
        return Contact
    def getName(self):
        return str(self.givenName)
    def getFamily(self):
        return str(self.familyName)

