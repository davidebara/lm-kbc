def generate_sparql_query(series_name):
    query = f"""
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?numberOfEpisodes
        WHERE
        {{
            ?series rdfs:label "{series_name}"@en.
            ?series wdt:P31 wd:Q5398426.
            ?series wdt:P1113 ?numberOfEpisodes.
        }}
        LIMIT 1
    """
    return query