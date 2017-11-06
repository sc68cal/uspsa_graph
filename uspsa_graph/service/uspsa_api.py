from bs4 import BeautifulSoup
import requests



ENDPOINT = "https://uspsa.org/uspsa-classifier-lookup-results.php?number=%s"


def fetch_classifiers(member_number):
    response = requests.get(ENDPOINT % member_number)

    if not response.ok:
        raise Exception("Error returned from USPSA")

    # USPSA's website doesn't gracefully handle invalid member numbers.
    # Surprisingly, when sending totally bullshit data like "FOO", which isn't
    # even a number, you'll get back results for member #A97604.

    # So, we'll just assume someone is putting in a valid member number for
    # now.

    soup = BeautifulSoup(response.text)

    # USPSA's classification lookup page is a table based layout. The 18th
    # innermost table has the actual classification data

    classification_data = list(soup.find_all('table')[18].children)[3]

    return classification_data
