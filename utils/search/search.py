import sys
import webbrowser
from googlesearch import search

def main(args):
    print('🔍 This feature is in alpha.')

    if not args:
        print("❌ You must provide a search query.")
        return

    query = " ".join(args).strip()
    print(f"Searching Google for: {query}")

    try:
        # Get top 10 search results
        results = list(search(query, num_results=10))

        if not results:
            print("❌ No results found.")
            return

        valid_links = []

        # Filter and display only valid HTTPS links
        for idx, url in enumerate(results, 1):
            if url.startswith("https://"):
                valid_links.append(url)
                print(f"{len(valid_links)}. {url}")
            # Stop after 5 good links
            if len(valid_links) >= 5:
                break

        if not valid_links:
            print("❌ No valid HTTPS results found.")
            return

        top_link = valid_links[0]
        print(f"\n🚀 Opening top result: {top_link}")
        webbrowser.open(top_link)

    except Exception as e:
        print(f"❌ Search failed: {e}")

