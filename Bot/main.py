import openai
from livechat.agent.rtm.base import AgentRTM
import config
import asyncio
import json


async def get_GPT_response(text: str) -> str:
	openai.api_key = config.OPENAI_APIKEY

	print(text)

	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=text,
		temperature=0,
		max_tokens=200,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)

	return response.get("choices")[0].get("text")


async def get_chats():
	token = config.LIVECHAT_TOKEN
	agent_rtm = AgentRTM.get_client()
	agent_rtm.open_connection()
	agent_rtm.login(token=token)
	response = agent_rtm.list_chats()
	agent_rtm.close_connection()

	return response.payload.get("chats_summary")


async def send_to_LiveChat(chat_id: str, message: str):
	token = config.LIVECHAT_TOKEN
	agent_rtm = AgentRTM.get_client()
	agent_rtm.open_connection()
	agent_rtm.login(token=token)

	agent_rtm.send_event(
		chat_id=chat_id, 
		event={'type': 'message','text': message, 'visibility': 'all'})

	return agent_rtm.close_connection()



async def main():
	a = await get_chats()
	# # with open("data.json", "w") as f:
	# # 	json.dump(a, f, indent=4)

	# for i in a:

	# # 		print(i.get("id"))
	# # 		try:
	# #	 		print(i.get("last_event_per_type").get("message").get("event").get("text"))
	# #	 	except:
	# #	 		pass

	# 	if i.get("id") == "RP0TEH3068":
	# 		print("done 1")
	# 		with open("data.json", "w") as f:
	# 			json.dump(i, f, indent=4)

	with open("data.json", "w") as f:
		json.dump(a, f, indent=4)

	while True:
		temp = ""
		a = await get_chats()
		print("fetched")
		for i in a:
			try:
				if (d := i.get("last_event_per_type").get("filled_form").get("event").get("properties").get("source").get("client_id")) == (c := i.get("last_event_per_type").get("message").get("event").get("properties").get("source").get("client_id")):
					print(f"APPROVED DONE id: {i.get('id')}", d, c)
					text = i.get("last_event_per_type").get("message").get("event").get("text")
					chat_id = i.get("id")
					response = await get_GPT_response(text)
					print(":" + response + ":")
					await send_to_LiveChat(chat_id, response)
					print(f"APPROVED DONE ENDED id: {i.get('id')}", d, c)
				print(f"DONE id: {i.get('id')}", d, c)
			except:
				print(f"ERROR.  id: {i.get('id')}")
				pass

		await asyncio.sleep(5)
		# break



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	loop.close()
