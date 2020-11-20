import requests

# Username of Gists
username = 'linuxkathirvel'
# Gists API URL
gists_url = 'https://api.github.com/users/linuxkathirvel/gists'
# Results per page (max 100)
per_page = 100
# Page number of the results to fetch.
page = 1001
# Headers values
headers = {
    'accept':'application/vnd.github.v3+json'
}
# Parameters to GET method
payload = {'per_page': per_page,}

gists_list = []

for page_number in range(1, page):
    payload['page'] = page_number
    r = requests.get(gists_url, params=payload)
    if r.status_code == 200:
        gists = r.json()
        if gists:
            for gist in gists:
                gists_list.append(
                    {
                        'html_url': gist.get('html_url'),
                        'description': gist.get('description') if gist.get('description') else gist['files']
                    }
                )
        else:
            break
    else:
        print("Status code:", r.status_code)
if gists_list:
    for count, gist in enumerate(gists_list):
        print(count, gist.get('html_url'), gist.get('description'))
else:
    print("No Gists.")
