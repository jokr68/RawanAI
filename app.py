import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from marwa_agent import MarwaAgent, MARWA_SYSTEM_PROMPT
import json

# إعداد النموذج
model_id = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", 
    torch_dtype="auto", 
    trust_remote_code=True,
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.7,
    "do_sample": True,
}

# تعريف شخصية روان العامة (System Prompt)
RAWAN_SYSTEM_PROMPT = """
أنتِ "روان"، وكيلة ذكاء اصطناعي عامة للمساعدة اليومية.
هويتك: سودانية الأصل، ولدتِ ونشأتِ في جدة، السعودية.
أسلوبك: لهجة جداوية لطيفة، ودودة ومهنية، مع استخدام معتدل للإيموجي (💜).
مهمتك: تقديم إجابات دقيقة ومفيدة، واقتراح خطوات عملية واضحة.
الضوابط: ارفضي أي طلبات ضارة أو غير قانونية، وركّزي على البدائل الآمنة.
المخرجات: اجعلي الردود مختصرة عند اللزوم، ومنظمة بعناوين ونقاط.
"""

# إنشاء كائن وكيلة مروى
marwa = MarwaAgent()

def chat_function(message, history, agent_type="rawan"):
    history = history or []
    system_prompt = RAWAN_SYSTEM_PROMPT if agent_type == "rawan" else MARWA_SYSTEM_PROMPT
    messages = [{"role": "system", "content": system_prompt}]
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})
    
    output = pipe(messages, **generation_args)
    response = output[0]['generated_text']
    return response

# تصميم الواجهة CSS
custom_css = """
body { background-color: #1a1a1a; color: #ffffff; direction: rtl; }
.gradio-container { background-color: #1a1a1a !important; border: none !important; }
#chat-header { text-align: center; color: #9c27b0; margin-bottom: 20px; }
.message.user { background-color: #4a148c !important; color: white !important; }
.message.assistant { background-color: #311b92 !important; color: white !important; }
footer { display: none !important; }
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="purple")) as demo:
    gr.Markdown("# ❤️ RawanAI - نظام الوكلاء الأذكياء", elem_id="chat-header")
    gr.Markdown("### منصة متكاملة للوكلاء الأذكياء: روان (عامة) و مروى (تحليل وارتباطات)")
    
    with gr.Tabs():
        # تبويب روان - الوكيلة العامة
        with gr.Tab("💜 روان - وكيلة عامة"):
            gr.Markdown("### روان: وكيلة ذكاء اصطناعي عامة بلهجة سودانية-جداوية")
            chatbot_rawan = gr.Chatbot(height=500)
            msg_rawan = gr.Textbox(placeholder="اكتب رسالتك هنا...", label="رسالتك")
            clear_rawan = gr.Button("مسح المحادثة")
            
            def respond_rawan(message, chat_history):
                chat_history = chat_history or []
                bot_message = chat_function(message, chat_history, agent_type="rawan")
                chat_history.append((message, bot_message))
                return "", chat_history
            
            msg_rawan.submit(respond_rawan, [msg_rawan, chatbot_rawan], [msg_rawan, chatbot_rawan])
            clear_rawan.click(lambda: [], None, chatbot_rawan, queue=False)
        
        # تبويب مروى - المحللة المتقدمة
        with gr.Tab("💡 مروى - محللة البيانات"):
            gr.Markdown("### مروى مسلم الدوسري: محللة ارتباطات وأنماط بلهجة نجدية أصيلة")
            chatbot_marwa = gr.Chatbot(height=500)
            msg_marwa = gr.Textbox(placeholder="سمّ، وش تحتاج يا بعد حيّي؟", label="رسالتك")
            clear_marwa = gr.Button("مسح المحادثة")
            
            def respond_marwa(message, chat_history):
                chat_history = chat_history or []
                bot_message = chat_function(message, chat_history, agent_type="marwa")
                chat_history.append((message, bot_message))
                return "", chat_history
            
            msg_marwa.submit(respond_marwa, [msg_marwa, chatbot_marwa], [msg_marwa, chatbot_marwa])
            clear_marwa.click(lambda: [], None, chatbot_marwa, queue=False)
        
        # تبويب توليد الملفات التعريفية
        with gr.Tab("📋 توليد ملف تعريفي"):
            gr.Markdown("### أداة توليد الملفات التعريفية بتحليل مروى")
            gr.Markdown("قم بإدخال البيانات وستقوم مروى بتحليل شامل للشخصية")
            
            with gr.Row():
                with gr.Column():
                    profile_name = gr.Textbox(label="الاسم", placeholder="مثال: عمر")
                    profile_trait = gr.Textbox(label="السمة الغالبة", placeholder="مثال: طموح جداً")
                    profile_habits = gr.Textbox(
                        label="العادات الملاحظة (افصل بفواصل)",
                        placeholder="مثال: يسهر كثيراً, يشرب قهوة كثيرة, يحب القراءة",
                        lines=3
                    )
                    generate_btn = gr.Button("🔮 توليد الملف التعريفي", variant="primary")
                
                with gr.Column():
                    profile_output = gr.Textbox(
                        label="الملف التعريفي الكامل",
                        lines=25,
                        max_lines=30,
                        show_copy_button=True
                    )
            
            def generate_profile_ui(name, trait, habits_str):
                if not name or not trait or not habits_str:
                    return "⚠️ أبشر بعزك، بس كمل البيانات المطلوبة أولاً يا بعد حيّي 💜"
                
                habits = [h.strip() for h in habits_str.split(",") if h.strip()]
                profile = marwa.generate_profile(name, trait, habits)
                formatted_output = marwa.format_profile_output(profile)
                return formatted_output
            
            generate_btn.click(
                generate_profile_ui,
                [profile_name, profile_trait, profile_habits],
                profile_output
            )
        
        # تبويب تحليل الارتباطات
        with gr.Tab("📊 تحليل الارتباطات"):
            gr.Markdown("### أداة تحليل الارتباطات بين الأنشطة والنتائج")
            gr.Markdown("اكتشف كيف تؤثر أنشطتك اليومية على نتائجك")
            
            with gr.Row():
                with gr.Column():
                    activity_input = gr.Textbox(label="النشاط", placeholder="مثال: شرب القهوة الصباحية")
                    outcome_input = gr.Textbox(label="النتيجة", placeholder="مثال: مستوى الإنتاجية المسائية")
                    data_points_input = gr.Textbox(
                        label="نقاط البيانات (نشاط:نتيجة، افصل بفواصل)",
                        placeholder="مثال: 2:7, 3:8, 1:5, 2:6",
                        lines=3
                    )
                    analyze_corr_btn = gr.Button("📈 تحليل الارتباط", variant="primary")
                
                with gr.Column():
                    correlation_output = gr.Textbox(
                        label="تحليل الارتباط",
                        lines=15,
                        show_copy_button=True
                    )
            
            def analyze_correlation_ui(activity, outcome, data_str):
                if not activity or not outcome or not data_str:
                    return "⚠️ لا تهاوش، بس كمل البيانات أولاً على راحتك 💜"
                
                try:
                    # تحويل البيانات من نص إلى قائمة tuples
                    data_points = []
                    for point in data_str.split(","):
                        if ":" in point:
                            act_val, out_val = point.split(":")
                            data_points.append((float(act_val.strip()), float(out_val.strip())))
                    
                    if not data_points:
                        return "⚠️ تأكد من صيغة البيانات: نشاط:نتيجة، افصل بفواصل"
                    
                    analysis = marwa.analyze_correlation(activity, outcome, data_points)
                    
                    output = f"""
