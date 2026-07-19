from src.database import query_database

results = query_database(
    sport="Cricket",
    query_text="World Cup history",
    n_results=2
)

print("\nRetrieved Facts:\n")

for fact in results:
    print("-", fact)