#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  dacbook_v.4 - Client
  2026-09-14 16:44:52
"""

import requests
import sys
import time

SERVER_URL = "http://server-3-mzac.onrender.com"
TOOL_ID = "facbook_v.4"
LICENSE_KEY = "FACBOOK_-UHCB5D54313OU7R8LPQ6YVC0ELFJZ6X3"
TOOL_NAME = "dacbook_v.4"
INPUTS_PROMPTS = ['? Token :', '? id :']


def print_banner():
    print("=" * 60)
    print(f"  🛠️  {TOOL_NAME}")
    print("=" * 60)


def verify_license():
    print("\n🔐 جاري جلب الترخيص من السرفر...")
    try:
        response = requests.post(
            f"{SERVER_URL}/verify_license",
            json={"tool_id": TOOL_ID, "license_key": LICENSE_KEY},
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ تم التحقق من الترخيص")
            print(f"🏷️  الأداة: {data.get('tool_name', TOOL_NAME)}")
            if data.get('updated_at'):
                print(f"📅 آخر تحديث: {data['updated_at'][:19]}")
            return True
        else:
            try:
                error = response.json().get("error", "خطأ غير معروف")
            except Exception:
                error = response.text
            print(f"❌ فشل التحقق: {error}")
            return False
    except Exception as e:
        print(f"❌ خطأ: {e}")
        return False


def collect_inputs():
    if not INPUTS_PROMPTS:
        return ""
    print(f"\n📝 الأداة تحتاج {len(INPUTS_PROMPTS)} مدخل(ات):")
    print("-" * 60)
    values = []
    for i, prompt in enumerate(INPUTS_PROMPTS, 1):
        clean_prompt = prompt.strip() or f"مدخل #{i}"
        try:
            value = input(f"{i}. {clean_prompt}: ")
        except EOFError:
            value = ""
        values.append(value)
    return "\n".join(values) + "\n"


def start_execution(args, stdin_input=""):
    try:
        response = requests.post(
            f"{SERVER_URL}/execute",
            json={
                "tool_id": TOOL_ID,
                "license_key": LICENSE_KEY,
                "args": args,
                "stdin_input": stdin_input
            },
            timeout=30
        )
        if response.status_code == 202:
            return response.json().get("job_id")
        else:
            try:
                error = response.json().get("error", "خطأ")
            except Exception:
                error = response.text
            print(f"❌ خطأ ({response.status_code}): {error}")
            return None
    except Exception as e:
        print(f"❌ فشل الاتصال: {e}")
        return None


def stream_output(job_id):
    """عرض الإخراج لحظياً"""
    since = 0
    start_time = time.time()
    print()
    print("=" * 60)

    while True:
        try:
            response = requests.get(
                f"{SERVER_URL}/job_status/{job_id}?since={since}",
                timeout=15
            )
            if response.status_code == 404:
                print("\n❌ المهمة غير موجودة")
                return False

            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                new_lines = data.get("new_lines", [])

                for line in new_lines:
                    sys.stdout.write(line)
                    sys.stdout.flush()
                since = data.get("total_lines", since)

                if status == "completed":
                    print()
                    print("=" * 60)
                    return True
                elif status in ("timeout", "failed", "cancelled"):
                    result = data.get("result", {})
                    print(f"\n❌ {result.get('error', 'فشل')}")
                    return False

                if status in ("pending", "running"):
                    elapsed = int(time.time() - start_time)
                    if elapsed > 0 and elapsed % 5 == 0 and not new_lines:
                        sys.stdout.write(f"\r⏳ جاري التنفيذ... ({elapsed}ث)   ")
                        sys.stdout.flush()

            time.sleep(1.5)

        except requests.exceptions.Timeout:
            continue
        except KeyboardInterrupt:
            print("\n\n👋 تم الإلغاء")
            sys.exit(0)
        except Exception:
            time.sleep(2)


def main():
    print_banner()
    print(f"📡 السرفر: {SERVER_URL}")
    print("-" * 60)

    if not verify_license():
        print("\n❌ فشل التحقق من الترخيص")
        sys.exit(1)

    stdin_input = collect_inputs()
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    print(f"\n📤 إرسال الطلب للسرفر...")
    job_id = start_execution(args, stdin_input)
    if not job_id:
        print("❌ فشل بدء التنفيذ")
        sys.exit(1)

    success = stream_output(job_id)
    if success:
        print("✅ تم الانتهاء بنجاح")
    else:
        print("❌ فشل التنفيذ")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 تم الإلغاء")
        sys.exit(0)
