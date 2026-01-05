// تحديث الساعة
function updateClock() {
    const now = new Date();
    const clockElement = document.getElementById('clock');
    if (clockElement) {
        clockElement.innerText = now.toLocaleTimeString('ar-SA');
    }
}
setInterval(updateClock, 1000);
updateClock();

// فتح وإغلاق النوافذ
function openWindow(id) {
    const element = document.getElementById(id);
    if (element) {
        element.style.display = 'flex';
    }
}

function closeWindow(id) {
    const element = document.getElementById(id);
    if (element) {
        element.style.display = 'none';
    }
}

// قائمة البداية (placeholder)
function toggleStartMenu() {
    // يمكن إضافة قائمة بداية هنا لاحقاً
    console.log('Start menu toggled');
}

// جعل النوافذ قابلة للسحب (Draggable)
function makeDraggable(windowId, headerId) {
    const elmnt = document.getElementById(windowId);
    const header = document.getElementById(headerId);
    if (!elmnt || !header) return;
    
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    
    header.addEventListener('mousedown', dragMouseDown);

    function dragMouseDown(e) {
        // Only start drag if clicking on the header, not on controls
        if (e.target.classList.contains('dot')) return;
        
        e.preventDefault();
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.addEventListener('mouseup', closeDragElement);
        document.addEventListener('mousemove', elementDrag);
    }

    function elementDrag(e) {
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        document.removeEventListener('mouseup', closeDragElement);
        document.removeEventListener('mousemove', elementDrag);
    }
}

// منطق روان AI البسيط (للعرض)
function askAI() {
    const input = document.getElementById('user-msg');
    const chatBox = document.getElementById('chat-box');
    if (!input || !chatBox || input.value === "") return;

    chatBox.innerHTML += `<p><b>أنت:</b> ${escapeHtml(input.value)}</p>`;
    const userText = input.value;
    input.value = "";

    setTimeout(() => {
        chatBox.innerHTML += `<p style="color: #00ffcc;"><b>روان:</b> هلا بك.. أبشر، جاري تنفيذ طلبك بخصوص ${escapeHtml(userText)}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}

// دالة للهروب من HTML لمنع XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// إضافة دعم الإدخال بالضغط على Enter
document.addEventListener('DOMContentLoaded', function() {
    const userMsgInput = document.getElementById('user-msg');
    if (userMsgInput) {
        userMsgInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                askAI();
            }
        });
    }
    
    // تفعيل السحب للنوافذ
    makeDraggable('ai-window', 'ai-window-header');
});
