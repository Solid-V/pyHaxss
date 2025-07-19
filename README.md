#  pyHaxxs

A Python-based reflected XSS scanner that automatically detects vulnerable input fields on a given URL and tests them using a JavaScript payload. Built with BeautifulSoup, Requests, and Colorama for CLI aesthetics.

---

##  Features

- Scans web pages for form `<input>` fields
- Matches them against common parameter names
- Injects a test XSS payload
- Detects successful reflections in the HTTP response

---

##  Requirements

Make sure Python 3 and `pip` are installed.

Install required packages:

```bash
pip install -r requirements.txt
```

---

## TODO
 - Add POST request support
 - DOM-based XSS detection (using headless browser)
 - Generate HTML vulnerability report
 - Add logging support
 - And many other features once i figure out how to :>
