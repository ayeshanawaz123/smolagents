from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

search_tool = DuckDuckGoSearchTool()

model = InferenceClientModel(
    model_id="mistralai/Mistral-7B-Instruct-v0.2"
)

agent = CodeAgent(
    model=model,
    tools=[search_tool],
)

print("Agent running...")

response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)

print("Response received:")
print(response)