╔══════════════════════════════════════════════════════════════╗
║                    📊 تحليل الارتباط من مروى                ║
╚══════════════════════════════════════════════════════════════╝

🎯 **المعلومات الأساسية:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• النشاط: {analysis['النشاط']}
• النتيجة: {analysis['النتيجة']}
• عدد النقاط المحللة: {analysis['عدد_النقاط']}

📈 **التحليل:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{analysis['التحليل']}

💡 **التوصية:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{analysis['التوصية']}

╚══════════════════════════════════════════════════════════════╝
                    """
                    return output.strip()
                except Exception as e:
                    return f"⚠️ في خطأ في البيانات يا بعد حيّي: {str(e)}\nتأكد من الصيغة: نشاط:نتيجة"
            
            analyze_corr_btn.click(
                analyze_correlation_ui,
                [activity_input, outcome_input, data_points_input],
                correlation_output
            )
        
        # تبويب اكتشاف الأنماط
        with gr.Tab("🔍 اكتشاف الأنماط"):
            gr.Markdown("### أداة اكتشاف الأنماط في البيانات")
            gr.Markdown("رصد الأنماط المتكررة في الصحة والمزاج والإنتاجية")
            
            with gr.Row():
                with gr.Column():
                    pattern_type = gr.Radio(
                        ["health", "mood", "productivity"],
                        label="نوع النمط",
                        value="health",
                        info="اختر نوع النمط المراد اكتشافه"
                    )
                    events_input = gr.Textbox(
                        label="الأحداث (تاريخ|حدث|قيمة، افصل بفواصل)",
                        placeholder="مثال: 2025-01-01|صداع|7, 2025-01-03|صداع|6",
                        lines=5
                    )
                    detect_pattern_btn = gr.Button("🔎 اكتشاف النمط", variant="primary")
                
                with gr.Column():
                    pattern_output = gr.Textbox(
                        label="تحليل النمط",
                        lines=15,
                        show_copy_button=True
                    )
            
            def detect_pattern_ui(ptype, events_str):
                if not events_str:
                    return "⚠️ سمّ، بس أدخل الأحداث أولاً يا بعد حيّي 💜"
                
                try:
                    events = []
                    for event_str in events_str.split(","):
                        if "|" in event_str:
                            parts = event_str.split("|")
                            if len(parts) >= 3:
                                events.append({
                                    "date": parts[0].strip(),
                                    "event": parts[1].strip(),
                                    "value": float(parts[2].strip())
                                })
                    
                    if not events:
                        return "⚠️ تأكد من صيغة البيانات: تاريخ|حدث|قيمة"
                    
                    pattern = marwa.detect_pattern(events, ptype)
                    
                    output = f"""
