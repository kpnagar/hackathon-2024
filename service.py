import requests

async def ask_ai(text_body: str):
    data = {
        "question": text_body,
        "context": [[]],
        "index": "HSE",
        "SourceLanguageCode": "auto",
        "TargetLanguageCode": "en",
    }
    try:
        url = "https://dev-chat-service-apis.dev.infra.navatechgroup.com/generateresponse"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        print(response)
        response.raise_for_status()
        response = response.json()
        return response
    except requests.HTTPError as e:
        raise Exception("Error from bot")
    except Exception as e:
        raise Exception("Error in chatbot")
