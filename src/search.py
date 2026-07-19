from ddgs import DDGS      

def get_live_news(sport):
    """
    Fetches the latest news snippets for the selected sport.
    """

    query = f"{sport} latest news tournaments championships"

    snippets = []
    seen_titles = set()

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)

            for result in results:
                title = result.get("title", "")
                body = result.get("body", "")

                if title in seen_titles:
                    continue

                seen_titles.add(title)
                snippets.append(f"{title}\n{body}")

                if len(snippets) == 3:
                    break

    except Exception as e:
        print("Search Error:", e)
        return "No live news available."

    return "\n\n".join(snippets)