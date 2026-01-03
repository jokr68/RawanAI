"""
AI Model management for RawanAI.
Handles model loading, initialization, and text generation.
"""
import logging
from typing import List, Dict, Any, Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

from config.config import config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelManager:
    """Manages the AI model and text generation."""
    
    def __init__(self):
        """Initialize the model manager."""
        self.model = None
        self.tokenizer = None
        self.pipe = None
        self.generation_args = {
            "max_new_tokens": config.model.max_new_tokens,
            "return_full_text": False,
            "temperature": config.model.temperature,
            "do_sample": config.model.do_sample,
        }
        
    def load_model(self) -> None:
        """Load the AI model and tokenizer."""
        try:
            logger.info(f"Loading model: {config.model.model_id}")
            
            self.tokenizer = AutoTokenizer.from_pretrained(config.model.model_id)
            self.model = AutoModelForCausalLM.from_pretrained(
                config.model.model_id,
                device_map=config.model.device_map,
                torch_dtype=config.model.torch_dtype,
                trust_remote_code=config.model.trust_remote_code,
            )
            
            self.pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
            )
            
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def generate_response(
        self,
        messages: List[Dict[str, str]],
        custom_args: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Generate a response from the model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            custom_args: Optional custom generation arguments.
        
        Returns:
            str: The generated response text.
        """
        if self.pipe is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        
        try:
            gen_args = self.generation_args.copy()
            if custom_args:
                gen_args.update(custom_args)
            
            output = self.pipe(messages, **gen_args)
            response = output[0]['generated_text']
            return response
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"عذراً يا قلبي، حدث خطأ: {str(e)}"
    
    def is_loaded(self) -> bool:
        """Check if the model is loaded."""
        return self.pipe is not None


# Global model manager instance
model_manager = ModelManager()
