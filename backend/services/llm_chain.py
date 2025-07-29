from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType

def get_llm_agent():
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0.3)
    memory = ConversationBufferMemory()
    return initialize_agent(
        tools=[],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory
    )
