"""
RawanAI - Your Secretary
Main application entry point.

Copyright © 2025 Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari
All rights reserved.
"""
import logging
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import modules
from src.rawanai.model import model_manager
from src.rawanai.ui import create_interface, launch_interface


def main():
    """Main application entry point."""
    try:
        logger.info("Starting RawanAI application...")
        
        # Load the AI model
        logger.info("Loading AI model (this may take a few minutes)...")
        model_manager.load_model()
        
        # Create the Gradio interface
        demo = create_interface()
        
        # Launch the application
        launch_interface(demo)
        
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
