from bs4 import BeautifulSoup

def get_links(html):
    """
    Making soup and getting all the juicy stuff
    """
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all("input", attrs={"class" : "viewButton", "type":"submit"})

    links = []
    for item in table:
        link = item.get("onclick")[26:78]   # use regex to make this more robust
        links.append(link)
    return links

if __name__ == "__main__":
    f = open("georgia.html")
    html = f.read()
    f.close
    links = get_links(html)
    base_url = "https://www.georgiapublicnotice.com/"
    with open("search_result.txt", "w") as f:
        for link in links:
            f.write(base_url + link + "\n")


# import requests, pickle
# session = requests.session()
# # Make some calls
# with open('somefile', 'wb') as f:
#     pickle.dump(session.cookies, f)

# session = requests.session()  # or an existing session

# with open('somefile', 'rb') as f:
#     session.cookies.update(pickle.load(f))