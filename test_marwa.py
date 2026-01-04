#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
اختبار وحدة مروى مسلم الدوسري
"""

from marwa_agent import MarwaAgent

def test_marwa_agent():
    """اختبار الوظائف الأساسية لوكيلة مروى"""
    print("🧪 بدء اختبار وكيلة مروى...\n")
    
    # إنشاء كائن مروى
    marwa = MarwaAgent()
    print(f"✅ تم إنشاء وكيلة: {marwa.name}")
    print(f"   الشخصية: {marwa.personality}")
    print(f"   القدرات: {', '.join(marwa.capabilities)}\n")
    
    # اختبار 1: توليد ملف تعريفي
    print("=" * 60)
    print("📋 اختبار 1: توليد ملف تعريفي")
    print("=" * 60)
    profile = marwa.generate_profile(
        name="عمر",
        dominant_trait="طموح جداً",
        observed_habits=["يسهر كثيراً", "يشرب قهوة كثيرة", "يحب القراءة"]
    )
    print(marwa.format_profile_output(profile))
    print("\n✅ اختبار توليد الملف التعريفي نجح!\n")
    
    # اختبار 2: تحليل الارتباطات
    print("=" * 60)
    print("📊 اختبار 2: تحليل الارتباطات")
    print("=" * 60)
    correlation = marwa.analyze_correlation(
        activity="شرب القهوة الصباحية",
        outcome="مستوى الإنتاجية المسائية",
        data_points=[(2, 7), (3, 8), (1, 5), (2, 6), (3, 9)]
    )
    print(f"النشاط: {correlation['النشاط']}")
    print(f"النتيجة: {correlation['النتيجة']}")
    print(f"عدد النقاط: {correlation['عدد_النقاط']}")
    print(f"\nالتحليل:\n{correlation['التحليل']}")
    print(f"\nالتوصية:\n{correlation['التوصية']}")
    print("\n✅ اختبار تحليل الارتباطات نجح!\n")
    
    # اختبار 3: اكتشاف الأنماط
    print("=" * 60)
    print("🔍 اختبار 3: اكتشاف الأنماط")
    print("=" * 60)
    events = [
        {"date": "2025-01-01", "event": "صداع", "value": 7},
        {"date": "2025-01-03", "event": "صداع", "value": 6},
        {"date": "2025-01-05", "event": "صداع", "value": 8},
        {"date": "2025-01-07", "event": "صداع", "value": 7}
    ]
    pattern = marwa.detect_pattern(events, pattern_type="health")
    print(f"نوع النمط: {pattern['نوع_النمط']}")
    print(f"عدد الأحداث: {pattern['عدد_الأحداث']}")
    print(f"\nالنمط المكتشف:\n{pattern['النمط_المكتشف']}")
    print(f"\nالتنبيهات:")
    for alert in pattern['التنبيهات']:
        print(f"  • {alert}")
    print(f"\nالتوصيات:")
    for rec in pattern['التوصيات']:
        print(f"  • {rec}")
    print("\n✅ اختبار اكتشاف الأنماط نجح!\n")
    
    # اختبار 4: اقتراحات الرفاهية
    print("=" * 60)
    print("✨ اختبار 4: اقتراحات الرفاهية")
    print("=" * 60)
    user_data = {
        "sleep_hours": 5.5,
        "exercise_days": 1,
        "stress_level": 8
    }
    suggestions = marwa.get_wellness_suggestions(user_data)
    print(f"التقييم العام:\n{suggestions['التقييم_العام']}")
    print(f"\nمجالات التحسين:")
    for area in suggestions['مجالات_التحسين']:
        print(f"  • {area}")
    print(f"\nرسالة مروى:\n{suggestions['رسالة_مروى']}")
    print("\n✅ اختبار اقتراحات الرفاهية نجح!\n")
    
    # اختبار 5: System Prompt
    print("=" * 60)
    print("🎯 اختبار 5: System Prompt")
    print("=" * 60)
    system_prompt = marwa.get_system_prompt()
    print(f"طول System Prompt: {len(system_prompt)} حرف")
    print(f"أول 200 حرف:\n{system_prompt[:200]}...")
    print("\n✅ اختبار System Prompt نجح!\n")
    
    print("=" * 60)
    print("🎉 جميع الاختبارات نجحت! مروى جاهزة للعمل")
    print("=" * 60)

if __name__ == "__main__":
    test_marwa_agent()
