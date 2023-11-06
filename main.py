import openai

openai.api_key = "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"

def get_reponse(user_prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_prompt,
        max_tokens=1000,
        temperature=0.5).choices[0].text
    return response


while True:
    decision = input("Please enter a prompt or q to exit: ")
    if decision != 'q':
        get_reponse(decision)
    else:
        break
