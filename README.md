# Sunainagoel-langgraph-MAT496
### Module 1:
**Video 1:** Motivation

In this lesson, I learned why LangGraph is useful when building more complex LLM applications. Rather than having to work with straightforward, linear chains, LangGraph allows you to construct dynamic, graph-based workflows with loops, branching, and shared state. This greatly simplifies being able to construct agent-like systems that can make decisions, invoke tools, and evolve as they execute. It also helps with debugging and scaling by giving better visibility into how the flow is working.

**Tweaking:** There was no code provided for this video — it mainly covered the basics and introductory concepts, so there was no tweaking or hands-on implementation to document for this lesson.


**Video 2:** Simple Graph

I understood how to create a basic graph-based workflow with LangGraph, in which every node is either a function or operation, and edges specify how data passes between nodes. I understood how arguments are passed around among nodes and how the graph is executed to produce an output. This practical example helped to better see how LangGraph can substitute linear chains with something more flexible. It's ideal for developing applications that require shared state, branching logic, or improved control.

**Tweaking:** I invoked the original graph again to generate output for node 2, checking how the outputs varied for each node. I enhanced the original graph by adding a “goodbye” node for a proper ending and expanded the mood choices to include “confused.” We used a random selection between the three nodes, and invoked the graph to generate output.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/simple-graph.ipynb


**Video 3:** LangGraph Studio

I explored LangGraph Studio, a visual IDE that makes it easier to build, debug, and test LangGraph workflows. It connects seamlessly with LangSmith, so I could trace runs and fine-tune prompts live. I also learned that each module in the course has its own studio folder, which lets us spin up the studio environment and view the specific graph for that module. It’s a super helpful way to interact with and understand each graph’s structure.

**Tweaking:** Since there wasn’t a notebook provided for this video, I followed the tutorial and successfully ran LangGraph Studio on my local machine. I tested a few basic graph states to ensure everything was working correctly, and everything ran smoothly. I’ve also attached screenshots above as proof of setup and execution.

**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/langgraph-studio.ipynb


**Video 4:** Chain

In this notebook, I learned how to build on simple LangGraph structures by combining different concepts to form a chain. It starts with storing messages in a list to keep track of conversation flow, then introduces a basic tool that performs a single operation. Finally, by connecting the message history, tool, and an LLM, I created a complete graph that executes like a chain — showing how modular components can be combined for richer interactions.

**Tweaking:** I created a new conversation on a different topic to test the flow. I also built a simple tool that adds two numbers, then integrated it into the graph with the model. I observed how sometimes the model chose to handle the question directly, while other times it triggered the tool call.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/chain.ipynb
