from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

def calculate_fuel_needed(distance: float, efficiency: float) -> float:
    """Calculates fuel needed for a trip based on distance and efficiency.
    
    Args:
        distance: distance to travel in kilometers
        efficiency: fuel efficiency in km per liter
    """
    return distance / efficiency

def remaining_fuel_after_trip(current_fuel: float, fuel_needed: float) -> float:
    """Calculates remaining fuel after a trip.
    
    Args:
        current_fuel: current fuel in liters
        fuel_needed: fuel required for the trip in liters
    """
    return current_fuel - fuel_needed

def suggest_refuel(current_fuel: float, distance: float, efficiency: float) -> str:
    """Suggests whether refueling is needed for a trip."""
    fuel_needed = calculate_fuel_needed(distance, efficiency)
    remaining = remaining_fuel_after_trip(current_fuel, fuel_needed)
    if remaining < 0:
        return f"Refuel required! Trip requires {fuel_needed}L but only {current_fuel}L available."
    elif remaining < 10:
        return f"Warning: Low fuel. Trip requires {fuel_needed}L; only {current_fuel}L available."
    else:
        return f"Fuel sufficient. Trip requires {fuel_needed}L; {remaining}L will remain."

tools = [calculate_fuel_needed, remaining_fuel_after_trip, suggest_refuel]

llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(
    content="You are a helpful assistant providing fuel calculation guidance for trips."
)

def assistant(state: MessagesState):
    """Invokes LLM with current messages state."""
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition 
)
builder.add_edge("tools", "assistant")

graph = builder.compile(interrupt_before=["tools"])
