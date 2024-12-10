## Setup and Installation

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
python -m playwright install
```
3. Modify the proxy variable in `main.py` with a working German (DE) proxy
4. Run the script:
```bash
python main.py
```