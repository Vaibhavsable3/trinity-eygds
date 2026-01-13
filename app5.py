import google.generativeai as genai
genai.configure(api_key="AIzaSyB09Zf92WgBYckYL4O7aNfjQ3Jq8Uc1n7o")
for m in genai.list_models():
    print(m.name)