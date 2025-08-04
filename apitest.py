from config.api_key_enum import API_KEY_ENUM
from config.openai_key import get_openai_key

print(API_KEY_ENUM.OPEN_AI.value)

print(get_openai_key(API_KEY_ENUM.OPEN_AI.value))