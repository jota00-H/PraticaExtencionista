import sys, base64, io, pathlib
from playwright.sync_api import sync_playwright
url = sys.argv[1] if len(sys.argv) > 1 else ""
html = pathlib.Path("folder.html").read_text()
if url:
    import qrcode, qrcode.image.svg
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, border=1)
    b = io.BytesIO(); img.save(b)
    qr = f'<div class="qr"><img src="data:image/svg+xml;base64,{base64.b64encode(b.getvalue()).decode()}"></div>'
else:
    qr = '<div class="qr placeholder">INSERIR AQUI<br>o QR code<br>do roteiro<br>de consulta</div>'
pathlib.Path("_render.html").write_text(html.replace("__QR__", qr))
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page()
    pg.goto("file://" + str(pathlib.Path("_render.html").resolve()))
    pg.wait_for_timeout(500)
    # overflow check
    print(pg.evaluate("""[...document.querySelectorAll('.panel')].map((p,i)=>{let m=0;p.querySelectorAll('*').forEach(e=>{if(getComputedStyle(e).position!=='absolute'){const r=e.getBoundingClientRect(),pr=p.getBoundingClientRect();m=Math.max(m,r.bottom-pr.top)}});return i+':'+Math.round(m/3.78)+'mm'})"""))
    pg.pdf(path="Folder_Salario-Maternidade.pdf", width="297mm", height="210mm", print_background=True, prefer_css_page_size=True)
    br.close()
