import urllib.request, urllib.parse, json, re, sys, time

def wiki_search(q, limit=4):
    url="https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch="+urllib.parse.quote(q)+f"&format=json&srlimit={limit}"
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 research-bot"})
        d=json.load(urllib.request.urlopen(req, timeout=12))
        return [(r['title'], re.sub('<[^>]+>','',r.get('snippet',''))[:90]) for r in d.get('query',{}).get('search',[])]
    except Exception as e:
        return [("ERR", str(e)[:80])]

def ddg_api(q):
    # DuckDuckGo Instant Answer API (JSON)
    url="https://api.duckduckgo.com/?q="+urllib.parse.quote(q)+"&format=json&no_html=1&no_redirect=1"
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 research-bot"})
        d=json.load(urllib.request.urlopen(req, timeout=12))
        rel=[(x.get('text','')[:90], x.get('firstURL','')) for x in d.get('RelatedTopics',[]) if isinstance(x,dict) and 'text' in x][:4]
        abst=d.get('AbstractText','')[:120]
        return abst, rel
    except Exception as e:
        return "", [("ERR", str(e)[:60])]

if __name__=="__main__":
    queries=sys.argv[1:]
    out=[]
    for q in queries:
        w=wiki_search(q)
        a,r=ddg_api(q)
        out.append({"query":q,"wiki":w,"ddg_abstract":a,"ddg_rel":r})
        time.sleep(0.3)
    print(json.dumps(out, indent=2, ensure_ascii=False))
