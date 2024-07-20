def generate_sparql_query(person_name):
    query = f"""
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?placeLabel
        WHERE
        {{
            ?person rdfs:label "{person_name}"@en.
            ?person wdt:P20 ?place.
            ?person wdt:P31 wd:Q5.
            
            OPTIONAL {{
                ?place rdfs:label ?placeLabel filter (lang(?placeLabel) = "en").
            }}
        }}
    """
    return query