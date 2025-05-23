import markdown
from pathlib import Path

# 読み込むMarkdownファイル
files = ["README.md", "commands.log"]
output = Path("index.html")

# HTMLヘッダー（Mermaid v9.4.0 & 遅延初期化対応）
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
    window.addEventListener("DOMContentLoaded", function () {
      mermaid.initialize({ startOnLoad: true });
    });
  </script>
</head>
<body>
<h1>NFS + Kerberos Lab Report</h1>
"""

html_footer = "</body></html>"

# HTML本文生成
full_html = html_header

# Markdownファイルを変換して追加
for f in files:
    text = Path(f).read_text()
    html = markdown.markdown(text)
    full_html += f"<h2>{f}</h2>\n{html}<hr>\n"

# Mermaid構成図（直接HTMLに埋め込み）
full_html += """
<h2>Architecture Diagram</h2>
<pre class="mermaid">
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

# HTMLファイル書き出し
full_html += html_footer
output.write_text(full_html)
print("✅ HTML report written to index.html")
