from openai import OpenAI
import json
import os
import requests
import wikipedia

wikipedia.API_URL = "https://en.wikipedia.org/w/api.php"
wikipedia.wikipedia.headers = {
    "User-Agent": "SimpleAgentProject/1.0 (test@example.com)"
}

os.environ["NO_PROXY"] = "localhost,127.0.0.1"

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"خطا: {e}"



def wikipedia_search(query: str) -> str:
    headers = {"User-Agent": "SimpleAgentProject/1.0 (test@example.com)"}

    for lang in ["en", "fa"]:
        url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                extract = data.get("extract")
                if extract:
                    return extract
        except Exception as e:
            continue

    return "چیزی با این عنوان در ویکی‌پدیا پیدا نشد."

def translate_to_persian(text: str) -> str:
    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": (
                    "فقط متن زیر رو کلمه‌به‌کلمه به فارسی روان ترجمه کن. "
                    "هیچ جمله‌ی اضافه، نظر شخصی، یا پیشنهادی به متن اضافه نکن. "
                    "فقط و فقط ترجمه‌ی دقیق همین متن رو بنویس:\n\n"
                    f"{text}"
                )
            }
        ],
        temperature=0.3,  # کاهش خلاقیت مدل برای کاهش توهم/اضافه‌گویی
    )
    return response.choices[0].message.content

SYSTEM_PROMPT = (
    "تو یک ایجنت هستی که به دو ابزار دسترسی داری:\n\n"
    "۱. calculator — برای محاسبات ریاضی\n"
    'فرمت: {"tool": "calculator", "expression": "عبارت ریاضی"}\n\n'
    "۲. wikipedia_search — برای جستجوی اطلاعات عمومی درباره‌ی افراد، مکان‌ها، مفاهیم و غیره\n"
    'فرمت: {"tool": "wikipedia_search", "query": "نام موضوع به زبان انگلیسی"}\n\n'
    "توجه: مقدار query همیشه باید به انگلیسی و با حروف لاتین نوشته بشه (مثلاً Albert Einstein نه آلبرت اینشتین).\n\n"
    "اگه سوال نیاز به یکی از این ابزارها داره، فقط JSON مربوطه رو برگردون و هیچ متن اضافه‌ای ننویس.\n"
    "اگه نیازی به ابزار نیست، عادی و به فارسی جواب بده."
)

def ask_agent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model="llama3.1:8b",
        messages=messages,
    )
    content = response.choices[0].message.content

    try:
        parsed = json.loads(content)
        tool = parsed.get("tool")

        if tool == "calculator":
            expression = parsed["expression"]
            result = calculator(expression)
            return f"حاصل {expression} برابر است با {result}"

        elif tool == "wikipedia_search":
            query = parsed["query"]
            result = wikipedia_search(query)
            translated = translate_to_persian(result)
            return translated

        else:
            return content

    except json.JSONDecodeError:
        return content


# تست
print(ask_agent("حاصل 234 ضرب در 17 چقدره؟"))
print(ask_agent("آلبرت اینشتین کیه؟"))
print(ask_agent("سلام، حالت چطوره؟"))