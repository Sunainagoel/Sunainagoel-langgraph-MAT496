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


**Video 2:** State Reducers

In this video, we examined reducers. These are responsible for managing how state updates occur for specific keys or channels in a schema. I learned that if two nodes try to update the same shared state simultaneously, it can lead to a value error. This is where state reducers become important. We used Annotated to handle this issue. Sometimes, we may need to create custom reducers instead of using Python’s built-in ones, particularly for special cases like null values. We also discussed message state reducers and the add_reducer method. This method allows us to add, overwrite (using IDs), or delete messages with the built-in RemoveMessage reducer.

**Tweaking:** I tested the built-in message reducers provided by LangGraph using a few examples. I also created a custom reducer and built a graph where each node adds 1, 3, and 5, then ran several test cases to verify that the custom reducer was working correctly.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-reducers.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/state-reducers.ipynb


**Video 3:** Multiple Schemas

In this video, I learned that most graphs use a single schema for both input and output, but sometimes we need more control. Some internal nodes may generate data that’s only used within the graph and shouldn’t be part of the final output. To handle this, we can use private state, which stores internal information without exposing it to the user. I also learned that while StateGraph uses one main schema for communication, we can define separate input, output, and internal schemas for better organization and control.

**Tweaking:** I built a graph simulating a bank account with deposits and withdrawals. I also created a graph that processes travel destinations, generates information, and outputs personalized messages using input and output schemas.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/multiple-schemas.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/multiple-schemas.ipynb


**Video 4:** Trim and Filter Messages

In this video, we learned how to manage messages in long-running conversations. Since long message histories can increase latency and token costs when passed into the graph, it becomes inefficient and expensive. To address this, we can keep only the most recent messages and delete older ones using “RemoveMessages.” Alternatively, we can filter the messages sent to the chat model without altering the stored state, sending only a subset of messages. Another approach is trimming messages based on a token limit, which helps the model respond faster and reduces costs.

**Tweaking:** I applied all three message management methods from the tutorial. First, I created a graph that trims the graph state to keep only the last three messages, deleting older ones using built-in reducer functions, and tested it with different message examples. Then, I set up a filter node that passes only the most recent two messages to the model without altering the stored message history. Lastly, I built a graph that automatically trims input messages exceeding 250 tokens before invoking the model, effectively managing token limits and improving efficiency during long conversations.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/trim-filter-messages.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/trim-filter-messages.ipynb


**Video 5:** Chatbot w/ Summarizing Messages and Memory

In this video, I learned how to build a chatbot that automatically summarizes past messages once their count exceeds six, effectively reducing the LLM’s context size. I also explored adding memory through a checkpointer to save the graph state after each interaction, enabling the chatbot to remember conversations across sessions. This persistence makes chatbots more practical and efficient for long-term use.

**Tweaking:** I changed the example to a casual chatbot about everyday topics. It uses MemorySaver to keep conversation memory and summarizes messages once they exceed six, retaining only the last two afterward. This reduces the LLM context size, improving speed and lowering costs while maintaining the conversation flow. I also worked with conversation threads and reviewed their behavior in the Langsmith portal, with screenshots included below.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/chatbot-summarization.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/chatbot-summarization.ipynb


**Video 6:** Chatbot w/ Summarizing Messages and External Memory

In this video, I learned that LangGraph supports both in-memory and external memory checkpoints like Postgres and SQLite. In-memory checkpoints retain conversation memory only while the notebook runs, whereas external checkpoints store conversations indefinitely in a database. We tested persistence by restarting the notebook to verify if threads were saved locally. Additionally, LangGraph Studio automatically adds a persistence layer (Postgres) when running chatbots. I also explored how the chatbot functions in LangGraph Studio and included screenshots in the notebook below.

**Tweaking:** I modified my chatbot to connect its memory to a local external database using SQLite, enabling persistent conversation storage beyond the notebook session. I tested this by restarting the notebook to confirm that the conversation was saved indefinitely. I also explored the chatbot’s behavior in LangGraph Studio, where an automatic persistence layer (Postgres) is added. I tested this by restarting the conversation there as well, and attached screenshots of these tests in the notebook below.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/chatbot-external-memory.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%202/chatbot-external-memory.ipynb


