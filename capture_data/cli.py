"""查看已接收资料的身份与本地引用。"""
import argparse,json
from pathlib import Path
from .io import load
from .domain import summarize
from .journal import connect,receive
from .projection import overview
def main():
 p=argparse.ArgumentParser();p.add_argument('command',choices=['inspect']);p.add_argument('file');a=p.parse_args()
 path=Path(a.file);v,digest=load(path);summary=summarize(v,path.parent)
 c=connect(':memory:');source=receive(c,v,path.parent)
 print(json.dumps({'manifest_sha256':digest,'source_sha256':source,'summary':summary,'overview':overview(c,v['collection'])},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
