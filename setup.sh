mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"adam86546853@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 29890\n\
\n\
[theme]\n\
base = \"light\"\n\
primaryColor = \"#89CFF0\"\n\
backgroundColor = \"#E0F7FE\"\n\
secondaryBackgroundColor = \"#FFFCE4\"\n\
textColor = \"#000000\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml
