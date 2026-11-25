"""Build a Google search link pinned to a town, with personalization off. This is the method used for every contest check.

Usage:
    python make_search_link.py "mold remediation gettysburg pa" "Gettysburg,Pennsylvania,United States"
    python make_search_link.py "plumber leeds" "Leeds,England,United Kingdom" --country uk --page 2

The place name must be written the way Google lists it: City,State,Country with no spaces after the commas.
After you open the link, scroll to the bottom of the results. The footer must show your town and "Results are not personalized".
If it shows somewhere else, the place name was not written the way Google lists it.
"""
import sys, base64, urllib.parse

KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

def uule(place):
    return "w+CAIQICI" + KEY[len(place)] + base64.b64encode(place.encode()).decode().rstrip("=")

def link(query, place, country="us", page=1):
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query) + "&hl=en&gl=" + country + "&pws=0&uule=" + uule(place)
    return url + ("&start=" + str((page - 1) * 10) if page > 1 else "")

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    country = a[a.index("--country") + 1] if "--country" in a else "us"
    page = int(a[a.index("--page") + 1]) if "--page" in a else 1
    print(link(a[0], a[1], country, page))
