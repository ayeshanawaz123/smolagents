from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=InferenceClientModel()
)
agent.run("Give me the best playlist for a villain masquerade party at Wayne's mansion.")
