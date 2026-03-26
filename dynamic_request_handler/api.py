import frappe
import requests
import json

@frappe.whitelist()
def send_request(url, method="POST", headers=None, payload=None, timeout=5):
    """
    Send a dynamic HTTP request.
    Can be used for IoT devices, webhooks, or any external API.
    
    :param url: target URL
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param headers: JSON string or dict of headers
    :param payload: JSON string or dict of data to send
    :param timeout: request timeout
    """
    try:
        # Convert headers/payload from JSON string if needed
        if isinstance(headers, str):
            headers = json.loads(headers)
        if isinstance(payload, str):
            payload = json.loads(payload)
        
        method = method.upper()
        
        if method == "GET":
            r = requests.get(url, headers=headers, params=payload, timeout=timeout)
        elif method == "POST":
            r = requests.post(url, headers=headers, json=payload, timeout=timeout)
        elif method == "PUT":
            r = requests.put(url, headers=headers, json=payload, timeout=timeout)
        elif method == "DELETE":
            r = requests.delete(url, headers=headers, json=payload, timeout=timeout)
        else:
            frappe.throw(f"Unsupported HTTP method: {method}")
        
        return {"status": "success", "code": r.status_code, "response": r.text}
    
    except Exception as e:
        frappe.log_error(f"Failed sending request to {url}: {str(e)}", "Dynamic Request Error")
        return {"status": "failed", "error": str(e)}
