import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("reservas_voos.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1,col2 = st.columns(2)
col3,col4,col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", 
                  color="Departure City", title="Voos por data")
col1.plotly_chart(fig_date, use_container_width=True)

df_grouped = df_filtered.groupby("Seat Class", as_index=False)["Total"].sum()  
fig_seat = px.bar(df_grouped,
                  x="Seat Class", y="Total", 
                  color="Seat Class", title="Receita por tipo de assento")
col2.plotly_chart(fig_seat, use_container_width=True)

df_users = df_filtered.groupby("Customer Type", as_index=False)["Booking ID"].count()
fig_users = px.bar(df_users, x="Customer Type", y="Booking ID", 
                   color="Customer Type", title="Quantidade de usuários por tipo de cliente")
col3.plotly_chart(fig_users, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

print(df.columns.tolist())
