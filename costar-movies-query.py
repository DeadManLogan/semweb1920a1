from urllib.request import urlopen,Request
from urllib.parse import urlencode
import json
import pprint


# gets all the movies and the costars (for each movie) of a given actor

def sparql_select_query(query,endpoint):

	# params sent to server
	params = { 'query': query }
	# create appropriate param string
	paramstr = urlencode(params)

	# create GET http request object with params appended
	req = Request(endpoint+paramstr)
	# request specific content type
	req.add_header('Accept','application/sparql-results+json')
	# dispatch request
	page = urlopen(req)

	# get response and close
	response = page.read().decode('utf-8')
	page.close()

	# convert to json object
	jso = json.loads(response)


	results = []
	# iterate over results
	for binding in jso['results']['bindings']:
		# for every column in binding
		result = {}
		for bname,bcontent in binding.items():
			result[bname] = bcontent['value']
		
		results.append(result)
	# return the list of result dicts
	return results

first_name = input("Give us the actor's first name: ")
last_name = input("Give us the actor's last name: ")
actor_name = first_name.capitalize() + " " + last_name.capitalize()


# define the endpoint
endpoint = "https://linkedmdb.lodbook.org/sparql?"

# define the sparql select query
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX movie: <http://data.linkedmdb.org/resource/movie/>
PREFIX actor_name: <http://data.linkedmdb.org/resource/movie/actor_name>
SELECT ?actor WHERE
{{
    ?actor movie:actor_name "{}" .
}}
""".format(actor_name)

# get results from endpoint
results = sparql_select_query(query,endpoint)

r = (results[0]['actor'])

# define the sparql select query
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX movie: <http://data.linkedmdb.org/resource/movie/>
PREFIX actor_name: <http://data.linkedmdb.org/resource/movie/actor_name>
SELECT ?moviename ?costaruri ?costar WHERE
{{
    ?s movie:actor <{uri}> .
    ?s rdfs:label ?moviename .
	?s movie:actor ?costaruri .
	?costaruri movie:actor_name ?costar .
	FILTER (?costaruri != <{uri}>)
}}order by ?moviename
""".format(uri = r)

# get results from endpoint
results = sparql_select_query(query,endpoint)

# process list of results here
pprint.pprint(results)