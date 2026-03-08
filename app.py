import streamlit as st
import pandas as pd
from textblob import TextBlob

# 1. Configuração da Página
st.set_page_config(page_title="Philosophy Analytics Hub", page_icon="🏛️", layout="wide")
st.title("🏛️ Philosophical Thought & Sentiment Explorer")
st.markdown("Analyze classic philosophical quotes to extract underlying sentiments and engagement metrics for educational content.")

# 2. Base de Dados Simulada (Citações e engajamento em plataformas de estudo)
data = {
    'Philosopher': ['Marcus Aurelius', 'Friedrich Nietzsche', 'Arthur Schopenhauer', 'Socrates', 'Immanuel Kant', 'Marcus Aurelius', 'Friedrich Nietzsche'],
    'Book/Source': ['Meditations', 'Thus Spoke Zarathustra', 'The World as Will and Representation', 'Apology (Plato)', 'Critique of Pure Reason', 'Meditations', 'Beyond Good and Evil'],
    'Quote': [
        'You have power over your mind - not outside events. Realize this, and you will find strength.', 
        'He who has a why to live for can bear almost any how.', 
        'Life is a constant process of dying.', 
        'The unexamined life is not worth living.', 
        'Thoughts without content are empty, intuitions without concepts are blind.', 
        'The happiness of your life depends upon the quality of your thoughts.',
        'To live is to suffer, to survive is to find some meaning in the suffering.'
    ],
    'Saves_by_Students': [5400, 4200, 1500, 3800, 900, 6100, 4800]
}
df = pd.DataFrame(data)

# 3. Lógica de NLP (Processamento de Linguagem Natural adaptado para Filosofia)
def analyze_philosophical_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0.15:
        return 'Optimistic ☀️'
    elif score < -0.15:
        return 'Pessimistic ⛈️'
    else:
        return 'Objective/Neutral ⚖️'

# Aplicando a IA
df['School_of_Thought_Tone'] = df['Quote'].apply(analyze_philosophical_sentiment)

# 4. Interface de Usuário (Filtros na barra lateral)
st.sidebar.header("Explore the Thinkers")
selected_philosopher = st.sidebar.selectbox("Select a Philosopher", df['Philosopher'].unique())

filtered_df = df[df['Philosopher'] == selected_philosopher]

# 5. Apresentação dos Dados (Métricas KPI)
st.subheader(f"Wisdom Overview: {selected_philosopher}")

col1, col2, col3 = st.columns(3)
col1.metric("Quotes Analyzed", len(filtered_df))
col2.metric("Total Student Bookmarks", filtered_df['Saves_by_Students'].sum())
col3.metric("Predominant Tone", filtered_df['School_of_Thought_Tone'].mode()[0])

# 6. Adicionando um Elemento Visual (Gráfico de Barras)
st.markdown("### 📊 Engagement by Quote")
# Criei um gráfico simples mostrando qual citação foi mais salva pelos estudantes
chart_data = filtered_df[['Quote', 'Saves_by_Students']].set_index('Quote')
st.bar_chart(chart_data)

# 7. Tabela de Dados Brutos
st.markdown("### 📜 Classical Texts & NLP Analysis")
st.dataframe(filtered_df[['Book/Source', 'Quote', 'School_of_Thought_Tone']], use_container_width=True)

st.markdown("---")
st.markdown("**🎓 Educator's Insight:** Use the highly-bookmarked quotes to design engaging lesson plans or discussion prompts for critical thinking sessions.")