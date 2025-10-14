# Sunainagoel-langgraph-MAT496
### Module 1:
**Video 1:** In this lesson, I learned why LangGraph is useful when building more complex LLM applications. Rather than having to work with straightforward, linear chains, LangGraph allows you to construct dynamic, graph-based workflows with loops, branching, and shared state. This greatly simplifies being able to construct agent-like systems that can make decisions, invoke tools, and evolve as they execute. It also helps with debugging and scaling by giving better visibility into how the flow is working.

**Tweaking:** There was no code provided for this video — it mainly covered the basics and introductory concepts, so there was no tweaking or hands-on implementation to document for this lesson.


**Video 2:** I understood how to create a basic graph-based workflow with LangGraph, in which every node is either a function or operation, and edges specify how data passes between nodes. I understood how arguments are passed around among nodes and how the graph is executed to produce an output. This practical example helped to better see how LangGraph can substitute linear chains with something more flexible. It's ideal for developing applications that require shared state, branching logic, or improved control.

**Tweaking:** I invoked the original graph again to generate output for node 2, checking how the outputs varied for each node. I enhanced the original graph by adding a “goodbye” node for a proper ending and expanded the mood choices to include “confused.” We used a random selection between the three nodes, and invoked the graph to generate output.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/simple-graph.ipynb
