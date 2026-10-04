# 🏰 Arab Albion Discord Bot

بوت ديسكورد متكامل ومصمم خصيصاً لمجتمعات وكلانات لعبة **Albion Online** باللغة العربية، مبني باستخدام **Python 3.13** ومكتبة **Discord.py v2**.

---

## ✨ المميزات الرئيسية (Features)

1. **🔗 تسجيل اللاعبين والتحقق (`/register`)**:
   - ربط حساب الديسكورد مع اسم الشخصية في Albion Online.
   - تغيير اسم العضو في السيرفر تلقائياً إلى اسم شخصيته في اللعبة.
   - إسناد رتبة الأعضاء تلقائياً.

2. **📊 استعلام اللاعبين والكلان (`/player`, `/guild`)**:
   - البحث عن إحصائيات أي لاعب (PvP Kill Fame, PvE Fame, Crafting, Gathering, K/D Ratio).
   - عرض إحصائيات الكلان، عدد الأعضاء، وإجمالي الشهرة (Total Fame).
   - دعم جميع سيرفرات ألبيون (**Europe**, **West**, **East**).

3. **⚔️ إدارة الفعاليات والـ CTA (`/create_event`)**:
   - إرسال تنبيهات الفعاليات مع أزرار تفاعلية لاختيار الأدوار (Tank 🛡️, Healer 💚, Support ✨, DPS ⚔️, اعتذار ❌).
   - تحديث القائمة المباشرة للمشاركين داخل الرسالة.

4. **🛡️ نظام التعويضات ZvZ Re-gear (`/regear`)**:
   - تقديم طلب تعويض الموت في الـ ZvZ بواسطة رابط Killboard والـ IP.
   - لوحة تحكم تفاعلية للمسؤولين لقبول التعويض أو رفضه مع إرسال إشعار مباشر للاعب.

5. **📩 نظام التذاكر والتجنيد Recruitment Tickets (`/setup_tickets`)**:
   - إنشاء لوحة تذاكر تفاعلية تسمح للاعبين الجدد بفتح تذكرة تقديم خاصة.
   - إنشاء روم فرعي خاص باللاعب ومسؤولي التجنيد فقط.

6. **📖 أوامر عامة (`/help`, `/ping`, `/rules`)**:
   - دليل شامل باللغة العربية وشرح لجميع الأوامر.

---

## 🚀 طريقة التشغيل والتركيب (Setup Guide)

### 1️⃣ الخطوة الأولى: إنشاء التوكن (Discord Bot Token)
1. اذهب إلى [Discord Developer Portal](https://discord.com/developers/applications).
2. اضغط على **New Application** وادخل اسم البوت (مثل `Arab Albion`).
3. انتقل إلى تبويب **Bot**:
   - اضغط **Reset Token** وانسخ التوكن الخاص بالبوت.
   - قم بتفعيل الخيارات التالية تحت **Privileged Gateway Intents**:
     - ✅ **Presence Intent**
     - ✅ **Server Members Intent**
     - ✅ **Message Content Intent**
4. قم بدعوة البوت لسيرفرك عن طريق تبويب **OAuth2** -> **URL Generator**:
   - اختر scope: `bot` و `applications.commands`.
   - اختر Permissions: `Administrator` أو الصلاحيات المطلوبة (Manage Roles, Manage Channels, Send Messages).

---

### 2️⃣ الخطوة الثانية: إعداد بيئة العمل (Configuration)
قم بإنشاء ملف `.env` داخل مجلد المشروع وضع فيه التوكن وإعدادات السيرفر:

```env
DISCORD_TOKEN=your_discord_bot_token_here
GUILD_ID=your_discord_server_id_here
DEFAULT_GUILD_NAME=Arab Albion
DEFAULT_REGION=europe
```

---

### 3️⃣ الخطوة الثالثة: تشغيل البوت (Running the Bot)

تأكد من فتح المجلد في التيرمنال، ثم شغّل الأمر التالي:

```bash
.\venv\Scripts\python main.py
```

أو في حال عدم استخدام البيئة الافتراضية:
```bash
py -3 main.py
```

---

## 🛠️ تقنيات المستحدثة (Tech Stack)

- **Language**: Python 3.13
- **Framework**: `discord.py >= 2.3` (Slash Commands & UI Components)
- **HTTP Client**: `aiohttp` for Albion Online GameInfo REST API
- **Config**: `python-dotenv`

---

## 📁 هيكل المشروع (Project Architecture)

```
Arab Albion/
├── main.py              # النقطة الرئيسية لتشغيل البوت وتسجيل الأوامر
├── config.py            # قراءة الإعدادات والمتغيرات
├── requirements.txt     # المكتبات المطلوبة
├── .env.example         # نموذج ملف الإعدادات
├── cogs/
│   ├── albion.py        # أوامر التسجيل والبحث عن اللاعبين والكلان
│   ├── events.py        # أوامر الفعاليات وأزرار الأدوار (CTA)
│   ├── regear.py        # نظام التعويضات ومراجعة المسؤولين
│   ├── tickets.py       # نظام التذاكر والتجنيد الخاص
│   └── general.py       # دليل الأوامر، الفحص، والقوانين
└── utils/
    ├── albion_api.py    # الاتصال بـ API لعبة Albion Online
    └── embeds.py        # تصميم وتنسيق الرسائل التفاعلية (Embeds)
```
