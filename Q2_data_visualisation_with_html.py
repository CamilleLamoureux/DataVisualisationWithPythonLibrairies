# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

# Data visualization with html
html_content = i.data.to_html()
text_file = open("index.html", "w")
text_file.write(html_content)
text_file.close()
i.webbrowser.open_new_tab("index.html")

