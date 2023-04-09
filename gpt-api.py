import os
import openai
openai.organization = os.getenv("ORG_ID")
openai.api_key = os.getenv("API_KEY")
openai.Model.list()