import pandas as pd
import streamlit as st

class DataDashboard:
    @staticmethod
    def load_data(file):
        try:
            return pd.read_csv(file)
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
            return None

    @staticmethod
    def display_dashboard(data_file):
        st.title("Dashboard de Análise de Dados Financeiros")
        
        # Carregar dados
        df = DataDashboard.load_data(data_file)
        if df is not None:
            st.write("**Dados Carregados:**")
            st.dataframe(df)

            # Estatísticas gerais
            st.subheader("Estatísticas Gerais")
            st.write(df.describe())

            # Total por categoria
            st.subheader("Total por Categoria")
            category_totals = df.groupby("Categoria")["Valor"].sum()
            st.bar_chart(category_totals)

            # Filtro por data
            st.subheader("Filtro por Data")
            start_date = st.date_input("Data Inicial", df["Data"].min())
            end_date = st.date_input("Data Final", df["Data"].max())
            filtered_df = df[(df["Data"] >= str(start_date)) & (df["Data"] <= str(end_date))]
            st.write(filtered_df)

            # Gráfico de dispersão
            st.subheader("Gráfico de Dispersão")
            st.scatter_chart(df, x="Data", y="Valor")

def main():
    st.sidebar.title("Configurações")
    file = st.sidebar.file_uploader("Faça o upload de um arquivo CSV", type=["csv"])

    if file:
        DataDashboard.display_dashboard(file)

if __name__ == "__main__":
    main()
