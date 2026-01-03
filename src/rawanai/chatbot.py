"""
Chatbot functionality for RawanAI.
Handles conversation history and message processing.
"""
import logging
from typing import List, Tuple, Optional

from src.rawanai.prompts import get_system_prompt

logger = logging.getLogger(__name__)


class Chatbot:
    """Manages chat conversations with Rawan."""
    
    def __init__(self):
        """Initialize the chatbot."""
        self.system_prompt = get_system_prompt()
        self._model_manager = None
    
    @property
    def model_manager(self):
        """Lazy load model manager."""
        if self._model_manager is None:
            from src.rawanai.model import model_manager
            self._model_manager = model_manager
        return self._model_manager
    
    def process_message(
        self,
        message: str,
        history: List[Tuple[str, str]]
    ) -> str:
        """
        Process a user message and generate a response.
        
        Args:
            message: The user's message.
            history: List of (user_message, assistant_message) tuples.
        
        Returns:
            str: The assistant's response.
        """
        if not message or not message.strip():
            return "يا قلبي، قل لي شيء! 💜"
        
        try:
            # Build messages list with system prompt
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add conversation history
            for user_msg, assistant_msg in history:
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": assistant_msg})
            
            # Add current message
            messages.append({"role": "user", "content": message})
            
            # Generate response
            response = self.model_manager.generate_response(messages)
            
            logger.info(f"Generated response for message: {message[:50]}...")
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return f"آسفة يا حبيبي، حدث خطأ: {str(e)} 💔"
    
    def clear_history(self) -> List[Tuple[str, str]]:
        """
        Clear conversation history.
        
        Returns:
            Empty list representing cleared history.
        """
        logger.info("Conversation history cleared")
        return []


# Global chatbot instance
chatbot = Chatbot()
