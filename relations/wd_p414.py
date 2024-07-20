def generate_sparql_query(company_name):
    query = f"""
      PREFIX wikibase: <http://wikiba.se/ontology#>
      PREFIX wd: <http://www.wikidata.org/entity/>
      PREFIX wdt: <http://www.wikidata.org/prop/direct/>
      PREFIX p: <http://www.wikidata.org/prop/>
      PREFIX ps: <http://www.wikidata.org/prop/statement/>
      PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

      SELECT ?stockExchangeLabel
      WHERE
      {{
          ?company rdfs:label "{company_name}"@en.
          ?company wdt:P414 ?stockExchange.
          
          OPTIONAL {{
              ?stockExchange rdfs:label ?stockExchangeLabel.
              FILTER (lang(?stockExchangeLabel) = "en")
          }}
      }}

    """
    return query