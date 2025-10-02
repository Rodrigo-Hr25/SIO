## RUN

1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment (Every time you open a new terminal you need to do this to make the virtual environment the default Python interpreter of this shell):
```bash
source venv/bin/activate
```
or (Windows):
```bash
.\venv\Scripts\activate.ps1
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

(Se não der fazer isto:)
dos2unix run.sh
chmod +x run.sh

4. Run the application:


```bash
./run.sh app_org 8000
```
or:
```bash
./run.sh app_sec <PORT>
```

&emsp;&emsp;In Windows use instead:

```bash
.\run.bat app_org 8000
```
or:
```bash
.\run.bat app_sec <PORT>
```
5. Access the website:

```bash
http://127.0.0.1:<PORT>
```

6. To generate the database you need to access the following link:

```bash
/generate/all
```