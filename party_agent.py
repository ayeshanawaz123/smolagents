from smolagents import Tool, tool
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.

    Args:
        occasion (str): The type of occasion for the party. Allowed values:
                        "casual", "formal", "superhero", "custom".

    Returns:
        str: The suggested menu for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
@tool
def catering_service_tool(query: str) -> str:
    """
    Returns the highest-rated catering service in Gotham City.

    Args:
        query (str): A search term for finding catering services.

    Returns:
        str: The name of the best catering service.
    """
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }
    return max(services, key=services.get)
class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = "Suggests creative superhero-themed party ideas based on a category."
    
    inputs = {
        "category": {
            "type": "string",
            "description": "Type of superhero party ('classic heroes', 'villain masquerade', 'futuristic Gotham')",
        }
    }
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes.",
            "villain masquerade": "Gotham Rogues' Ball: Guests dress as classic Batman villains.",
            "futuristic gotham": "Neo-Gotham Night: Cyberpunk-style party with neon decorations."
        }
        return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")
print("Menu tool output:", suggest_menu("formal"))
print("Catering tool output:", catering_service_tool("best catering in Gotham"))

theme_tool = SuperheroPartyThemeTool()
print("Theme tool output:", theme_tool.forward("villain masquerade"))
