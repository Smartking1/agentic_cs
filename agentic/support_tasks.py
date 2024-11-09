from crewai import Task
from textwrap import dedent
from datetime import datetime

#embedding_tool = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")


class SupportTasks:

    def webscrape_task(self, agent, product_category, issue_type, customer_location):
        description = dedent(f"""
        I want you to act as a web scraper for Dell Technologies customer support.
        Your task is to scrape the given website URLs and extract the relevant customer support information.

        URLs:
        "https://www.dell.com/support/home/en-us",
        "https://www.dell.com/support/kbdoc/en-us/product-support",
        "https://www.dell.com/support/contents/en-us/category/Warranty",
        "https://www.dell.com/support/home/en-us/servicecontracts"
        
        Based on the URLs provided, extract the following information for {product_category} and {issue_type}:

        * For troubleshooting issues related to {issue_type}:
            - Problem description
            - Solution steps
            - Required tools or software
            - Estimated time for resolution
            - Warranty impact
            - Common user questions and solutions

        * For warranty and service contract information for customers in {customer_location}:
            - Warranty period and coverage
            - Service options
            - How to extend warranty
            - Warranty terms specific to {customer_location}
            - Contact information for service centers

        * For frequently asked questions (FAQs) for {product_category}:
            - Common issues and fixes
            - Product manuals and user guides
            - Software/firmware updates
            - Tips for optimizing performance
            - Preventive measures to avoid future issues

        Ensure that the scraped information is clear and organized, suitable for supporting agents to quickly provide solutions to customers.
        """)

        expected_output = dedent(f"""
            A well-structured report containing troubleshooting steps, warranty information, and FAQs for {product_category} and {issue_type}.
        """)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='dell_customer_support_task.md',
            callback=lambda output: display_output(output, title="Dell Technologies Customer Support Information")
        )

    def inquiry_resolution(self, customer, inquiry, person):
        description = dedent(f"""
        "{customer} just reached out with a super important ask:\n"
	    "{inquiry}\n\n"
        "{person} from {customer} is the one that reached out. "
		"Make sure to use everything you know "
        "to provide the best support possible."
		"You must strive to provide a complete "
        "and accurate response to the customer's inquiry."

        "Ensure that the best solution to the customer inquiry is being provided."
        """)

        expected_output=(f"""
	    "A detailed, informative response to the "
        "customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references "
        "to everything you used to find the answer, "
        "including external data or solutions. "
        "Ensure the answer is complete, "
		"leaving no questions unanswered, and maintain a helpful and friendly "
		"tone throughout."
        """)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='dell_customer_support_task2.md',
            callback=lambda output: display_output(output, title="Dell Technologies Customer Support Information")
        )

    def quaiity_assurance_review(self):
        description = dedent(f"""
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
		"high-quality standards expected for customer support.\n"
        "Verify that all parts of the customer's inquiry "
        "have been addressed "
		"thoroughly, with a helpful and friendly tone.\n"
        "Check for references and sources used to "
        " find the information, "
		"ensuring the response is well-supported and "
        "leaves no questions unanswered."
        """)

        expected_output = dedent(f"""
        "A final, detailed, and informative response "
        "ready to be sent to the customer.\n"
        "This response should fully address the "
        "customer's inquiry, incorporating all "
		"relevant feedback and improvements.\n"
		"Don't be too formal, we are a chill and cool company "
	    "but maintain a professional and friendly tone throughout."
        """)

        
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='dell_customer_support_task3.md',
            callback=lambda output: display_output(output, title="Dell Technologies Customer Support Information")
        )
    


    
    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000!"