### Module 3:
**Video 1:** Streaming

In this notebook, I learned how to stream responses and intermediate states from a LangGraph chatbot in real time. I understood the difference between streaming updates, full graph states, and token-level outputs. This makes it easier to track progress while the model is responding. I also explored how interruptions and resumptions can be handled seamlessly, and how LangGraph Studio enables smooth message streaming through its built-in API.

**Tweaking:** I changed the theme of the chatbot to a travel assistant that helps plan trips and give destination ideas. I tested streaming in different modes using travel-related prompts like planning itineraries and finding destinations. I also observed how the chatbot summarized long conversations after four messages and maintained context using memory checkpoints.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/streaming-interruption.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/streaming-interruption.ipynb


**Video 2:** Breakpoints

Through this notebook, we explored how LangGraph enables human-in-the-loop AI workflows using breakpoints. We learned how to build a simple agent capable of performing arithmetic operations, pause its execution before tool use, inspect its internal state, and then either resume or stop it. This gave us insight into how breakpoints can support approval, debugging, and state editing — key concepts for creating transparent and controllable AI systems. We also saw how LangGraph manages memory checkpoints, allowing an agent to pause and resume seamlessly.

**Tweaking:** We customized the notebook by adding our own tools like power, trying new prompts, and introducing a user approval step to manually control the agent’s actions — making the workflow more interactive and realistic.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/breakpoints.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/breakpoints.ipynb


**Video 3:** Editing State and Human Feedback

I understood how to stop, examine, and modify the internal state of an AI agent with LangGraph breakpoints. I realized how breakpoints enable us to halt the graph anywhere, look at what the agent is considering, and even alter the messages or inputs before resuming. This explained how human-in-the-loop systems can enable corrections, feedback, and transparency in AI processes. I also realized how the memory checkpoints enable the agent to stop and resume seamlessly without any loss of progress — similar to monitoring a conversation in real time.

**Tweaking:** Added more tools to the tools list provided to the chat model. Changed the arithmetic expressions and operations inputted to the graph. Tested how editing the graph’s state affected the results.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/edit-state-human-feedback.ipynb
**My Code:** https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/edit-state-human-feedback.ipynb


**Video 4:** Dynamic Breakpoints

This notebook helped me grasp how LangGraph manages state transitions, dynamic breakpoints, and real-time interruptions in a workflow. I learned how each node executes its logic while sharing a unified state across the graph, and how interrupts can pause execution until the state is updated or approved. This showed me how LangGraph goes beyond simple automation — enabling adaptive, human-in-the-loop systems that can reason, react, and continue intelligently.

**Tweaking:** I transformed the base example into a Mission Control simulation, applying key LangGraph concepts like conditional interrupts, state inspection, and state updates. Renamed the nodes to diagnostics, anomaly_check, and confirm_mission, and added triggers that respond to words like “oxygen” or “critical”.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/dynamic-breakpoints.ipynb
**My Code:** (https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/dynamic-breakpoints.ipynb), (https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/mission_control_dynamic_breakpoints.py)


**Video 5:** Time Travel

I learned how LangGraph supports advanced debugging and exploration of agent behavior using time travel, replaying, and forking. Each state of the graph is captured as a StateSnapshot, allowing inspection of the current state or the entire history. I learned how to replay a graph from any checkpoint without re-executing and how forking lets me modify a previous state, create a new checkpoint, and re-execute to explore alternative outcomes. Using the correct message ID ensures updates overwrite rather than append messages. LangGraph Studio also provides a visual way to experiment with forking and alternative trajectories, making it easier to debug and test agent behavior step by step.

**Tweaking:** I adapted the notebook into a fuel monitoring scenario. I renamed the nodes, added interrupts for critical fuel conditions, and practiced pausing the graph, inspecting and updating state, and resuming execution. Demonstrating the concepts dynamic breakpoints, conditional interrupts, and interactive state management as well.

**Source Code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/time-travel.ipynb
**My Code:** (https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/time-travel.ipynb), (https://github.com/Sunainagoel/Sunainagoel-langgraph-MAT496/blob/main/module%203/fuel.py)
