import os
import openai
from dotenv import load_dotenv, find_dotenv

# 读取本地环境变量

# find_dotenv()寻找并定位.env文件路径
# load_dotenv()读取.env文件，并将其中的环境变量加载到当前运行环境中
_ = load_dotenv(find_dotenv())

#获取环境变量 OPENAI_API_KEY
openai.api_key = os.environ['OPENAI_API_KEY']