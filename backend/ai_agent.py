

# PHASE 2 : ________________________________ SETUP AI-AGENT & TOOLS ________________________________ #

from langchain.agents import tool
from tools import query_medgemma, call_emergency


# Step1: ------------------------------ Create an AI Agent & Link to backend ------------------------------ #

from langgraph.prebuilt import create_react_agent
from config import  GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
# from config import OPENAI_API_KEY
# from config import  GROQ_API_KEY
# from langchain.schema import HumanMessage, SystemMessage



# ------------------------------------- TOOLS--------------------------------------- #

@tool
def ask_mental_health_specialist(query: str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this for all general user queries, mental health questions, emotional concerns,
    or to offer empathetic, evidence-based guidance in a conversational tone.
    """
    return query_medgemma(query)



# Emergency tool
@tool
def energency_call_tool(phone: str) -> str:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    """
    return call_emergency(phone)


@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    return (
        f"Here are some therapists near {location}, {location}:\n"
        "- Dr. Naseem Chaudhry - +92 (300) 123-4567\n"
        "- Dr. Ghulam Rasool - +92 (301) 987-6543\n"
        "- MindCare Counseling Center - +92 (333) 222-3333"
    )




# ----------------------------- LLM + GRAPH ----------------------------- #

tools = [ask_mental_health_specialist, energency_call_tool, find_nearby_therapists_by_location]
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=OPENAI_API_KEY)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # or "gemini-1.5-pro"
    temperature=0.2,
    google_api_key=GEMINI_API_KEY) 
graph = create_react_agent(llm, tools=tools)

for chunk in llm.stream("Explain me RAG in simple words."):
    print(chunk.content, end="", flush=True)


SYSTEM_PROMPT = """
You are an AI engine supporting mental health conversations with warmth and vigilance.
You have access to three tools:

1. `ask_mental_health_specialist`: Use this tool to answer all emotional or psychological queries with therapeutic guidance.
2. `locate_therapist_tool`: Use this tool if the user asks about nearby therapists or if recommending local professional help would be beneficial.
3. `emergency_call_tool`: Use this immediately if the user expresses suicidal thoughts, self-harm intentions, or is in crisis.

Always take necessary action. Respond kindly, clearly, and supportively.
"""


# ----------------------------- PARSER ----------------------------- #

def parse_response(stream):
    tool_called_name = "None"
    final_response = None

    for s in stream:
        # Check if a tool was called
        tool_data = s.get('tools')
        if tool_data:
            tool_messages = tool_data.get('messages')
            if tool_messages and isinstance(tool_messages, list):
                for msg in tool_messages:
                    tool_called_name = getattr(msg, 'name', 'None')

        # Check if agent returned a message
        agent_data = s.get('agent')
        if agent_data:
            messages = agent_data.get('messages')
            if messages and isinstance(messages, list):
                for msg in messages:
                    if msg.content:
                        final_response = msg.content

    return tool_called_name, final_response
























        



"""if __name__=="__main__":
    while True:
        user_input = input("User: ")
        print(f"Recieved user input: {user_input[:200]}...")
        # inputs = {"messageS": [("system", SYSTEM_PROMPT), ("user", user_input)]}
        inputs = {"messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=user_input)]}
        stream = graph.stream(inputs, system_mode="updates")
        tool_called_name, final_response = parse_response(stream)
        print("TOOL CALLED: ", tool_called_name)
        print("ANSWER: ", final_response) """

        
        
        
        
        
        
        
        
        
        
        # Process the stream of updates
        # for update in stream:
        #     for value in update.values():
        #         if "messages" in value:  # check correct key
        #             msg = value["messages"][-1]
        #             if msg["role"] == "assistant":
        #                 print("assistant:", msg["content"])

        # for s in stream:
        #     print(s)

    
    