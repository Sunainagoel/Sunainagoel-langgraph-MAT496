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


**Video 5:** Router

To explore routing behavior, I created a simple tool and added it to the tools list. I then allowed the LLM to decide when to use it, based on a predefined tools condition. When asked a relevant question, the LLM triggered the tool correctly; for unrelated queries, it chose to respond directly without calling the tool. This helped me understand how the model intelligently routes between using its own reasoning and external tools based on context.

**Tweaking:** I created a custom divide tool to see how adding tools affects the graph. When a division-related question was asked, it correctly triggered the new tool, confirming it worked. I also updated the .py file with the new tool, and added screenshots.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/router.ipynb


**Video 6:** Agent

Built a simple agent using multiple arithmetic tools and followed the ReAct architecture, where the model thinks, acts by calling tools, and observes the results before continuing. The goal was to have the model solve a multi-step arithmetic problem, involving a sequence of tool calls. The model intelligently decided when to call which tool, and repeated the process until it arrived at the final answer, showcasing how LangGraph supports dynamic reasoning in a loop.

**Tweaking:** I expanded the toolset to include five arithmetic operations: add, subtract, multiply, divide, and power. The model handled multi-step reasoning well, chaining tools as needed. I also tracked the entire process on LangSmith to observe how the execution unfolded. The screenshots are included for reference.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/agent.ipynb


**Video 7:** Agent with Memory

I explored how memory can be added to agents. I created a thread ID that allows the agent to reference previous interactions, enabling follow-up questions to be answered in context. This helped maintain continuity across multiple queries. Interestingly, LangGraph’s dev mode includes a built-in persistence layer, which automatically manages memory by integrating with the API key—making it much easier to track and recall past states without manual setup.

**Tweaking:** I extended toolset and tested memory by creating a thread where the final question depended on earlier steps. The model successfully referenced previous results, showing memory retention works. I also confirmed LangGraph Studio’s built-in persistence layer handles memory automatically.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent-memory.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%201/agent-memory.ipynb


**Video 8:** Intro to Deployment (Optional)

Since LangSmith Deployment is currently only available for LangSmith Plus users and Lesson 8 is optional, I just went through the video to understand the concept but didn’t implement anything. I learned how to move beyond local development and actually deploy a LangGraph application so it can be used as a service or API. The lesson covered how to package the graph, manage secrets and environment variables, enable persistence, and expose graph endpoints for external use.


### Module 2:
**Video 1:** State Schema

In this video, I learned that a schema defines the structure and data types used in a graph. We’ve been using TypedDict for this, and also looked at dataclasses, which are similar but use the dot (.) operator to access values. The issue with both is that type hints aren’t enforced at runtime, so invalid data won’t raise errors. To address this, Pydantic comes in handy, as it not only supports type hints but also performs automatic data validation to ensure the inputs are correct.

**Tweaking:** I created my own graph that checks whether a task is completed or still pending using Pydantic, and observed how it handles both valid and invalid inputs.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-schema.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/state-schema.ipynb
