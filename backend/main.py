from consts import ROOT
from src.scraper import dump_to_json, fetch_list_opt_term, load_from_json


JSON_DATA_PATH = ROOT / "frontend" / "src" / "data" / "list_opt_term.json"


def main():
    list_opt_term = fetch_list_opt_term()
    dump_to_json(list_opt_term, JSON_DATA_PATH)
        


if __name__ == "__main__":
    main()
