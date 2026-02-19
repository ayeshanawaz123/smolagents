from smolagents import tool

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.

    Args:
        occasion (str): Type of party. Allowed values:
                        - "casual": Casual party
                        - "formal": Formal party
                        - "superhero": Superhero party
                        - "custom": Custom menu
    Returns:
        str: Suggested menu as a string.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
print(suggest_menu("formal"))
