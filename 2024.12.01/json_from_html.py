from urllib.request import urlopen
from json import dumps
from pathlib import Path
from re import findall, S


def json_from_html(url: str, modules_pattern: str, encoding: str ='utf-8') -> Path:
    with urlopen(url) as response:
        html = response.read()
        content_type = response.headers.get_content_charset()
        
    if not content_type:
        content_type = str(html).find("charset=")
        content_type = str(html)[content_type+8:].split()[0]
    html = html.decode(encoding if encoding == content_type else content_type)
    
    data_dict = dict(findall(modules_pattern, html, S))
    json_data = dumps(data_dict, ensure_ascii=False, indent=2)
    
    current_path = globals()["__loader__"].path
    if url[-4:] == 'html':
        name_json_file = url[url.rfind("/")+1:-4] + "json"
    else:
        name_json_file = current_path[current_path.rfind("\\")+1:-2] + "json" 
        
    with open(name_json_file, "w", encoding=encoding) as output:
        output.writelines(json_data)
        
    return Path(current_path[:current_path.rfind("\\")+1]+name_json_file)




# >>> url = 'https://docs.python.org/3/py-modindex.html'
# >>> modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'
# >>> file_path = json_from_html(url, modules_pattern)
# >>> file_path.name
# 'py-modindex.json'
# >>> print(file_path.read_text(encoding='utf-8')[:110])
# {
  # "__future__": "Future statement definitions",
  # "__main__": "The environment where top-level code is run.
# >>>
# >>>
# >>> url = 'http://www.world-art.ru/cinema/rating_top.php'
# >>> films_pattern = (r'<tr .*?>'
# ...  r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'
# ...  r'<td .*?>(?P<rating>.*?)</td>')
# >>> file_path = json_from_html(url, films_pattern)
# >>> file_path.name
# 'json_from_html.json'
# >>> Path(__loader__.path).name
# 'json_from_html.py'
# >>> print(file_path.read_text(encoding='utf-8')[:110])
# {
  # "Побег из Шоушенка": "8.9755",
  # "Зелёная миля": "8.9540",
  # "Форрест Гамп": "8.9035",
  # "Леон": "8.8920",
# >>>