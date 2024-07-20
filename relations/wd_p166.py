def generate_sparql_query(award_name):
    query = f"""
      PREFIX wikibase: <http://wikiba.se/ontology#>
      PREFIX wd: <http://www.wikidata.org/entity/>
      PREFIX wdt: <http://www.wikidata.org/prop/direct/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

      SELECT DISTINCT ?personLabel
      WHERE
      {{
          ?award rdfs:label "{award_name}"@en.
          ?person wdt:P166 ?award.
          ?award wdt:P31/wdt:P279* wd:Q618779. 

      OPTIONAL {{
          ?person rdfs:label ?personLabel filter (lang(?personLabel) = "en").
      }}
      }}
    """
    return query