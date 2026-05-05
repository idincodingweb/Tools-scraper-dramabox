import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from .client import DramaBoxClient


def _dump(data: dict, output: str | None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if output:
        Path(output).write_text(text, encoding="utf-8")
        print(f"Saved to {output}")
        return
    print(text)


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="DramaBox scraper CLI")
    parser.add_argument("-o", "--output", help="Save result json to file")

    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search drama")
    p_search.add_argument("keyword")
    p_search.add_argument("--page", type=int, default=1)
    p_search.add_argument("--size", type=int, default=20)

    p_latest = sub.add_parser("latest", help="Get latest dramas")
    p_latest.add_argument("--page", type=int, default=1)
    p_latest.add_argument("--size", type=int, default=20)

    p_detail = sub.add_parser("detail", help="Get drama detail")
    p_detail.add_argument("drama_id")

    p_eps = sub.add_parser("episodes", help="Get drama episodes")
    p_eps.add_argument("drama_id")
    p_eps.add_argument("--page", type=int, default=1)
    p_eps.add_argument("--size", type=int, default=100)

    args = parser.parse_args()

    client = DramaBoxClient()
    try:
        if args.command == "search":
            result = client.search(args.keyword, args.page, args.size)
        elif args.command == "latest":
            result = client.latest(args.page, args.size)
        elif args.command == "detail":
            result = client.detail(args.drama_id)
        else:
            result = client.episodes(args.drama_id, args.page, args.size)
        _dump(result, args.output)
    finally:
        client.close()


if __name__ == "__main__":
    main()
