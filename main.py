import requests
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree
from flask import Flask,request, jsonify
app = Flask(__name__)


def get_social_links(domain_name):
    res = requests.get('http://www.{}'.format(domain_name))
    tree = parse_html_bytes(res.content, res.headers.get('content-type'))
    social_links = set(find_links_tree(tree))
    out_dict = {}
    for item in social_links:
        if "facebook" in item:
            out_dict["facebook"] = item
        if "twitter" in item:
            out_dict["twitter"] = item
        if "linkedin" in item:
            out_dict["linkedin"] = item
        if "youtube" in item:
            out_dict["youtube"] = item
    return out_dict

@app.route('/social-media-handles',methods=['POST'])
def get_handles():
    data = request.get_json(force=True)
    return jsonify(get_social_links(data['domain']))
if __name__ == "__main__":
    app.run()

    
