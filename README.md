# Multi-Agent AI Project using SmolAgents

## Overview
This project demonstrates the use of **SmolAgents**, a lightweight Python framework for building **multi-agent AI systems**.  
The system consists of several specialized agents working together to perform complex tasks in a modular and scalable way.

The goal of this project is to experiment with **agent delegation, task orchestration, and tool integration** without relying on paid APIs.

---

## Features
- **RAG Agent (`Rag.py`)**: Implements a Retrieval-Augmented Generation agent for answering queries using local or simulated knowledge.  
- **Alfred Agent (`alfred_agent.py`)**: A manager agent inspired by Alfred from Batman, orchestrating tasks for other agents.  
- **Custom Base (`custombase.py`)**: Base classes and utilities shared among different agents.  
- **Menu Agent (`menu_agent.py`)**: Handles tasks related to menus, planning, and organizing content.  
- **Party Agent (`party_agent.py`)**: Handles party-themed tasks, such as creating ideas, menus, or event planning.

---

## Tech Stack
- Python 3.10+
- [SmolAgents](https://github.com/your-link-to-smolagents) for multi-agent orchestration
- HuggingFace Transformers (free models)
- Optional: Plotly or other visualization libraries for output

---

## How It Works
1. **Manager Agent** receives a complex task (e.g., plan party or query RAG).  
2. **Sub-agents** (Menu Agent, Party Agent) perform specialized subtasks.  
3. **Custom base classes** handle shared logic and utilities for agents.  
4. **Results aggregation** happens via the manager or orchestrator agent.  

> The system demonstrates **agent delegation, planning intervals, and modular agent architecture**.

---


