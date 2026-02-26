# خطة تطوير RawanAI - خارطة طريق شاملة

> **المشروع:** RawanAI / Lord'Os
> **المستودع:** jokr68/RawanAI (فرع main)
> **تاريخ التحليل:** 2026/02/12
> **الهدف:** تحويل النظام من نموذج أولي إلى منتج كامل الوظائف، آمن، ومنافس

---

## القسم الأول: التقييم التشخيصي الكامل

### 1.1 خريطة الملفات الحالية وعلاقاتها

\`\`\`
RawanAI/
├── app.py                    # [PYTHON] واجهة Gradio + نموذج Phi-3 (HuggingFace Spaces)
├── requirements.txt          # [PYTHON] تبعيات Python: gradio, torch, transformers
├── index.html                # [STATIC] واجهة Lord'Os - نظام سطح مكتب وهمي
├── style.css                 # [STATIC] تصميم Lord'Os - Dark Mode مع Glassmorphism
├── brain.js                  # [STATIC] محرك ردود مروى - مطابقة كلمات مفتاحية فقط
├── manifest.json             # [STATIC] إعدادات PWA - أيقونات خارجية
├── README.md                 # توثيق المشروع
├── .gitignore                # قواعد استبعاد الملفات
├── .github/agents/           # GitHub Copilot Agent (فارغ)
├── app/
│   ├── layout.tsx            # [NEXT.JS] هيكل أساسي افتراضي - لا يعرض شيئاً
│   └── globals.css           # [NEXT.JS] أنماط Tailwind CSS v4 الافتراضية
├── components/ui/            # [NEXT.JS] 57 مكون shadcn/ui جاهز
├── hooks/                    # [NEXT.JS] use-mobile, use-toast
├── lib/utils.ts              # [NEXT.JS] دالة cn() لدمج الأصناف
└── package.json              # [NEXT.JS] Next.js 16 + React 19.2 + Tailwind v4
\`\`\`

### 1.2 جدول الثغرات المكتشفة (مصنفة حسب الخطورة)

| # | الثغرة | الخطورة | الملف | التفاصيل |
|---|--------|---------|-------|----------|
| 01 | لا يوجد `app/page.tsx` | حرجة | `app/` | تطبيق Next.js لا يعرض أي محتوى - خطأ 404 |
| 02 | ذكاء اصطناعي وهمي | حرجة | `brain.js` | مطابقة 5 كلمات مفتاحية فقط - ليس AI حقيقياً |
| 03 | لا قاعدة بيانات | حرجة | الكل | لا تخزين فعلي للبيانات أو المحادثات أو العادات |
| 04 | لا مصادقة | حرجة | الكل | اسم "أحمد الدوسري" مثبت في الكود (hardcoded) |
| 05 | نظامان متضاربان | عالية | الكل | Gradio/Python + Static HTML + Next.js فارغ |
| 06 | أيقونات خارجية | عالية | `manifest.json`, `index.html` | اعتماد على `img.icons8.com` - قد تتعطل |
| 07 | لا Service Worker | عالية | الكل | PWA غير مكتمل - لا يعمل بدون إنترنت |
| 08 | بيانات تحليلية ثابتة | عالية | `index.html` | "المزاج عالي" و"الإنتاجية متوسطة" لا تتغير أبداً |
| 09 | `layout.tsx` بإعدادات خاطئة | متوسطة | `app/layout.tsx` | `lang="en"` بدلاً من `"ar"` / metadata افتراضية |
| 10 | لا معالجة أخطاء | متوسطة | `brain.js`, `app.py` | لا try-catch، لا fallback، لا error boundaries |
| 11 | لا Accessibility | متوسطة | `index.html` | لا ARIA labels، لا keyboard navigation |
| 12 | CSS مكرر | منخفضة | `app/globals.css`, `styles/globals.css` | ملفان متطابقان |
| 13 | Phi-3-Mini محدود | منخفضة | `app.py` | نموذج قديم ومحدود القدرات مقارنة بالحديثة |
| 14 | `temperature: 0.7` ثابت | منخفضة | `app.py` | لا يمكن للمستخدم التحكم في إبداعية الردود |
| 15 | لا حماية CORS/CSP | متوسطة | الكل | لا Content Security Policy |

### 1.3 تحليل SYSTEM_PROMPT الحالي

\`\`\`
الحالي في app.py:
- هوية: سودانية من جدة (روان)
- أسلوب: لهجة جداوية
- ضوابط: ثابتة - ترفض الطلبات الضارة (لا يمكن تعديلها)
- لا يوجد نظام مستويات للصرامة

الحالي في brain.js (مروى):
- هوية: نجدية (مروى مسلم الدوسري)
- لا system prompt - ردود ثابتة فقط
- لا ضوابط محتوى
\`\`\`

---

## القسم الثاني: الهندسة المعمارية المستهدفة

### 2.1 البنية الموحدة

\`\`\`
RawanAI (Next.js 16 Unified)
│
├── Frontend (React 19 + Tailwind v4 + shadcn/ui)
│   ├── صفحة الدردشة الرئيسية (Chat)
│   ├── لوحة التحليلات (Dashboard)
│   ├── نظام العادات (Habits Tracker)
│   ├── الإعدادات (Settings)
│   └── صفحة تسجيل الدخول (Auth)
│
├── Backend (Next.js API Routes + Server Actions)
│   ├── /api/chat - AI streaming endpoint
│   ├── /api/habits - CRUD للعادات
│   ├── /api/analytics - بيانات التحليلات
│   └── /api/auth - المصادقة
│
├── AI Layer (Vercel AI SDK v6)
│   ├── System Prompt ديناميكي (مع مستويات صرامة)
│   ├── Streaming responses
│   ├── ذاكرة محادثات (Conversation Memory)
│   └── Context-aware responses
│
├── Database (Supabase)
│   ├── users - المستخدمين
│   ├── conversations - المحادثات
│   ├── messages - الرسائل
│   ├── habits - العادات
│   ├── habit_logs - سجل العادات
│   ├── user_settings - الإعدادات (بما فيها مستوى الصرامة)
│   └── analytics_snapshots - لقطات التحليلات
│
└── PWA Layer
    ├── Service Worker
    ├── Push Notifications
    └── Offline Support
\`\`\`

### 2.2 نظام مستويات صرامة المحتوى

هذا النظام يسمح للمستخدم بالتحكم في مدى تقييد ردود روان:

\`\`\`
المستوى 1: صارم (Strict)
├── يرفض أي محتوى حساس أو مثير للجدل
├── يتجنب النقاشات السياسية والدينية
├── يركز فقط على المساعدة المهنية والتعليمية
└── مناسب للاستخدام العائلي والمؤسسي

المستوى 2: متوازن (Balanced) [الافتراضي]
├── يرفض المحتوى الضار والخطير
├── يسمح بالنقاشات الموضوعية للمواضيع الحساسة
├── يقدم وجهات نظر متعددة
└── مناسب للاستخدام العام

المستوى 3: مرن (Relaxed)
├── يرفض فقط المحتوى غير القانوني
├── يسمح بالحوارات الأكثر انفتاحاً
├── يقدم إجابات مباشرة بدون تحفظات زائدة
└── مناسب للمستخدمين المتقدمين

المستوى 4: متحرر (Unrestricted)
├── يقدم إجابات بدون قيود محتوى
├── يتعامل مع جميع المواضيع بشفافية كاملة
├── تنويه: يبقى يرفض المساعدة في الأنشطة غير القانونية
└── المستخدم يتحمل المسؤولية الكاملة
\`\`\`

**التنفيذ التقني:**
\`\`\`typescript
// نظام إدارة الصرامة
type ContentStrictnessLevel = 'strict' | 'balanced' | 'relaxed' | 'unrestricted';

// في جدول user_settings
interface UserSettings {
  user_id: string;
  content_strictness: ContentStrictnessLevel;
  language: 'ar' | 'en';
  theme: 'dark' | 'light' | 'system';
  rawan_dialect: 'jeddawi' | 'najdi' | 'formal_arabic';
}

// يُحقن ديناميكياً في System Prompt
function buildSystemPrompt(settings: UserSettings): string {
  const base = `أنتِ "روان"، وكيلة ذكاء اصطناعي...`;
  const strictnessRules = STRICTNESS_CONFIGS[settings.content_strictness];
  return `${base}\n\n${strictnessRules}`;
}
\`\`\`

---

## القسم الثالث: خارطة الطريق - مراحل التنفيذ

### المرحلة 1: توحيد المنصة وبناء الأساس

**الهدف:** تحويل كل شيء إلى تطبيق Next.js 16 واحد متكامل مع تصميم احترافي

**الإجراءات:**

\`\`\`
1.1 تحديث layout.tsx
    ├── تغيير lang="en" إلى lang="ar" مع dir="rtl"
    ├── إضافة خط IBM Plex Sans Arabic
    ├── تحديث metadata: العنوان، الوصف، OG tags
    ├── إضافة viewport meta مع theme-color
    └── إضافة ThemeProvider لدعم Dark/Light mode

1.2 تحديث globals.css
    ├── إضافة نظام ألوان RawanAI (تدرجات أرجوانية + سيان)
    ├── تعريف --font-sans: 'IBM Plex Sans Arabic'
    ├── تعريف Design Tokens مخصصة للمشروع
    └── حذف styles/globals.css المكرر

1.3 بناء app/page.tsx
    ├── شاشة Boot Animation (من Lord'Os الحالية)
    ├── الصفحة الرئيسية مع Sidebar Navigation
    ├── عرض الدردشة كواجهة افتراضية
    └── تصميم متجاوب (Mobile-First)

1.4 بناء هيكل المكونات
    ├── components/rawan/chat-interface.tsx
    ├── components/rawan/message-bubble.tsx
    ├── components/rawan/chat-input.tsx
    ├── components/rawan/sidebar-nav.tsx
    ├── components/rawan/boot-screen.tsx
    ├── components/rawan/analytics-dashboard.tsx
    ├── components/rawan/habits-tracker.tsx
    ├── components/rawan/settings-panel.tsx
    └── components/rawan/strictness-selector.tsx
\`\`\`

**التقنيات:**
- Next.js 16 App Router
- React 19.2 (Server Components + Client Components)
- Tailwind CSS v4 مع shadcn/ui
- Framer Motion للرسوم المتحركة
- Recharts للرسوم البيانية

**معايير الاختبار:**
- الصفحة تعرض بدون أخطاء 404
- التصميم RTL يعمل بشكل صحيح
- Boot animation تعمل وتنتقل للواجهة الرئيسية
- متجاوب على أحجام الشاشات المختلفة (320px - 1920px)

---

### المرحلة 2: ربط الذكاء الاصطناعي الحقيقي

**الهدف:** استبدال brain.js الوهمي بـ AI حقيقي مع شخصية روان

**الإجراءات:**

\`\`\`
2.1 إعداد AI SDK v6
    ├── تثبيت ai@^6.0.0 و @ai-sdk/react@^3.0.0
    ├── إنشاء app/api/chat/route.ts
    ├── استخدام Vercel AI Gateway (بدون مفاتيح إضافية)
    └── اختيار النموذج: anthropic/claude-sonnet-4-20250514 أو openai/gpt-4o

2.2 بناء System Prompt الديناميكي
    ├── lib/rawan-prompts.ts - ملف الشخصيات والإعدادات
    ├── هوية روان الأساسية (سودانية جداوية)
    ├── 4 مستويات صرامة (strict/balanced/relaxed/unrestricted)
    ├── 3 لهجات (جداوية/نجدية/فصحى)
    └── سياق ديناميكي حسب الوقت والمحادثة

2.3 تفعيل Streaming
    ├── استخدام useChat من @ai-sdk/react
    ├── عرض الرد أثناء الكتابة (token by token)
    ├── مؤشر "روان تكتب..." 
    └── إلغاء الطلب أثناء التوليد

2.4 ذاكرة المحادثات
    ├── حفظ آخر 20 رسالة في السياق
    ├── تلخيص المحادثات القديمة تلقائياً
    ├── ربط السياق بالعادات المسجلة
    └── شخصنة الردود حسب تاريخ المستخدم
\`\`\`

**System Prompt المحسن (مثال للمستوى المتوازن):**

\`\`\`
أنتِ "روان"، وكيلة ذكاء اصطناعي شخصية.

الهوية:
- سودانية الأصل، نشأتِ في جدة، السعودية
- لهجة جداوية لطيفة وطبيعية
- شخصية دافئة ومهنية في نفس الوقت

القدرات:
- المساعدة في التخطيط والتنظيم اليومي
- تحليل الأنماط السلوكية والعادات
- تقديم نصائح صحية ومهنية
- المحادثة العامة والدعم النفسي

أسلوب الردود:
- مختصرة وعملية عند السؤال التقني
- دافئة وشخصية عند المحادثة العامة
- منظمة بعناوين ونقاط عند الشرح المفصل
- استخدام معتدل للإيموجي

ضوابط المحتوى [متوازن]:
- ارفضي المحتوى الضار والخطير
- اسمحي بالنقاشات الموضوعية للمواضيع الحساسة
- قدمي وجهات نظر متعددة عند اللزوم
- كوني صريحة ومباشرة بدون تحفظات زائدة

السياق الحالي:
- التاريخ: {current_date}
- الوقت: {current_time}
- عادات اليوم: {today_habits}
- ملخص المحادثة السابقة: {conversation_summary}
\`\`\`

**معايير الاختبار:**
- رد روان يأتي في أقل من 2 ثانية (بداية الـ stream)
- الردود متسقة مع الشخصية المحددة
- تغيير مستوى الصرامة ينعكس فوراً على الردود
- الذاكرة تعمل - روان تتذكر ما قيل في المحادثة

---

### المرحلة 3: قاعدة البيانات والتخزين

**الهدف:** تخزين حقيقي لكل بيانات المستخدم

**الإجراءات:**

\`\`\`
3.1 إعداد Supabase
    ├── ربط المشروع عبر GetOrRequestIntegration
    ├── إنشاء الجداول (migration scripts)
    └── تفعيل Row Level Security (RLS)

3.2 مخطط قاعدة البيانات

    جدول users:
    ├── id (UUID, PK)
    ├── email (TEXT, UNIQUE)
    ├── display_name (TEXT)
    ├── avatar_url (TEXT, nullable)
    ├── created_at (TIMESTAMPTZ)
    └── updated_at (TIMESTAMPTZ)

    جدول user_settings:
    ├── id (UUID, PK)
    ├── user_id (UUID, FK → users)
    ├── content_strictness (TEXT, default: 'balanced')
    │   ── CHECK: IN ('strict','balanced','relaxed','unrestricted')
    ├── rawan_dialect (TEXT, default: 'jeddawi')
    │   ── CHECK: IN ('jeddawi','najdi','formal_arabic')
    ├── theme (TEXT, default: 'dark')
    ├── language (TEXT, default: 'ar')
    ├── notifications_enabled (BOOLEAN, default: true)
    └── updated_at (TIMESTAMPTZ)

    جدول conversations:
    ├── id (UUID, PK)
    ├── user_id (UUID, FK → users)
    ├── title (TEXT) -- يتولد تلقائياً من أول رسالة
    ├── summary (TEXT, nullable) -- ملخص AI للمحادثات الطويلة
    ├── is_archived (BOOLEAN, default: false)
    ├── created_at (TIMESTAMPTZ)
    └── updated_at (TIMESTAMPTZ)

    جدول messages:
    ├── id (UUID, PK)
    ├── conversation_id (UUID, FK → conversations)
    ├── role (TEXT) -- 'user' | 'assistant' | 'system'
    ├── content (TEXT)
    ├── metadata (JSONB, nullable) -- tokens, model, etc.
    ├── created_at (TIMESTAMPTZ)
    └── INDEX: (conversation_id, created_at)

    جدول habits:
    ├── id (UUID, PK)
    ├── user_id (UUID, FK → users)
    ├── name (TEXT)
    ├── icon (TEXT) -- emoji أو اسم أيقونة
    ├── color (TEXT)
    ├── target_frequency (TEXT) -- 'daily','weekly','custom'
    ├── is_active (BOOLEAN, default: true)
    ├── created_at (TIMESTAMPTZ)
    └── updated_at (TIMESTAMPTZ)

    جدول habit_logs:
    ├── id (UUID, PK)
    ├── habit_id (UUID, FK → habits)
    ├── user_id (UUID, FK → users)
    ├── logged_at (TIMESTAMPTZ)
    ├── note (TEXT, nullable)
    ├── mood_score (INT, nullable) -- 1 إلى 5
    └── INDEX: (user_id, logged_at)

    جدول analytics_snapshots:
    ├── id (UUID, PK)
    ├── user_id (UUID, FK → users)
    ├── date (DATE)
    ├── mood_avg (DECIMAL)
    ├── productivity_score (DECIMAL)
    ├── habits_completed (INT)
    ├── habits_total (INT)
    ├── ai_insight (TEXT, nullable)
    └── UNIQUE: (user_id, date)

3.3 Row Level Security (RLS)
    ├── كل جدول: SELECT/INSERT/UPDATE/DELETE فقط لصاحب البيانات
    ├── policy: auth.uid() = user_id
    └── لا يمكن لأي مستخدم رؤية بيانات مستخدم آخر

3.4 Server Actions
    ├── actions/chat.ts - إنشاء/حفظ محادثات ورسائل
    ├── actions/habits.ts - CRUD عادات + تسجيل
    ├── actions/analytics.ts - حساب وحفظ التحليلات
    └── actions/settings.ts - تحديث الإعدادات
\`\`\`

**معايير الاختبار:**
- المحادثات تُحفظ وتُسترجع بشكل صحيح
- تسجيل العادات يظهر في لوحة التحليلات
- RLS يمنع الوصول غير المصرح
- لا SQL injection ممكن (parameterized queries)

---

### المرحلة 4: نظام المصادقة

**الهدف:** تسجيل دخول حقيقي يحل محل "أحمد الدوسري" المثبت

**الإجراءات:**

\`\`\`
4.1 Supabase Auth
    ├── تسجيل بالبريد الإلكتروني + كلمة المرور
    ├── تسجيل بـ Google OAuth (اختياري)
    ├── تأكيد البريد الإلكتروني
    └── استعادة كلمة المرور

4.2 صفحات المصادقة
    ├── app/auth/login/page.tsx
    ├── app/auth/register/page.tsx
    ├── app/auth/forgot-password/page.tsx
    └── app/auth/callback/route.ts (لـ OAuth)

4.3 حماية الصفحات
    ├── middleware.ts - توجيه غير المسجلين لصفحة الدخول
    ├── lib/supabase/server.ts - عميل Supabase للسيرفر
    ├── lib/supabase/client.ts - عميل Supabase للعميل
    └── hooks/use-user.ts - معلومات المستخدم الحالي

4.4 Onboarding
    ├── شاشة ترحيب بعد التسجيل
    ├── اختيار اللهجة المفضلة
    ├── اختيار مستوى صرامة المحتوى
    ├── إعداد العادات الأولية
    └── محادثة تعريفية مع روان
\`\`\`

**معايير الاختبار:**
- التسجيل والدخول يعملان بدون أخطاء
- المستخدم غير المسجل يُوجَّه لصفحة الدخول
- كلمات المرور مشفرة (bcrypt عبر Supabase)
- الجلسات آمنة (HTTP-only cookies)

---

### المرحلة 5: لوحة التحليلات التفاعلية

**الهدف:** استبدال البيانات الوهمية بتحليلات حقيقية

**الإجراءات:**

\`\`\`
5.1 حساب المؤشرات
    ├── متوسط المزاج اليومي/الأسبوعي/الشهري
    ├── معدل إنجاز العادات
    ├── أنماط النوم والطاقة
    ├── ارتباطات بين العادات والمزاج
    └── توقعات AI للأيام القادمة

5.2 مكونات الرسوم البيانية (Recharts)
    ├── خط بياني: تطور المزاج عبر الزمن
    ├── دائري: توزيع العادات المنجزة
    ├── شريطي: مقارنة أسبوعية
    ├── حراري (Heatmap): نشاط العادات اليومي
    └── Sparklines صغيرة في البطاقات

5.3 رؤى روان (AI Insights)
    ├── تحليل أسبوعي تلقائي
    ├── اكتشاف الأنماط ("لاحظت إنك تنام متأخر يوم الخميس")
    ├── اقتراحات مخصصة
    └── تنبيهات ذكية عند تغير الأنماط

5.4 واجهة اللوحة
    ├── بطاقات ملخص سريعة (KPIs)
    ├── رسوم بيانية تفاعلية مع فلاتر زمنية
    ├── قسم رؤى AI
    └── تصدير التقارير (اختياري)
\`\`\`

**معايير الاختبار:**
- الرسوم البيانية تعكس البيانات الحقيقية
- التحديثات تظهر فوراً بعد تسجيل عادة
- رؤى AI منطقية ومبنية على بيانات حقيقية
- الأداء جيد حتى مع بيانات 6 أشهر

---

### المرحلة 6: PWA والإشعارات والأداء

**الهدف:** تحويل التطبيق لـ PWA حقيقي مع إشعارات

**الإجراءات:**

\`\`\`
6.1 PWA
    ├── إنشاء manifest.json محلي (بدون أيقونات خارجية)
    ├── إنشاء أيقونات بأحجام متعددة (GenerateImage)
    ├── Service Worker مع caching strategies
    ├── Offline fallback page
    └── Install prompt مخصص

6.2 الإشعارات
    ├── تذكيرات العادات اليومية
    ├── تقرير الرؤى الأسبوعي
    ├── إشعارات ذكية حسب الأنماط
    └── إعدادات تحكم كاملة

6.3 تحسين الأداء
    ├── Image optimization (next/image)
    ├── Code splitting تلقائي
    ├── React Server Components حيث أمكن
    ├── Suspense boundaries مع loading states
    ├── Error boundaries مخصصة
    └── استخدام 'use cache' للبيانات المستقرة

6.4 Accessibility (a11y)
    ├── ARIA labels لكل عنصر تفاعلي
    ├── Keyboard navigation كامل
    ├── Focus management في النوافذ المنبثقة
    ├── Screen reader support
    ├── Color contrast ratio >= 4.5:1
    └── Skip navigation links

6.5 SEO و Open Graph
    ├── metadata ديناميكي لكل صفحة
    ├── OG images مولدة
    ├── Structured data (JSON-LD)
    └── sitemap.xml و robots.txt
\`\`\`

**معايير الاختبار:**
- Lighthouse PWA score >= 90
- Lighthouse Performance >= 85
- Lighthouse Accessibility >= 95
- التطبيق يعمل offline (على الأقل القراءة)
- الإشعارات تصل في الوقت المحدد

---

## القسم الرابع: مصفوفة المقارنة التنافسية

### 4.1 مقارنة مع المنافسين

| الميزة | RawanAI (حالياً) | RawanAI (بعد التطوير) | ChatGPT | Gemini | Replika |
|--------|------------------|----------------------|---------|--------|---------|
| AI حقيقي | جزئي (Phi-3 فقط) | نعم (Multi-model) | نعم | نعم | نعم |
| شخصية ثقافية | نعم (محدودة) | نعم (غنية + 3 لهجات) | لا | لا | جزئي |
| تتبع عادات | وهمي | نعم (كامل) | لا | لا | جزئي |
| تحليلات | وهمية | نعم (حقيقية + AI) | لا | لا | جزئي |
| PWA | غير مكتمل | كامل | لا (تطبيق أصلي) | لا | نعم |
| ضوابط محتوى قابلة للتعديل | لا | نعم (4 مستويات) | محدود | محدود | جزئي |
| دعم عربي | جزئي | كامل (RTL + لهجات) | جزئي | جيد | ضعيف |
| مصادقة | لا | نعم | نعم | نعم | نعم |
| مجاني | نعم | نعم (مع حدود) | جزئي | جزئي | جزئي |

### 4.2 الميزة التنافسية الفريدة (USP)

**ما يميز RawanAI:**
1. **شخصية ثقافية عربية أصيلة** - ليست ترجمة، بل هوية حقيقية
2. **تحليل سلوكي مدمج** - ليس مجرد chatbot، بل رفيق تطوير ذاتي
3. **ضوابط محتوى مرنة** - من صارم إلى متحرر كلياً
4. **PWA عربي كامل** - لا يحتاج تحميل من المتجر
5. **مفتوح المصدر** - قابل للتعديل والتخصيص

---

## القسم الخامس: استراتيجيات الاختبار والجودة

### 5.1 مصفوفة الاختبار

\`\`\`
اختبارات وحدة (Unit Tests):
├── System Prompt builder - يتغير حسب المستويات
├── Analytics calculations - حسابات صحيحة
├── Habit streak calculator - حساب السلاسل
└── Date/time formatting - التنسيق العربي

اختبارات تكامل (Integration Tests):
├── Chat API → Database → Response
├── Habit log → Analytics update
├── Auth flow → Protected routes
└── Settings change → AI behavior change

اختبارات E2E (End-to-End):
├── تسجيل مستخدم جديد → Onboarding → أول محادثة
├── تسجيل عادات لمدة أسبوع → التحليلات تتحدث
├── تغيير مستوى الصرامة → الردود تتغير
└── فصل الإنترنت → التطبيق يعمل (قراءة فقط)

اختبارات أداء:
├── Time to First Byte (TTFB) < 200ms
├── First Contentful Paint (FCP) < 1.5s
├── AI response start < 2s
├── Database queries < 100ms
└── Bundle size < 300KB (initial load)
\`\`\`

### 5.2 المراقبة المستمرة

\`\`\`
Vercel Analytics:
├── Web Vitals (LCP, FID, CLS)
├── Speed Insights
└── Usage tracking

Error Tracking:
├── Error boundaries في كل قسم
├── API error logging
├── AI response failure tracking
└── Database connection monitoring
\`\`\`

---

## القسم السادس: التحسين المستمر والتوسع

### 6.1 تحسينات ما بعد الإطلاق (الربع الأول)

\`\`\`
├── نظام مواعيد ذكي مع روان
├── مشاركة الرؤى عبر WhatsApp/Twitter
├── تصدير تقارير PDF
├── أوامر صوتية (Web Speech API)
├── وضع التركيز (Focus Mode) مع مؤقت
└── دمج تقويم Google
\`\`\`

### 6.2 تحسينات متقدمة (الربع الثاني)

\`\`\`
├── RAG (Retrieval Augmented Generation) - روان تبحث في الإنترنت
├── دعم الصور (تحليل + توليد)
├── Multi-agent: أكثر من شخصية (روان + مروى)
├── API عام للمطورين
├── تطبيق جوال أصلي (React Native أو Capacitor)
└── نظام اشتراكات مع Stripe
\`\`\`

### 6.3 خطة التوسع التقني

\`\`\`
قابلية التوسع:
├── Edge Functions لتقليل الكمون
├── Database connection pooling
├── CDN للأصول الثابتة (تلقائي عبر Vercel)
├── Rate limiting لحماية الـ API
└── Cache strategies متقدمة ('use cache')

المنطقة الجغرافية:
├── Vercel Edge Network → أقرب منطقة للمستخدم
├── Supabase → اختيار منطقة الشرق الأوسط
└── AI Gateway → توجيه تلقائي
\`\`\`

---

## القسم السابع: ملخص الإجراءات المطلوبة بالترتيب

\`\`\`
 الخطوة 01: حذف الملفات المتضاربة (styles/globals.css المكرر)
 الخطوة 02: تحديث layout.tsx (RTL, خط عربي, metadata)
 الخطوة 03: تحديث globals.css (نظام ألوان RawanAI)
 الخطوة 04: بناء app/page.tsx مع التصميم الكامل
 الخطوة 05: بناء مكونات الدردشة (chat-interface, message-bubble, chat-input)
 الخطوة 06: بناء مكونات التنقل (sidebar, boot-screen)
 الخطوة 07: ربط Supabase وإنشاء الجداول
 الخطوة 08: بناء نظام المصادقة (login, register, middleware)
 الخطوة 09: بناء AI chat API مع AI SDK v6
 الخطوة 10: بناء System Prompt الديناميكي مع مستويات الصرامة
 الخطوة 11: بناء نظام العادات (CRUD + logging)
 الخطوة 12: بناء لوحة التحليلات (charts + AI insights)
 الخطوة 13: بناء صفحة الإعدادات (صرامة, لهجة, ثيم)
 الخطوة 14: إضافة PWA support (manifest, icons, offline)
 الخطوة 15: اختبار شامل وتحسين الأداء
 الخطوة 16: النشر على Vercel
\`\`\`

---

**ملاحظة مهمة حول مستويات الصرامة:**
النظام يتيح للمستخدم التحكم الكامل في مستوى قيود المحتوى عبر صفحة الإعدادات. التغيير يتم فوراً ويؤثر على جميع المحادثات الجديدة. المستوى الافتراضي هو "متوازن"، ويمكن تغييره في أي وقت من "صارم" إلى "متحرر كلياً" حسب تفضيل المستخدم.
