// مصفوفة ردود مروى النجدية (محاكاة الذكاء)
const marwaKnowledge = {
    greetings: ["يا هلا والله بأحمد!", "ارحب تراحيب المطر", "سمّ، آمرني؟"],
    unknown: ["والله يا أحمد هالنقطة يبي لها بحث، بس أبشر بعزك بدرسها وأرد عليك.", "وش تقصد بالضبط يا بعدي؟"],
    habits: ["سجلت لك العادة، وترا الاستمرار هو السر.", "كفو! هذا الشغل الصح."]
};

// تشغيل النظام
window.onload = function() {
    setTimeout(() => {
        document.getElementById('boot-screen').style.opacity = '0';
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('desktop').classList.remove('hidden');
        }, 1000);
    }, 2000); // محاكاة وقت الإقلاع
    updateClock();
};

// الساعة
function updateClock() {
    const now = new Date();
    document.getElementById('clock').innerText = now.toLocaleTimeString('ar-SA', {hour: '2-digit', minute:'2-digit'});
    setTimeout(updateClock, 1000);
}

// إدارة النوافذ
function openApp(appId) {
    document.querySelectorAll('.window').forEach(w => w.classList.add('hidden'));
    document.getElementById('app-' + appId).classList.remove('hidden');
}

function closeApp(appId) {
    document.getElementById('app-' + appId).classList.add('hidden');
}

// منطق الشات (مروى)
function handleEnter(e) { if(e.key === 'Enter') sendMessage(); }

function sendMessage() {
    const input = document.getElementById('user-input');
    const msg = input.value.trim();
    if (!msg) return;

    // عرض رسالة المستخدم
    addMessage(msg, 'user');
    input.value = '';

    // محاكاة التفكير والرد
    setTimeout(() => {
        let reply = generateMarwaResponse(msg);
        addMessage(reply, 'bot');
    }, 800);
}

function addMessage(text, sender) {
    const box = document.getElementById('chat-box');
    const div = document.createElement('div');
    div.className = `message ${sender}`;
    div.innerText = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

function generateMarwaResponse(text) {
    text = text.toLowerCase();
    if (text.includes('هلا') || text.includes('سلام')) return marwaKnowledge.greetings[Math.floor(Math.random() * marwaKnowledge.greetings.length)];
    if (text.includes('تحليل') || text.includes('وضع')) return "بناءً على بياناتك الأخيرة، أشوف إن وضعك مستقر بس تحتاج تزيد ساعات نومك عشان تركيزك يوصل 100%.";
    if (text.includes('شكرا')) return "العفو، حنا في الخدمة طال عمرك.";
    if (text.includes('من انت')) return "أنا مروى، ذراعك اليمين، وعقلك الرقمي. مخلوقة عشانك يا أحمد.";
    return marwaKnowledge.unknown[Math.floor(Math.random() * marwaKnowledge.unknown.length)];
}

// تسجيل العادات
function logHabit(habit) {
    // هنا يمكن ربط قاعدة بيانات حقيقية لاحقاً
    const status = document.getElementById('log-status');
    status.innerText = `✅ تم تسجيل "${habit}" في قاعدة البيانات.`;
    
    // ردة فعل فورية من مروى في الشات لو كان مفتوح
    setTimeout(() => {
        status.innerText = '';
        // تحديث التحليل وهمياً
        document.getElementById('ai-insight-text').innerText = `تحديث: تسجيلك لـ "${habit}" الحين له تأثير إيجابي على مؤشراتك الحيوية.`;
    }, 2000);
}
