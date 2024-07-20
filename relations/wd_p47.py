def generate_sparql_query(country_name):
    query = f"""
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX p: <http://www.wikidata.org/prop/>
        PREFIX ps: <http://www.wikidata.org/prop/statement#>
        PREFIX pq: <http://www.wikidata.org/prop/qualifier#>

        SELECT DISTINCT ?borderingCountryLabel
        WHERE
        {{
            ?country rdfs:label "{country_name}"@en.
            ?country wdt:P47 ?borderingCountry.
            ?borderingCountry wdt:P31/wdt:P279* wd:Q6256. 

            OPTIONAL {{
                ?borderingCountry rdfs:label ?borderingCountryLabel filter (lang(?borderingCountryLabel) = "en").
            }}
            
            MINUS {{
                ?country wdt:P31 wd:Q112099.
            }}

            MINUS {{
                ?country p:P47 ?borderingStatement.
                ?borderingStatement ps:P47 ?borderingCountry.
                ?borderingStatement pq:P582 ?endTime.
            }}
        }}
    """
    return query