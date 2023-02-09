import openai


openai.api_key = "<token>"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write simple aiogram bot in python that uses openai to answer",
  temperature=0,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.get("choices")[0].get("text"))
# print(response)