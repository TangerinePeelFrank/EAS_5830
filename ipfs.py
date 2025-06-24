import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	post = requests.post("https://ipfs.infura.io:5001/api/v0", files={"file": json_data})
	if post.status_code == 200:
		cid = post.json().get("Hash")
		return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	response = requests.post(f"https://ipfs.infura.io:5001/api/v0/cat?arg={cid}")
	if response.status_code == 200:
		if content_type == "json":
			data = json.loads(response.text)
		else:
			data = response.text
            
		assert isinstance(data, dict), f"get_from_ipfs should return a dict"
		return data
	else:
		raise Exception(f"Error fetching data from IPFS: {response.text}")

	return data
