import os
from anthropic import Anthropic

# قراءة المفتاح من متغيرات البيئة
api_key = os.environ.get("ANTHROPIC_API_KEY")

if not api_key:
    print("خطأ: لم يتم العثور على مفتاح API.")
    exit(1)

# تهيئة العميل
client = Anthropic(api_key=api_key)

# قائمة الرسائل (تاريخ المحادثة)
messages = [
    {"role": "user", "content": "مرحباً! ما هو دوري أبطال أوروبا؟"}
]

try:
    # إرسال الطلب إلى Claude
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",  # يمكنك تغيير الموديل حسب رصيدك
        max_tokens=1024,
        messages=messages
    )
    
    # طباعة رد Claude
    print("Claude:", response.content[0].text)

except Exception as e:
    print(f"حدث خطأ: {e}")
