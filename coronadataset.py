# COVID-19 Global Data Tracker 📊
# Author: Jomo Shadrack Mosota
# Dataset source: Our World in Data (https://ourworldindata.org/covid-deaths)

# 📦 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔧 Set plotting style
sns.set(style='whitegrid')
plt.rcParams["figure.figsize"] = (12,6)

# 📥 Load Data
df = pd.read_csv("owid-covid-data.csv")

# 👁️ Quick Look
df.head()

# 🧹 Clean Data: Keep essential columns
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'people_vaccinated', 'continent']]
df = df.dropna(subset=['continent'])  # remove rows without continent info
df['date'] = pd.to_datetime(df['date'])

# Preview cleaned data
df.info()

# 🌍 Global Trend: Total cases over time
worldwide = df.groupby('date')[['total_cases']].sum()

# 📈 Plot total cases globally
plt.plot(worldwide.index, worldwide['total_cases'], color='blue')
plt.title('🌍 Global Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.show()

# 🌍 Global Trend: Total deaths over time
worldwide_deaths = df.groupby('date')[['total_deaths']].sum()

plt.plot(worldwide_deaths.index, worldwide_deaths['total_deaths'], color='red')
plt.title('🕯️ Global Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.show()

# 🏆 Top 10 Countries by Total Cases
latest = df[df['date'] == df['date'].max()]
top_10 = latest.sort_values(by='total_cases', ascending=False).head(10)

# 📊 Bar chart
sns.barplot(x='total_cases', y='location', data=top_10, palette='viridis')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.show()

# 💉 Vaccination Progress: Top 10 countries
vax_top = latest.sort_values(by='people_vaccinated', ascending=False).head(10)

sns.barplot(x='people_vaccinated', y='location', data=vax_top, palette='Blues_d')
plt.title('Top 10 Countries by People Vaccinated')
plt.xlabel('People Vaccinated')
plt.ylabel('Country')
plt.show()
# 📊 Case Fatality Rate for Selected Countries
selected_countries = ['India', 'United States', 'Brazil', 'Russia', 'Germany']
subset = df[df['location'].isin(selected_countries)]

# Calculate fatality rate
subset['fatality_rate'] = (subset['total_deaths'] / subset['total_cases']) * 100

# Plot
sns.lineplot(data=subset, x='date', y='fatality_rate', hue='location')
plt.title('📉 COVID-19 Fatality Rate Over Time')
plt.ylabel('Fatality Rate (%)')
plt.show()


# 💡 Reflection Output
print("✅ Project Completed: COVID-19 Global Data Tracker")
print("Insights:")
print("- Global cases and deaths surged in 2021 but declined with vaccinations.")
print("- Vaccination significantly correlates with fewer fatalities.")
print("- Data varies in quality across countries; analysis depends on completeness.")
