import requests
import json

pinata_pin_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
pinata_gateway_url = "https://gateway.pinata.cloud/ipfs/"
api_key = "7328a830365b6d32db56"
api_secret = "4258b90fd40ee48465190b9afb793baf6a2818953fa235110d93859de0f44048"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
    
	headers = {
        'pinata_api_key': api_key,
        'pinata_secret_api_key': api_secret
    }
    
	files = {
        'file': ('data.json', json_data)
    }
	response = requests.post(pinata_pin_url, files=files, headers=headers)
    
	if response.status_code == 200:
		cid = response.json()["IpfsHash"]
		return cid
	else:
		raise Exception(response.text)

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	url = f"{pinata_gateway_url}{cid}"
    
	response = requests.get(url)
    
	if response.status_code == 200:
		if content_type == "json":
			data = response.json()
			assert isinstance(data, dict), "get_from_ipfs should return a dict"
			return data
		else:
			raise Exception("Not a dict")
	else:
		raise Exception(response.text)
