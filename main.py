from flask import Flask
import requests 
app = Flask(__name__)

@app.route('/<search_query>')
def get_poshmark_data(search_query):
    # search_query = "Zara Trafaluc White Tank Top"
    search_query = search_query.replace(" ", "%20")
    response = requests.get("https://poshmark.ca/vm-rest/posts?request={%22filters%22:{%22department%22:%22All%22,%22inventory_status%22:[%22available%22]},%22query_and_facet_filters%22:{%22department%22:%22All%22},%22query%22:%22" + search_query + "%22,%22facets%22:[%22brand%22,%22color%22,%22department%22],%22experience%22:%22all%22,%22sizeSystem%22:%22us%22,%22count%22:%2248%22}&summarize=true&feature_extraction_setting=null&suggested_filters_count=40&summarize=true&pm_version=197.0.0")
    #print(response.json())
    data = response.json()
    first_item = data["data"][0]
    first_item_name = data["data"][0]["title"]
    return first_item_name + "|" + data["data"][0]["pictures"][0]["url"]


    for x in range(0, 2):
      print(data["data"][x]["title"])
    print(data["data"][x]["pictures"][0]["url"])

print(get_poshmark_data("Zara Tank Top"))
app.run(host = "0.0.0.0")