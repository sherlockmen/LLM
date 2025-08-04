import os
from dotenv import load_dotenv, find_dotenv


# 暴露一个函数 可以直接获得当前模型的api key
def get_openai_key(keyname):
    _ = load_dotenv(find_dotenv())
    return os.environ[keyname]
