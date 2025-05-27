# # -*- coding: utf-8 -*-

import json
from openai import OpenAI
from pydantic import BaseModel
from accounts.models import User

# user = User.objects.all(user_pk)로 query
# user.age
# model 여기서 쓰려면 django 설정해야함
# user = User.objects.all()
# OpenAI API Key 가져오기
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

user_prompt = "한국 사람들이 좋아하는 과일은 사과, 배, 귤, 포도, 수박, 참외, 딸기, 감, 복숭아 같은 것들이 있어요. 계절마다 선호하는 과일이 좀 다른데, 여름엔 수박이나 참외를 많이 먹고, 겨울엔 귤이 인기 많죠. 딸기는 봄철에 특히 많이 찾고, 가을엔 감이나 배를 많이 먹어요. 포도도 여름에서 가을 사이에 인기가 많고, 복숭아도 달콤하고 부드러워서 좋아하는 사람이 많아요. - 출처 : 00뉴스"

# 공식문서 붙여넣기
# response = client.responses.create(
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    # {
    #   "role": "system",
    #   "content": [
    #     {
    #       "type": "input_text",
    #       "text": "You will be provided with unstructured data, and your task is to parse it into CSV format."
    #     }
    #   ]
    # },
    {
      "role": "system",
    #   "content": "You will be provided with unstructured data, and your task is to parse it into CSV format."
      "content": "당신은 구조화 되지 않은 데이터를 CSV 형식으로 변환하는 AI입니다. 사용자가 과일에 대한 설명을 제공하면, 과일 이름만 CSV 형식으로 추출하세요."
    },

    # {
    #   "role": "user",
    #   "content": [
    #     {
    #       "type": "input_text",
    #       "text": "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
    #     }
    #   ]
    # }
    {
      "role": "user",
    #   "content": "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
      "content": user_prompt
    }
  ],
  temperature=1,
#   max_output_tokens=256
  max_tokens=256
)

# print(response.output_text)
print(response.choices[0].message.content)



