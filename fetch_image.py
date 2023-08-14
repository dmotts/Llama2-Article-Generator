import requests

def fetch_photo(query):
    api_key = 'kWmCxiNE7hh1uiLSsyKGi110yApV0mEGMFON10LDXbb9zp3bt4X0Zlfp'

    url =  'https://api.pexels.com/v1/search'

    headers = {
        'Authorization': api_key
    }

    params = {
        'query': query,
        'per_page': 1
    }

    response = requests.get(url, headers=headers, params=params)

    #Check if the request was successful (status code is 200)

    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            src_original_url = photos[0]['src']['original']
            return src_original_url
        else:
            print("No photos found!")

    else:
        print(f"Error:  {response.status_code}, {response.text}")

        return None

#Example usage of this function
query = "Circular Economy"

src_original_url = fetch_photo(query)

if src_original_url:
    print(f"Original URL for '{query}': {src_original_url}")