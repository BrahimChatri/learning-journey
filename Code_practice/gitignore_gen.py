"""
    To uses the arguments given at the termenal 
    example to run this  
    python gitignore_ge.py <language>
    and install requests modual
"""

import argparse
import requests

GITIGNORE_BASE_URL = "https://raw.githubusercontent.com/github/gitignore/main/"

def fetch_gitignore(language) -> str | None:
    """Fetch the .gitignore file for the specified language."""
    url: str = f"{GITIGNORE_BASE_URL}{language}.gitignore"
    try:
        response: requests.Response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching .gitignore for {language}: {e}")
        return None

def create_gitignore(language, output_path) -> None:
    """Create a .gitignore file based on the specified language."""
    content: str | None  = fetch_gitignore(language)
    if content:
        with open(output_path, "w") as f:
            f.write(content)
        print(f".gitignore for {language} created at {output_path}")
    else:
        print(f"Failed to create .gitignore for {language}.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a .gitignore file based on programming language.")
    parser.add_argument("language", help="Programming language for the .gitignore template (e.g., Python, Node).")
    parser.add_argument(
        "-o", "--output", default=".gitignore", help="Output file path (default: ./.gitignore)."
    )
    args: argparse.Namespace = parser.parse_args()

    language = args.language.capitalize()  
    output_path = args.output

    create_gitignore(language, output_path)

if __name__ == "__main__":
    main()
