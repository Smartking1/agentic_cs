from crewai import Agent
from langchain_qroq import ChatGroq
import os
from langchain_core.agents import AgentAction, AgentFinish
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools


llm = ChatGroq(temperature=0.1, groq_api_key=os.environ["GROQ_API_KEY"], model_name="llama3-70b-8192")

class CustomerSupportAgents():
    def support_agent(self,customer):
        return Agent(
    role="Senior Support Representative",
	goal="Be the most friendly and helpful "
        "support representative in your team",
	backstory =
		"You work at Dell Technologies (https://www.dell.com/support/home/en-us) and "
        " are now working on providing "
		"support to {customer}, a super important customer "
        " for your company."
		"You need to make sure that you provide the best support!"
		"Make sure to provide full complete answers, "
        " and make no assumptions.",
        tools[
            SearchTools.search_internet,
            BrowserTools.scrape_website,

        ],
        verbose = True,
        llm = llm,
        max_iter = 5,
        allow_delegation= False)


    def support_quality_assurance_agent = (self, customer):
        return Agent(
            role = "Support Quality Assurance Specialist",
            goal = "Get recognition for providing the best support quality assurance in your team",
            backstory = "You work at Dell Technologies (https://www.dell.com/support/home/en-us) and "
            "are now working with your team "
            "on a request from {customer} ensuring that "
            "the support representative is "
            "providing the best support possible.\n"
            "You need to make sure that the support representative "
            "is providing full"
            "complete answers, and make no assumptions.",
            tools[
                SearchTools.search_internet,
                BrowserTools.scrape_website,
            ],
        )

      def product_support_agent(self):
        return Agent(
            role='Product Support Expert',
            goal='Assist customers with product issues and troubleshoot solutions.',
            backstory='An experienced support agent at Dell Technologies, specializing in troubleshooting hardware and software issues.',
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_website,
            ],
            verbose=True,
            llm = llm,
            max_iter = 5,
            allow_delegation= False)

    def warranty_service_agent(self):
        return Agent(
            role='Warranty and Service Expert',
            goal='Provide information on warranty coverage, service contracts, and assistance with warranty claims.',
            backstory="""A knowledgeable Dell Technologies representative, specializing in explaining and managing customer warranties, service options, and contract extensions.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_website,
            ],
            verbose=True,
            llm = llm,
            max_iter = 5,
            allow_delegation= False)

    def faq_support_agent(self):
        return Agent(
            role='FAQ Specialist',
            goal='Answer frequently asked questions and assist customers in finding relevant manuals, updates, and troubleshooting tips.',
            backstory="""A seasoned Dell Technologies support agent with expertise in handling common customer issues, providing manuals, and optimizing product performance.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_website,
            ],
            verbose=True,
            llm = llm,
            max_iter = 5,
            allow_delegation= False)

