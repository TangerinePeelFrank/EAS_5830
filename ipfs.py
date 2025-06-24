import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
    
	headers = {
        'pinata_api_key': "7328a830365b6d32db56",
        'pinata_secret_api_key': "4258b90fd40ee48465190b9afb793baf6a2818953fa235110d93859de0f44048"
    }
    
	files = {
        'file': ('data.json', json_data)
    }
	response = requests.post("https://api.pinata.cloud/pinning/pinFileToIPFS", files=files, headers=headers)
    
	if response.status_code == 200:
		cid = response.json()["IpfsHash"]
		return cid
	else:
		raise Exception(response.text)

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	url = f"{"https://gateway.pinata.cloud/ipfs/"}{cid}"
    
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
