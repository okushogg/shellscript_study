# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LINE_ACCESS = os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN")
LINE_SECRET = os.environ.get("YOUR_CHANNEL_SECRET")
GS_KEY = os.environ.get("SP_SHEET_KEY")