from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from urllib.error import HTTPError, URLError
from typing import Union


def request_data(url: str) -> Union[BeautifulSoup, None]:
    """Request data from an url

    Args:
        url (str): website url

    Returns:
        A BeautifulSoup object or None if an error occurred

    """
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html.read(), "html5lib")

        return soup
    except HTTPError:
        print("[ERROR]: Page not found!")
    except URLError:
        print("[ERROR]: Server not found!")


def extract_data(soup: BeautifulSoup) -> Union[dict, None]:
    """Extract data from a BeautifulSoup object

    Args:
        soup (BeautifulSoup): Requested data

    Returns:
        Union[dict, None]: Dict with extracted data or None if an error occurred
    """
    try:
        title = soup.title.string
        paragraphs = [link.string for link in soup.find_all("p")]

        return {"Title": title, "Paragraphs": paragraphs}
    except AttributeError:
        print("[Error]: Tag not found!")


def save_data(data: dict, file_name: str = "output.csv") -> bool:
    """Save data into a file

    Args:
        data (dict): Extracted data
        file_name (str): File name

    Returns:
        bool: Successfuly saved or not
    """

    try:
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow([key for key in data.keys()])
            writer.writerow([value for value in data.values()])

            return True
    except Exception as e:
        print(f"[ERROR]: Unexpected error on save_data(): {e}")

    return False


def main() -> None:

    # Request data
    url = "https://raw.githubusercontent.com/PedroFerreiraBento/Python-Projects/main/2-web-scraping-projects/2.1-beautiful-soap/static/example-1.html"
    soup = request_data(url)

    # Extract data
    data = extract_data(soup) if soup is not None else None

    # Save data
    is_saved = save_data(data) if data is not None else None

    if is_saved:
        print("[INFO]: Successfuly extracted data!")


if __name__ == "__main__":
    main()
