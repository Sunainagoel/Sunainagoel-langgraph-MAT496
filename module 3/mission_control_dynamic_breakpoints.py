from typing_extensions import TypedDict
from langgraph.types import interrupt 
from langgraph.graph import START, END, StateGraph

class MissionState(TypedDict):
    ai_report: str
    control_response: str

def diagnostics(state: MissionState) -> MissionState:
    """Simulates running spacecraft diagnostics."""
    print("---[Step 1: Running Diagnostics]---")
    return {"ai_report": state["ai_report"], "control_response": f"Received report: '{state['ai_report']}'"}


def anomaly_check(state: MissionState) -> MissionState:
    """Analyzes input for critical anomalies and may trigger an interrupt."""
    print("---[Step 2: Checking for Anomalies]---")

    message = state["ai_report"].lower()

    if "critical" in message or "oxygen" in message or "life support" in message:
        raise interrupt(f"Critical anomaly detected! Message: '{state['ai_report']}'")

    print("✅ No anomalies found.")
    return {"ai_report": state["ai_report"], "control_response": state["control_response"] + " | Systems nominal."}


def confirm_mission(state: MissionState) -> MissionState:
    """Confirms the next action in the mission flow."""
    print("---[Step 3: Confirming Mission Continuation]---")
    return {"ai_report": state["ai_report"], "control_response": state["control_response"] + " | Mission confirmed."}

builder = StateGraph(MissionState)

builder.add_node("diagnostics", diagnostics)
builder.add_node("anomaly_check", anomaly_check)
builder.add_node("confirm_mission", confirm_mission)

builder.add_edge(START, "diagnostics")
builder.add_edge("diagnostics", "anomaly_check")
builder.add_edge("anomaly_check", "confirm_mission")
builder.add_edge("confirm_mission", END)

graph = builder.compile()