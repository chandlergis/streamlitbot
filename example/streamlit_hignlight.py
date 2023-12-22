# Original phrases string
phrases_str = """
最佳
"""
import streamlit as st

# Function to highlight phrases in text
def highlight_phrases_in_text(text, phrases):
    for phrase in phrases:
        if phrase in text:
            text = text.replace(phrase, f"<span style='color:red;font-weight:bold;'>{phrase}</span>")
    return text

# Streamlit app
def main():
    st.title("违禁词检测📸")

    # Text input for the article
    text = st.text_area("输入待检测文案:", height=250)

    # Text input for custom phrases
    custom_phrases_str = st.text_area("输入你的违禁词 (一行一个，没有双引号：张三 王五):", height=100)
    # Splitting the custom phrases into a list
    custom_phrases = [phrase.strip() for phrase in custom_phrases_str.split('\n') if phrase.strip()]

    # Button to perform the highlighting
    if st.button("检测违禁词"):
        # Combining default and custom phrases
        all_phrases = custom_phrases

        # Highlighting the phrases in the text
        highlighted_text = highlight_phrases_in_text(text, all_phrases)

        # Displaying the result
        st.markdown(highlighted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()