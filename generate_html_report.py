import markdown
from pathlib import Path

files = ["README.md", "commands.log"]
output = Path("index.html")

html_header = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>NFS + Kerberos Lab Report</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; line-height: 1.6; }
    h1 { color: #2c3e50; }
    h2 { color: #34495e; border-bottom: 1px solid #ccc; }
    code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; }
    pre { background-color: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.0/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({ startOnLoad: true });
  </script>
</head>
<body>
<h1>NFS + Kerberos Lab Report</h1>
"""

html_footer = "</body></html>"

full_html = html_header

# Markdownファイルの変換
for f in files:
    text = Path(f).read_text()
    html = markdown.markdown(text)
    full_html += f"<h2>{f}</h2>\n{html}<hr>\n"

# Mermaid構成図（直接埋め込み）
full_html += "<h2>Architecture Diagram</h2>\n"
full_html += """<pre class="mermaid">
graph TD
  Client[Linux Client (motokazu)]
  KDC[Kerberos KDC (LAB.LOCAL)]
  Server[NFS Server + Kerberos (samba.lab)]
  Keytab[/etc/krb5.keytab]
  Exports[/exports]
  Client -->|kinit| KDC
  Client -->|mount -o sec=krb5| Server
  Server --> Keytab
  Server --> Exports
</pre>
"""

full_html += html_footer
output.write_text(full_html)
print("✅ HTML report written to index.html")
