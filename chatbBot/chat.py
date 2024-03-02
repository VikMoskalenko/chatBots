import openai

API = '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'

openai.api_key = API

def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine='gpt-3.5-turbo-instruct', 
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None
    
res = generate_response('Hiya, how are you doing? What the weather now in Norwich?')
print(res)