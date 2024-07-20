import requests
import urllib.parse
import time
from ratelimit import limits, sleep_and_retry
import backoff

from relations import *

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 60

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=5)
def fetch_from_wikidata(query):
    encoded_query = urllib.parse.quote(query)

    url = f'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query={encoded_query}'

    headers = {
        "Accept": "application/sparql-results+json",
        'User-Agent': 'LMKBCBot/1.0 (lm-kbc-challenge.vercel.app; 07.truffle.bold@icloud.com)'
    }

    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    delay = int(retry_after)
                except ValueError:
                    retry_after_time = time.strptime(retry_after, "%a, %d %b %Y %H:%M:%S %Z")
                    delay = time.mktime(retry_after_time) - time.time()
                print(f"Rate limit exceeded. Retrying after {delay} seconds.")
                time.sleep(delay)
            else:
                print("Rate limit exceeded. Retrying after 60 seconds.")
                time.sleep(60)
        else:
            response.raise_for_status()

def get_place_of_death(person_name):
    query = wd_p20.generate_sparql_query(person_name)
    try:
        results = fetch_from_wikidata(query)
        query_results = []
        for result in results["results"]["bindings"]:
            place_label = result.get("placeLabel", {}).get("value", "No label available")
            query_results.append(place_label)
        return query_results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_bordering_countries(country_name):
    query = wd_p47.generate_sparql_query(country_name)
    try:
        results = fetch_from_wikidata(query)
        query_results = []
        for result in results["results"]["bindings"]:
            boredering_country_label = result.get("borderingCountryLabel", {}).get("value", "No label available")
            query_results.append(boredering_country_label)
        return query_results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_award_winners(award_name):
    query = wd_p166.generate_sparql_query(award_name)
    try:
        results = fetch_from_wikidata(query)
        query_results = []
        for result in results["results"]["bindings"]:
            person_label = result.get("personLabel", {}).get("value", "No label available")
            query_results.append(person_label)
        return query_results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_stock_exchanges(company_name):
    query = wd_p414.generate_sparql_query(company_name)
    try:
        results = fetch_from_wikidata(query)
        query_results = []
        for result in results["results"]["bindings"]:
            stock_exchange_label = result.get("stockExchangeLabel", {}).get("value", "No label available")
            query_results.append(stock_exchange_label)
        return query_results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_number_of_episodes(series_name):
    query = wd_p1113.generate_sparql_query(series_name)
    try:
        results = fetch_from_wikidata(query)
        query_results = []
        for result in results["results"]["bindings"]:
            number_of_episodes = result.get("numberOfEpisodes", {}).get("value", "No label available")
            query_results.append(number_of_episodes)
        return query_results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []