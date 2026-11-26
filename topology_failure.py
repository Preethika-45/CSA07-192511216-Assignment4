from itertools import combinations
from collections import deque
def links(kind,n):
    if kind=="bus": return [(i,i+1) for i in range(n-1)]
    if kind=="ring": return [(i,(i+1)%n) for i in range(n)]
    if kind=="star": return [("hub",i) for i in range(n)]
    if kind=="mesh": return list(combinations(range(n),2))
    raise ValueError(kind)
def connected_after_failure(edges,n,broken):
    adj={i:set() for i in range(n)}; adj["hub"]=set()
    for a,b in edges:
        if (a,b)==broken: continue
        adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
    seen=set(); q=deque([0])
    while q:
        x=q.popleft()
        if x in seen: continue
        seen.add(x); q.extend(adj[x]-seen)
    return all(i in seen for i in range(n))
if __name__=="__main__":
    n=5
    for k in ("bus","ring","star","mesh"):
        e=links(k,n); ok=sum(connected_after_failure(e,n,x) for x in e)
        print(f"{k:5} links={len(e):2} ports={2*len(e):2} survived={ok}/{len(e)}")
