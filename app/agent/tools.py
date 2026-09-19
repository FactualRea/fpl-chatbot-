from langchain_core.tools import tool

from app.Rag.retriever import search_historical_data


@tool
def get_player(name: str):
    """
    Get current FPL information about a player.
    """

    player_service = PlayerService()

    players = player_service.find_player(name)

    return players

@tool
def search_history(query: str):
    """
    Search historical FPL information.
    """

    results = search_historical_data(query)

    return [result.page_contentforresult in results]

@tool
def compare_players(player_a: str, player_b: str):
    """
    Compare two FPL players using current and historical data.
    """

    ...