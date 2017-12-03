

# Invoke GetCountryByCountryCode to get country by CountryCode = "qa",
#  assert test results
def test_invoke_get_country_by_country_code(get_resp_country_by_code):
    resp = get_resp_country_by_code
    print('Country code: ' + resp[0])
    print('Country name: ' + resp[1])
    assert 'qa' in resp
    assert 'Qatar' in resp


# Using data from step#1 invoke GetCurrencyByCountry,
#  assert test results
def test_invoke_get_currency_by_country(get_resp_currency_by_country):
    resp = get_resp_currency_by_country
    print('Country code: ' + resp[1])
    print('Country name: ' + resp[0])
    print('Country currency: ' + resp[2])
    print('Currency code: ' + resp[3])
    assert 'qa' in resp
    assert 'Qatar' in resp
    assert 'Rial' in resp


# Using data from step#2 invoke GetCountryByCurrencyCode,
#  assert that data from step#2 are equal to data from step#3
def test_invoke_get_country_by_currency_code(get_resp_country_by_currency_code, get_resp_currency_by_country):
    resp = get_resp_country_by_currency_code
    resp_step2 = get_resp_currency_by_country
    print('Country code: ' + resp[1])
    print('Country name: ' + resp[0])
    print('Country currency: ' + resp[2])
    print('Currency code: ' + resp[3])
    assert set(resp) == set(resp_step2)
    assert 'qa' in resp
    assert 'Qatar' in resp
    assert 'Rial' in resp


# Using data from step#3 invoke GetCurrencyCodeByCurrencyName,
# assert that CurrencyCode for requested Currency is present in Response
def test_invoke_get_currency_by_currency_name(get_resp_currency_code_by_currency_name):
    resp = get_resp_currency_code_by_currency_name
    print('Country currency: ' + resp[1])
    print('Currency code: ' + resp[4])
    assert 'QAR' in resp
    assert 'Rial' in resp
