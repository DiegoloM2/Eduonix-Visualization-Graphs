from pygal.maps.world import COUNTRIES

#for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])

#Extract the country code data:

def get_country_code(country_name):
     """Return the Pygal 2-digit country code for the given country."""
     for code, name in COUNTRIES.items():
        if country_name == name:
            return code

     return None

            
