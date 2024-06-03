import os
import openai
#from dotenv import load_dotenv
#load_dotenv()
deployment_name = "test-gpt-jay"
openai.api_type = "azure"
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key ="Your key"
#openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_base = "Endpoint Url"
openai.api_version = "Latest version of Azure OpenAI service"
print(os.getenv("OPENAI_API_KEY"))
prompt =(
    "Explain what the below SQL query does. Also answer why someone might be interested in this time period, "
    "and why a company might be interested in this SQL query:\n"
    "SELECT c.customer_id\n"
    "FROM Customers c\n"
    "JOIN Streaming s\n"
    "ON c.customer_id = s.customer_id\n"
    "WHERE c.signup_date BETWEEN '2020-03-01' AND '2020-03-31'\n"
    "AND s.watch_date BETWEEN c.signup_date AND DATE_ADD(c.signup_date, INTERVAL 30 DAY)\n"
    "GROUP BY c.customer_id\n"
    "HAVING SUM(s.watch_minutes) > 50 * 60"
)
result = openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    deployment_id=deployment_name
)
result.choices[0].text.strip(" \n")
print(result)
