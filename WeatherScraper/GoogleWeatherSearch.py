import requests
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
 
 
def fetch_results(zipcode, number_results, language_code):

    google_url = 'https://www.google.com/search?q='+ zipcode +'+weather'
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return zipcode, response.text
 
def google_search(zipcode):
    keyword, html = fetch_results(zipcode, 100, 'en')
    farenheit_position = html.find('<span class="wob_t" id="wob_tm" style="display:inline">') + 55;
    return html[farenheit_position:farenheit_position+2]

