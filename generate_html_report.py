import markdown
from pathlib import Path

# 読み込むファイル
files = ["README.md", "commands.log"]

# 出力HTMLファイル
output = Path("index.html")

# HTMLのヘッダー
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
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true });
  </script>
</head>
<body>
<h1>NFS + Kerberos Lab Report</h1>
"""

# フッター
html_footer = "</body></html>"

# 変換＋結合
full_html = html_header
for f in files:
    text = Path(f).read_text()
    html = markdown.markdown(text)
    full_html += f"<h2>{f}</h2>\n" + html + "<hr>\n"

# Mermaid図を追加
mermaid_code = Path("diagram.mmd").read_text()
full_html += "<h2>Architecture Diagram</h2>\n"
full_html += f"<pre class=\"mermaid\">\n{mermaid_code}\n</pre>\n"

full_html += html_footer

output.write_text(full_html)
print(f"✅ HTML report written to {output}")