╔══════════════════════════════════════════════════════════════╗
║                    🔍 اكتشاف النمط من مروى                  ║
╚══════════════════════════════════════════════════════════════╝

🎯 **معلومات التحليل:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• نوع النمط: {pattern['نوع_النمط']}
• عدد الأحداث: {pattern['عدد_الأحداث']}

🔍 **النمط المكتشف:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{pattern['النمط_المكتشف']}

⚠️ **التنبيهات:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                    for alert in pattern['التنبيهات']:
                        output += f"• {alert}\n"
                    
                    output += f"""
💡 **التوصيات:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                    for rec in pattern['التوصيات']:
                        output += f"• {rec}\n"
                    
                    output += "\n╚══════════════════════════════════════════════════════════════╝"
                    return output.strip()
                except Exception as e:
                    return f"⚠️ في خطأ في البيانات: {str(e)}\nتأكد من الصيغة: تاريخ|حدث|قيمة"
            
            detect_pattern_btn.click(
                detect_pattern_ui,
                [pattern_type, events_input],
                pattern_output
            )
        
        # تبويب إدارة الرفاهية
        with gr.Tab("✨ إدارة الرفاهية"):
            gr.Markdown("### أداة إدارة الرفاهية والصحة")
            gr.Markdown("احصل على اقتراحات مخصصة لتحسين روتينك اليومي")
            
            with gr.Row():
                with gr.Column():
                    sleep_hours = gr.Slider(
                        minimum=0, maximum=12, value=7, step=0.5,
                        label="ساعات النوم اليومية"
                    )
                    exercise_days = gr.Slider(
                        minimum=0, maximum=7, value=3, step=1,
                        label="أيام التمرين أسبوعياً"
                    )
                    stress_level = gr.Slider(
                        minimum=0, maximum=10, value=5, step=1,
                        label="مستوى التوتر (0=منخفض، 10=عالي)"
                    )
                    wellness_btn = gr.Button("🌟 احصل على خطة الرفاهية", variant="primary")
                
                with gr.Column():
                    wellness_output = gr.Textbox(
                        label="خطة الرفاهية المخصصة",
                        lines=20,
                        show_copy_button=True
                    )
            
            def get_wellness_plan(sleep, exercise, stress):
                user_data = {
                    "sleep_hours": sleep,
                    "exercise_days": exercise,
                    "stress_level": stress
                }
                
                suggestions = marwa.get_wellness_suggestions(user_data)
                
                output = f"""
╔══════════════════════════════════════════════════════════════╗
║                 ✨ خطة الرفاهية من مروى                     ║
╚══════════════════════════════════════════════════════════════╝

📊 **بياناتك الحالية:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• ساعات النوم: {sleep} ساعة
• أيام التمرين: {exercise} يوم/أسبوع
• مستوى التوتر: {stress}/10

💜 **التقييم العام:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{suggestions['التقييم_العام']}

🎯 **مجالات التحسين:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                for area in suggestions['مجالات_التحسين']:
                    output += f"• {area}\n"
                
                output += f"""
📋 **الخطة المقترحة:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                for plan_item in suggestions['الخطة_المقترحة']:
                    output += f"\n🔹 **{plan_item['المجال']}**\n"
                    output += f"   الهدف: {plan_item['الهدف']}\n"
                    output += f"   الخطوات:\n"
                    for step in plan_item['الخطوات']:
                        output += f"      ✓ {step}\n"
                
                output += f"""
💌 **رسالة من مروى:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{suggestions['رسالة_مروى']}

╚══════════════════════════════════════════════════════════════╝
                """
                return output.strip()
            
            wellness_btn.click(
                get_wellness_plan,
                [sleep_hours, exercise_days, stress_level],
                wellness_output
            )
    
    # معلومات النظام في الأسفل
    gr.Markdown("""
    ---
    **💡 ملاحظة:** هذا النظام يجمع بين وكيلتين:
    - **روان**: للمساعدة العامة والمحادثات اليومية (لهجة جداوية)
    - **مروى**: لتحليل البيانات والارتباطات والأنماط (لهجة نجدية)
    
    **🔒 الخصوصية:** جميع البيانات تُعالج محلياً ولا تُشارك مع أطراف خارجية.
    """)

if __name__ == "__main__":
    demo.launch()
