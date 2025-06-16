import openai
from dotenv import load_dotenv

load_dotenv()

openai_client = openai.OpenAI()

def generate_blog(paragraph_topic):
    response = openai_client.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt='Write a Paragraph About the Following Topic: ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].text

keep_writing = True

while keep_writing:
    answer = input('Write a Paragraph? Y for yes, Anything else for no. ')
    if answer.upper() == 'Y':
        paragraph_topic = input('What Should this Paragraph talk About? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
