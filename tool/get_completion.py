from openai import OpenAI
from config.api_key_enum import API_KEY_ENUM
from config.openai_key import get_openai_key


def get_completion(prompt, base_url, model):
    try:
        # 获取apikey
        api_key = get_openai_key(API_KEY_ENUM.DEEPSEEK.value)
        # 链接模型
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                }
            ]
        )
        return response
    except Exception as e:
        print(e)


if __name__ == '__main__':
    res = get_completion("你好", "https://api.deepseek.com", "deepseek-chat")
    print(res)
