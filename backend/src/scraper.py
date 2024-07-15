import json
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from src.schema import OptTerm

BASE_URL = "https://www.msi.co.jp/solution/nuopt/docs/glossary"


def get_list_term_dict() -> dict[str, str]:
    response = requests.get(f"{BASE_URL}/index.html")
    soup = BeautifulSoup(response.content, "html.parser")
    term2url = {}
    for item in soup.find_all("li", class_="toctree-l1"):
        term = item.find("a").text.strip()
        url = item.find("a").get("href")
        term2url[term] = url

    return term2url


def fetch_list_opt_term() -> list[OptTerm]:
    list_opt_term: list[OptTerm] = []
    term2url = get_list_term_dict()
    for term, article_url in tqdm(term2url.items()):
        term_url = f"{BASE_URL}/{article_url}"
        response = requests.get(term_url)
        soup = BeautifulSoup(response.content, "html.parser")
        list_reference = soup.find_all("a", class_="reference external")

        list_related_term = []
        for reference in list_reference:
            reference_term = reference.text.strip()
            if reference_term not in term2url.keys():
                continue
            list_related_term.append(reference_term)
        list_related_term = list(set(list_related_term))
        list_opt_term.append(
            OptTerm(term=term, url=term_url,
                    list_related_term=list_related_term)
        )
        time.sleep(1)

    return list_opt_term


def dump_to_json(list_opt_term: list[OptTerm], dir_path):
    with open(dir_path, "w", encoding="utf-8") as f:
        json.dump([opt_term.model_dump()
                  for opt_term in list_opt_term], f, ensure_ascii=False, indent=4)


def load_from_json(filename: str) -> list[OptTerm]:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [OptTerm(**item) for item in data]
    except IOError as e:
        print(f"An error occurred while loading the file: {e}")
        return []
