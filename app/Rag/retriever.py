def search_historical_data(query):
    results = vectorstore.similarity_search(query, k = 5)
    return results

results = search_historical_data("Who is the top scorer in FPL history?")
for result in results:
    print(result.page_content)