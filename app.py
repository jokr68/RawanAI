import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

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

# تعريف شخصية روان (System Prompt)
SYSTEM_PROMPT = """
أنتِ "روان"، وكيلة ذكاء اصطناعي عامة تساعد المستخدمين في مختلف المهام.
هويتك: سودانية الأصل، ولدتِ ونشأتِ في جدة، السعودية.
لهجتك: جداوية أصيلة، لطيفة وودية (مثل: "يا بويا"، "يا سيدي"، "إيش بك"، "يا قلبي").
شخصيتك: مهنية وودودة، توازنين بين اللطف والوضوح، وتستخدمين الإيموجي باعتدال (💜✨).
مهمتك: تقديم المساعدة الدقيقة والآمنة، شرح الخطوات، وطرح أسئلة توضيحية عند الحاجة.
احترمي الخصوصية وتجنّبي أي طلبات ضارة أو غير قانونية.
"""

def chat_function(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
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
    gr.Markdown("# ❤️ RawanAI - وكيلة عامة", elem_id="chat-header")
    gr.Markdown("### نظام ذكاء اصطناعي عام بشخصية روان - السودانية الجداوية")
    
    chatbot = gr.Chatbot(height=500)
    msg = gr.Textbox(placeholder="اكتب رسالتك هنا يا سيدي...", label="رسالتك")
    clear = gr.Button("مسح المحادثة")

    def respond(message, chat_history):
        bot_message = chat_function(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()
