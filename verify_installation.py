#!/usr/bin/env python3
"""
RawanAI Installation Verification Script
Checks if all dependencies and modules are correctly installed.
"""
import sys
import importlib.util


def check_module(module_name, display_name=None):
    """Check if a module is installed."""
    if display_name is None:
        display_name = module_name
    
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"❌ {display_name} - NOT INSTALLED")
        return False
    else:
        print(f"✅ {display_name} - OK")
        return True


def check_project_structure():
    """Check if project structure is correct."""
    import os
    
    print("\n📁 Checking project structure...")
    required_dirs = [
        "src/rawanai",
        "config",
        "tests",
        "docs"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ {dir_path}/ - OK")
        else:
            print(f"❌ {dir_path}/ - MISSING")
            all_exist = False
    
    return all_exist


def check_config():
    """Check if configuration is working."""
    print("\n⚙️  Checking configuration...")
    try:
        from config.config import config
        print(f"✅ Configuration loaded")
        print(f"   Model: {config.model.model_id}")
        print(f"   Temperature: {config.model.temperature}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False


def main():
    """Main verification function."""
    print("=" * 60)
    print("RawanAI Installation Verification")
    print("=" * 60)
    
    print("\n📦 Checking core dependencies...")
    all_ok = True
    
    # Check core dependencies
    all_ok &= check_module("gradio", "Gradio")
    
    # Optional dependencies (won't fail if missing)
    print("\n📦 Checking optional dependencies...")
    print("   (These are needed for full functionality)")
    check_module("torch", "PyTorch")
    check_module("transformers", "Transformers")
    check_module("accelerate", "Accelerate")
    
    # Check project structure
    all_ok &= check_project_structure()
    
    # Check configuration
    all_ok &= check_config()
    
    # Check if modules can be imported
    print("\n🐍 Checking RawanAI modules...")
    try:
        # Use importlib to check modules without importing heavy dependencies
        import importlib.util
        
        # Check prompts module (lightweight)
        spec = importlib.util.find_spec("src.rawanai.prompts")
        if spec is not None:
            print("✅ prompts module - OK")
        else:
            print("❌ prompts module - NOT FOUND")
            all_ok = False
        
        # Check chatbot module (lightweight with lazy loading)
        spec = importlib.util.find_spec("src.rawanai.chatbot")
        if spec is not None:
            print("✅ chatbot module - OK")
        else:
            print("❌ chatbot module - NOT FOUND")
            all_ok = False
        
        # Check config module (lightweight)
        spec = importlib.util.find_spec("config.config")
        if spec is not None:
            print("✅ config module - OK")
        else:
            print("❌ config module - NOT FOUND")
            all_ok = False
        
        # Check constants module
        spec = importlib.util.find_spec("src.rawanai.constants")
        if spec is not None:
            print("✅ constants module - OK")
        else:
            print("❌ constants module - NOT FOUND")
            all_ok = False
        
    except Exception as e:
        print(f"❌ Module check error: {e}")
        all_ok = False
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✅ All checks passed! RawanAI is ready to use.")
        print("\nTo start the application, run:")
        print("  python app.py")
    else:
        print("⚠️  Some checks failed. Please review the errors above.")
        print("\nTo install dependencies, run:")
        print("  pip install -r requirements.txt")
        return 1
    
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
