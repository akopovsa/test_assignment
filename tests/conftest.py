import pytest
from zeep import Client
from .context import helpers
import logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)


# Initiate Client for interacting with a SOAP server
@pytest.fixture()
def setup():
    logging.info('call setup()')
    wsdl = 'http://www.webservicex.net/country.asmx?WSDL'
    client = Client(wsdl)
    print("Client for interacting with a SOAP server initiated")
    return client


# Invoke GetCountryByCountryCode and get response and parse it
@pytest.fixture()
def get_resp_country_by_code(setup):
    logging.info('call get_resp_country_by_code()')
    country_by_code_resp = setup.service.GetCountryByCountryCode('qa')
    values = helpers.get_values_from_resp(country_by_code_resp)
    return values


# Get parsed response from GetCountryByCountryCode, Invoke GetCurrencyByCountry, get response and parse it
@pytest.fixture()
def get_resp_currency_by_country(setup, get_resp_country_by_code):
    logging.info('call get_resp_currency_by_country ')
    values_from_country_by_code = get_resp_country_by_code
    currency_by_country_resp = setup.service.GetCurrencyByCountry(values_from_country_by_code[1])
    values = helpers.get_values_from_resp(currency_by_country_resp)
    return values


# Get parsed response from GetCurrencyByCountry, Invoke GetCountryByCurrencyCode, get response and parse it
@pytest.fixture()
def get_resp_country_by_currency_code(setup, get_resp_currency_by_country):
    logging.info('call get_resp_country_by_currency_code')
    values_from_currency_by_country = get_resp_currency_by_country
    country_by_currency_code_resp = setup.service.GetCountryByCurrencyCode(values_from_currency_by_country[3])
    values = helpers.get_values_from_resp(country_by_currency_code_resp)
    return values


# Get parsed response from GetCountryByCurrencyCode,Invoke GetCountryByCurrencyCode, get response and parse it
@pytest.fixture()
def get_resp_currency_code_by_currency_name(setup, get_resp_country_by_currency_code):
    logging.info('call get_resp_currency_code_by_currency_name')
    values_from_country_by_currency_code = get_resp_country_by_currency_code
    currency_code_by_currency_name_resp = setup.service.GetCurrencyCodeByCurrencyName(values_from_country_by_currency_code[2])
    values = helpers.get_values_from_resp(currency_code_by_currency_name_resp)
    return values

