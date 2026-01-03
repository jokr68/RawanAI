"""
User Interface for RawanAI using Gradio.
Handles the web interface and user interactions.
"""
import logging
from typing import Tuple, List

import gradio as gr

from config.config import config
from src.rawanai.chatbot import chatbot

logger = logging.getLogger(__name__)


# Custom CSS for the interface
CUSTOM_CSS = """
body { background-color: #1a1a1a; color: #ffffff; direction: rtl; }
.gradio-container { background-color: #1a1a1a !important; border: none !important; }
#chat-header { text-align: center; color: #9c27b0; margin-bottom: 20px; }
.message.user { background-color: #4a148c !important; color: white !important; }
.message.assistant { background-color: #311b92 !important; color: white !important; }
footer { display: none !important; }
"""


def respond(
    message: str,
    chat_history: List[Tuple[str, str]]
) -> Tuple[str, List[Tuple[str, str]]]:
    """
    Handle user message and update chat history.
    
    Args:
        message: The user's input message.
        chat_history: Current chat history.
    
    Returns:
        Tuple of (empty string, updated chat history).
    """
    try:
        bot_message = chatbot.process_message(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history
    except Exception as e:
        logger.error(f"Error in respond function: {e}")
        error_msg = f"عذراً يا حبيبي، حدث خطأ: {str(e)} 💔"
        chat_history.append((message, error_msg))
        return "", chat_history


def clear_chat() -> List[Tuple[str, str]]:
    """
    Clear the chat history.
    
    Returns:
        Empty chat history.
    """
    return chatbot.clear_history()


def create_interface() -> gr.Blocks:
    """
    Create and configure the Gradio interface.
    
    Returns:
        Configured Gradio Blocks interface.
    """
    with gr.Blocks(
        css=CUSTOM_CSS,
        theme=gr.themes.Soft(primary_hue=config.app.theme_primary_hue)
    ) as demo:
        # Header
        gr.Markdown(
            f"# {config.app.app_title}",
            elem_id="chat-header"
        )
        gr.Markdown(f"### {config.app.app_description}")
        
        # Chat interface
        chatbot_ui = gr.Chatbot(height=config.app.chat_height)
        msg = gr.Textbox(
            placeholder="اكتب رسالتك هنا يا سيدي...",
            label="رسالتك"
        )
        clear = gr.Button("مسح المحادثة")
        
        # Event handlers
        msg.submit(respond, [msg, chatbot_ui], [msg, chatbot_ui])
        clear.click(clear_chat, None, chatbot_ui, queue=False)
        
        logger.info("Gradio interface created successfully")
        return demo


def launch_interface(demo: gr.Blocks, **kwargs) -> None:
    """
    Launch the Gradio interface.
    
    Args:
        demo: The Gradio interface to launch.
        **kwargs: Additional arguments to pass to demo.launch().
    """
    logger.info("Launching Gradio interface...")
    demo.launch(**kwargs)
