import requests
import json


def translate(text: str) -> str:
    r = requests.post(
        "http://www.scotranslate.com/Translation/Translate",
        headers={"Content-Type": "application/json; charset=utf-8"},
        data=json.dumps(
            {
                'InputString': text,
                'RegionId': '1007',
                'SourceId': '11'
            }
        )
    ).content.decode()
    return json.loads(r)['Translation']
