#Extract phone numbers, emails, or dates from a paragraph
import re

text = """
Contact us:
Email: support@shop.com or info@company.org
Phone: +91-9876543210, 9998887776
Date: 25-10-2025
"""

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
phones = re.findall(r'\+?\d[\d-]{9,}\d', text)
dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)

print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)
