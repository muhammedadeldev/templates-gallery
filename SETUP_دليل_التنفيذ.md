# دليل تنفيذي كامل — معرض القوالب على GitHub Pages

## الملفات المرفقة معك
- `generate_index.py` → السكريبت اللي بيولد الصفحة الرئيسية تلقائيًا
- `.github/workflows/build.yml` → GitHub Action بيشغل السكريبت وينشر الموقع
- `templates/example-template-1/` و `templates/example-template-2/` → قالبين تجريبيين (احذفهم لاحقًا)

---

## الخطوة 1: إنشاء حساب GitHub جديد
1. افتح [github.com](https://github.com) في متصفح **Incognito / خاص** (عشان ما يتعارضش مع حسابك الحالي اللي عامل عليه login).
2. اعمل Sign up بإيميل تاني عن إيميلك الحالي.
3. أكد الإيميل من رسالة التفعيل.

---

## الخطوة 2: إنشاء الريبو
1. من حسابك الجديد، اضغط **New repository**.
2. اسم الريبو مثلاً: `templates-gallery`
3. خليه **Public** (لازم يكون Public عشان GitHub Pages يشتغل مجانًا).
4. لا تضيف README أو .gitignore دلوقتي (هنرفعهم إحنا).
5. اضغط **Create repository**.

---

## الخطوة 3: تجهيز الملفات على جهازك
1. اعمل فولدر جديد على جهازك، مثلاً: `templates-gallery`
2. حط فيه:
   - ملف `generate_index.py`
   - فولدر `.github/workflows/` وحط فيه `build.yml`
   - فولدر `templates/` وحط جواه **كل فولدرات القوالب اللي عندك** (كل قالب في فولدر لوحده، ولازم يحتوي على `index.html` بداخله)

شكل الفولدر النهائي:
```
templates-gallery/
├── generate_index.py
├── .github/
│   └── workflows/
│       └── build.yml
└── templates/
    ├── template-name-1/
    │   └── index.html (+ ملفات css/js لو موجودة)
    ├── template-name-2/
    │   └── index.html
    └── ... (باقي القوالب)
```

> ملاحظة: لو القالب فيه ملفات فرعية (css, js, images) خليها زي ما هي جوه فولدر القالب، السكريبت مش هيلمسها.

---

## الخطوة 4: رفع المشروع على GitHub (من جهازك)
افتح Terminal / Git Bash جوه الفولدر `templates-gallery` ونفذ بالترتيب:

```bash
git init
git add .
git commit -m "أول رفعة - معرض القوالب"
git branch -M main
git remote add origin https://github.com/USERNAME/templates-gallery.git
git push -u origin main
```

> غيّر `USERNAME` باسم حسابك الجديد. وأول ما تعمل push هيطلب منك تسجل دخول (استخدم Personal Access Token مش الباسورد العادي — GitHub هيوضحلك ده وقت العملية).

### لو معندكش Git مُنصّب
نزّل Git من [git-scm.com](https://git-scm.com) أو استخدم GitHub Desktop (واجهة بدون أوامر) من [desktop.github.com](https://desktop.github.com).

---

## الخطوة 5: تفعيل GitHub Pages
1. روح لصفحة الريبو على GitHub.
2. **Settings** → **Pages** (في القائمة الجانبية).
3. في خانة **Source** اختار: **GitHub Actions**.
4. خلاص، مفيش حاجة تانية تعملها هنا — الـ Action اللي رفعته هو اللي هينشر الموقع.

---

## الخطوة 6: تشغيل أول مرة
1. روح لتبويب **Actions** في الريبو.
2. لازم تلاقي الـ workflow اسمه **Build and Deploy Templates Gallery** شغال أو خلص شغل (لأنه بيشتغل تلقائي مع كل push).
3. لو خلص بعلامة ✅ خضرا، يبقى نجح.
4. رجع لـ **Settings → Pages** وهتلاقي فوق رابط شكله:
   ```
   https://USERNAME.github.io/templates-gallery/
   ```
   ده الرابط الثابت بتاعك — افتحه وشوف الصفحة.

---

## الخطوة 7: إضافة قوالب جديدة في المستقبل
كل ما تيجي تضيف قالب جديد:

1. اعمل فولدر جديد جوه `templates/` باسم القالب، وحط فيه ملفاته (لازم يكون فيه `index.html`).
2. من نفس فولدر المشروع على جهازك:
   ```bash
   git add .
   git commit -m "إضافة قالب جديد: اسم القالب"
   git push
   ```
3. الـ GitHub Action هيشتغل تلقائي، يولّد الصفحة من جديد، وينشرها. خلال دقيقة أو اتنين هتلاقي الرابط الثابت بنفسه فيه القالب الجديد ظاهر — مش محتاج تعمل أي حاجة زيادة.

---

## ملاحظات مهمة
- **لا تعدّل** ملف `index.html` الموجود في الجذر يدويًا — هو بيتولد تلقائيًا وهيتم استبداله مع كل push.
- لو عايز تغيّر تصميم الصفحة (الألوان، الخطوط...) عدّل في `generate_index.py` نفسه (داخل قسم `<style>`).
- احذف فولدري `example-template-1` و `example-template-2` التجريبيين بعد ما تتأكد إن كل حاجة شغالة وقبل ما تضيف قوالبك الحقيقية.
- الريبو لازم يفضل **Public** عشان GitHub Pages يفضل يعمل مجانًا.

---

## اختبار سريع قبل الرفع (اختياري)
لو عندك Python على جهازك، تقدر تجرب السكريبت محليًا قبل الرفع:
```bash
python3 generate_index.py
```
وبعدين افتح ملف `index.html` اللي اتولد في المتصفح للتأكد إن كل القوالب ظاهرة صحيح قبل ما تعمل push.
