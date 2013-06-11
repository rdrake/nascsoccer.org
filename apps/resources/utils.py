from bs4 import BeautifulSoup

import requests

FIELD_NAME = 0
FIELD_STATUS = 1

FIELD_STATUS_URL = "http://www.oshawa.ca/mun_res/fieldstatus.asp?type=3"

FIELD_MAPPING = {
    "Grandridge": ["Grand Ridge"],
    "Lakeview Kluane East": ["Lakeview Southeast", "Field 1", "Field 2", "Field 3", "Field 4"],
    "Lakeview Kluane West": ["Lakeview Southwest", "Field 5", "Field 6", "Field 7"],
    "Southmead": ["Southmead Mini"],
    "Southmead 1,2": ["Southmead 1", "Southmead 2"],
    "McLaughlin": ["McLaughlin Park"],
}

def get_field_status():
    r = requests.get(FIELD_STATUS_URL)
    r.raise_for_status()
    
    fields = {}
    parser = BeautifulSoup(r.text)

    for entry in parser.find_all("tr"):
        for (i, item) in enumerate(entry.find_all("td")):
            if i == FIELD_NAME:
                field_name = item.string.strip().replace(" Park", "")
            elif i == FIELD_STATUS:
                field_status = item.string.strip().lower()

                if field_status != "open":
                    field_status = "closed"

                field_status = field_status.capitalize()
        
        try:
            mapped_fields = FIELD_MAPPING[field_name]
        except KeyError:
            mapped_fields = [field_name]
    
        for field in mapped_fields:
            fields[field] = field_status

    return fields
