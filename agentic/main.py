import os
from crewai import crew
from support_agents import CustomerSupportAgents
from support_tasks import  SupportTasks
import streamlit as st


support_agents = CustomerSupportAgents()
support_tasks = SupportTasks()


#App header
st.title('Dell Technologies AI Customer Support Agent')
st.subtitle('Get quick response to your queries')

st.write("All agents will work together to handle the query across multiple tasks.")

#Agent selection
st.sidebar.header('Select Customer Support Agents')

#Allow selecting multiple Agents
agents =[
    support_agents.support_agent(customer = 'Dell Customer'),
    support_agents.support_quality_assurance_agent(customer = 'Dell Customer'),
    support_agents.product_support_agent(),
    support_agents.warranty_service_agent(),
    support_agents.faq_support_agent()
]

# User input for the query
st.header("Customer Query Input")
customer_name = st.text_input('Enter Customer Name:')
product_category st.text_input('Enter Issue Type (e.g., Warranty, Hardware Failure):')
issue_type = st.text_input('Enter Customer Location')
inquiry = st.text_area('Enter the inquiry or issue:', height=200)

#once the user submits, generate all tasks and execute the crew

if st.button('Submit Query and Execute'):
    if not customer_name or not product_category or not issue_type or not inquiry:
        st.warning('Please provide all necessary inputs!')\
    else:
        webscrape_task = support_tasks.webscrape_task(
            agent = None,
            product_category = product_category,
            issue_type = issue_type,
            customer_location = customer_location
        )

        inquiry_task = support_tasks.inquiry_resolution(
            customer = customer_name,
            inquiry = inquiry,
            person = customer_name

        )

        quality_assurance_task = support_tasks.quality_assurance_task(
            customer = customer_name
        )





        #Add all tasks to the crew and execute with all agents
        tasks = [webscrape_task, inquiry_task, quality_assurance_task]


        #initialize the crew with all agents and tasks
        crew = Crew(
            agents = agents,
            tasks = tasks,
            full_output = True,
            verbose= True,
            output_log_file = True
        )

        #Kick off the execution 
        result = crew.kickoff()


        #Display the response from the crew
        st.subheader('Crew Response:')
        st.write(result)


        #Display the expected output
        st.subheader('Response')
        for task in tasks:
            st.write(task.response)



