import openai
import sys

sys.stdout = open("output.txt", "w")

openai.api_key = open("key.txt").read().strip("\n")

openai.ChatCompletion().create()