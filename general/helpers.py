import xml.etree.ElementTree as ET
import logging


# Parser for response from services
def get_values_from_resp(data):
    logging.info('call get_values_from_resp')
    root = ET.fromstring(data)
    resp_values = []
    for i in root.iter('Table'):
        for j in i:
            resp_values.append(j.text)
    print(resp_values)
    return resp_values

