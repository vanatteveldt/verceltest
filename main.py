# main.py
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # This is what will be refrenced in config



@app.get("/", response_class=HTMLResponse)
async def root():
    x = int(random.uniform(5, 40))
    y = int(random.uniform(5, 40))
    deg = int(random.uniform(0, 360))
    size = int(random.uniform(50, 300))
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return f"""<html>
<body>
<pre style='width: 20em; font-size: {size}%; padding-left: {x}%; padding-top: {y}%; transform: rotate({deg}deg); color:{color}'>
 ,_     _
 |\\\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \\  _T_/-._( (
 /         `. \\
|         _  \\ |
 \\ \\ ,  /      |
  || |-_\\__   /
 ((_/`(____,-'
</pre>
<script>
setTimeout(function(){{
   window.location.reload(1);
}}, 1000);
</script>
</body></html>
"""