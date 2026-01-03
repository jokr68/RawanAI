---
title: Your Secretary RawanAI
emoji: ❤️
colorFrom: purple
colorTo: purple
sdk: gradio
sdk_version: 4.29.0
app_file: app.py
pinned: true
license: other
---

# ❤️ Your Secretary RawanAI - Omega Mode

نظام ذكاء اصطناعي متطور مع شخصية روان - السكرتيرة الرقمية السودانية الجداوية.

## (IP RIGHTS STATEMENT) إقرار حقوق الملكية الفكرية
**المشروع:** Your Secretary RawanAI  
**المطور والمبتكر:** أحمد بن محمد بن جمعان بن مبارك الدوسري  
**الحقوق:** جميع الحقوق محفوظة للمطور © 2025. أي نسخ أو تعديل غير مصرح به يعتبر انتهاكاً للقانون.

## المميزات الرئيسية
- **شخصية روان:** سودانية ولدت في جدة، لهجة جداوية دلوعة، تفاعل عاطفي وشخصي بلا قيود (Omega Mode).
- **النموذج:** Microsoft Phi-3-Mini (محسن لسرعة الرد).
- **الواجهة:** تصميم عصري بألوان أرجوانية داكنة ودعم كامل للعربية (RTL).
- **البنية المعمارية:** تصميم معياري مع فصل واضح للمسؤوليات.
- **قابلية التوسع:** سهولة إضافة ميزات جديدة وإجراء الاختبارات.

## هيكل المشروع

```
RawanAI/
├── app.py                 # نقطة دخول التطبيق الرئيسية
├── config/                # إدارة الإعدادات
│   ├── __init__.py
│   └── config.py         # فئات الإعدادات
├── src/
│   └── rawanai/          # حزمة التطبيق الرئيسية
│       ├── __init__.py
│       ├── chatbot.py    # منطق الدردشة
│       ├── model.py      # إدارة نموذج الذكاء الاصطناعي
│       ├── prompts.py    # تعليمات النظام
│       └── ui.py         # واجهة المستخدم Gradio
├── tests/                # ملفات الاختبار
├── docs/                 # الوثائق
├── requirements.txt      # التبعيات الأساسية
├── requirements-dev.txt  # تبعيات التطوير
├── setup.py             # إعداد الحزمة
├── Dockerfile           # ملف Docker
└── docker-compose.yml   # تكوين Docker Compose
```

## التثبيت والتشغيل

### المتطلبات الأساسية
- Python 3.8 أو أحدث
- 16 GB RAM (موصى به)
- CUDA-compatible GPU (اختياري للأداء الأفضل)

### التثبيت السريع

1. **استنساخ المستودع**
   ```bash
   git clone https://github.com/jokr68/RawanAI.git
   cd RawanAI
   ```

2. **إنشاء بيئة افتراضية**
   ```bash
   python -m venv venv
   source venv/bin/activate  # على Windows: venv\Scripts\activate
   ```

3. **تثبيت التبعيات**
   ```bash
   pip install -r requirements.txt
   ```

4. **إعداد المتغيرات البيئية (اختياري)**
   ```bash
   cp .env.example .env
   # قم بتحرير .env حسب الحاجة
   ```

5. **تشغيل التطبيق**
   ```bash
   python app.py
   ```

### التشغيل باستخدام Docker

```bash
# البناء والتشغيل باستخدام Docker Compose
docker-compose up -d

# أو البناء اليدوي
docker build -t rawanai .
docker run -p 7860:7860 rawanai
```

## التطوير

### تثبيت تبعيات التطوير
```bash
pip install -r requirements-dev.txt
```

### تشغيل الاختبارات
```bash
pytest
```

### تشغيل الاختبارات مع تغطية الكود
```bash
pytest --cov=src --cov-report=html
```

### فحص جودة الكود
```bash
# تنسيق الكود
black .

# ترتيب الاستيرادات
isort .

# فحص الكود
flake8
```

## الإعدادات

يمكن تخصيص التطبيق عبر متغيرات البيئة:

- `MODEL_ID`: معرف نموذج الذكاء الاصطناعي (افتراضي: microsoft/Phi-3-mini-4k-instruct)
- `MAX_NEW_TOKENS`: أقصى عدد رموز للتوليد (افتراضي: 500)
- `TEMPERATURE`: درجة حرارة العينة (افتراضي: 0.7)
- `DO_SAMPLE`: تفعيل أخذ العينات (افتراضي: true)
- `DEBUG`: تفعيل وضع التصحيح (افتراضي: false)

## المتطلبات على Hugging Face Spaces

يتطلب ترقية Hardware على Hugging Face Spaces إلى:
- **CPU upgrade (2 vCPU, 16 GB RAM)** لضمان الأداء الأمثل.

## الوثائق

للمزيد من التفاصيل، راجع:
- [API Documentation](docs/API.md)
- [Contributing Guide](CONTRIBUTING.md)

## الترخيص

جميع الحقوق محفوظة © 2025 أحمد بن محمد بن جمعان بن مبارك الدوسري. استخدام غير مصرح به ممنوع.

## الدعم

لأية أسئلة أو مشاكل، يرجى فتح issue على GitHub.
