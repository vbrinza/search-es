# search-es
Prerequisites:
1. Docker 18.03 ce
2. Python 3

How to run:
1. Clone the repo
```
git clone https://github.com/vbrinza/search-es
```
2. Start a virtual environment
```
python3 -m venv search-es && source search-es/bin/activate
```
3. Install dependencies
```
cd search-es && pip install -r requirementx.txt
```
4. Start a local ES inside Docker
```
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.3
```
5. Run the script
```
python search_es.py
```
