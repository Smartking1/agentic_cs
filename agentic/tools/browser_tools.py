import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools:

    @tool("Scrape website content")
    def scrape_website(website):
        """Useful to scrape and summarize a website's content"""
        
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {"cache-control": "no-cache", "content-type": "application/json"}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        
        responses = []
        for chunk in content:
            agent = Agent(
                role='Customer Support Specialist',
                goal="Provide exceptional customer support by analyzing the information from the website and responding to the customer query with a detailed and helpful solution.",
                backstory="You are a customer support specialist at Dell Technologies, helping a customer resolve an issue related to one of Dell’s products or services.",
                allow_delegation=False
            )

            task = Task(
                agent=agent,
                description=f"Analyze the following website content and respond with a clear, well-structured support message addressing customer concerns. Ensure the response is concise, accurate, and helpful. Focus on customer satisfaction.\n\nContent\n---------\n{chunk}"
            )
            

            response = task.execute()
            responses.append(response)
        
        return '\n\n'.join(responses)
