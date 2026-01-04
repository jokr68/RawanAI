#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اختبار التكامل البسيط للتطبيق (بدون تحميل النموذج)
"""

import sys

def test_imports():
    """اختبار استيراد المكتبات الأساسية"""
    print("🧪 اختبار استيراد المكتبات...\n")
    
    try:
        import gradio as gr
        print("✅ Gradio imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Gradio: {e}")
        return False
    
    try:
        from marwa_agent import MarwaAgent, MARWA_SYSTEM_PROMPT
        print("✅ Marwa agent imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Marwa agent: {e}")
        return False
    
    return True

def test_marwa_agent():
    """اختبار وكيلة مروى"""
    print("\n🧪 اختبار وكيلة مروى...\n")
    
    try:
        from marwa_agent import MarwaAgent, MARWA_SYSTEM_PROMPT
        
        marwa = MarwaAgent()
        print(f"✅ وكيلة مروى تم إنشاؤها: {marwa.name}")
        print(f"   الشخصية: {marwa.personality}")
        print(f"   القدرات: {len(marwa.capabilities)} قدرات")
        
        # اختبار System Prompt
        prompt = marwa.get_system_prompt()
        print(f"✅ System Prompt: {len(prompt)} حرف")
        
        # اختبار توليد ملف تعريفي
        profile = marwa.generate_profile(
            name="اختبار",
            dominant_trait="منظم",
            observed_habits=["يحب القراءة"]
        )
        print(f"✅ الملف التعريفي: {profile['الاسم']}")
        
        return True
    except Exception as e:
        print(f"❌ خطأ في اختبار مروى: {e}")
        return False

def test_app_structure():
    """اختبار بنية التطبيق الأساسية"""
    print("\n🧪 اختبار بنية التطبيق...\n")
    
    try:
        # قراءة ملف التطبيق
        with open('app.py', 'r', encoding='utf-8') as f:
            app_content = f.read()
        
        # التحقق من العناصر الأساسية
        required_elements = [
            'import gradio as gr',
            'from marwa_agent import MarwaAgent',
            'RAWAN_SYSTEM_PROMPT',
            'MARWA_SYSTEM_PROMPT',
            'MarwaAgent()',
            'gr.Tabs()',
            'with gr.Tab("💜 روان',
            'with gr.Tab("💡 مروى',
            'with gr.Tab("📋 توليد ملف تعريفي")',
            'with gr.Tab("📊 تحليل الارتباطات")',
            'with gr.Tab("🔍 اكتشاف الأنماط")',
            'with gr.Tab("✨ إدارة الرفاهية")',
        ]
        
        all_found = True
        for element in required_elements:
            if element in app_content:
                print(f"✅ وُجد: {element[:50]}")
            else:
                print(f"❌ مفقود: {element[:50]}")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"❌ خطأ في اختبار البنية: {e}")
        return False

def main():
    """الدالة الرئيسية للاختبار"""
    print("=" * 60)
    print("🚀 اختبار التكامل للتطبيق")
    print("=" * 60)
    
    results = {
        'imports': test_imports(),
        'marwa': test_marwa_agent(),
        'structure': test_app_structure()
    }
    
    print("\n" + "=" * 60)
    print("📊 ملخص النتائج")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ نجح" if result else "❌ فشل"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 جميع الاختبارات نجحت! التطبيق جاهز للاستخدام")
    else:
        print("⚠️ بعض الاختبارات فشلت، يرجى المراجعة")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
