from bs4 import BeautifulSoup

with open("weather.html", "r") as file:
    soup=BeautifulSoup(file)

forecast_entries = soup.find_all("tr")[1:]

weather_data = []
for entry in forecast_entries:
    day = entry.find_all("td")[0].text
    temperature = int(entry.find_all("td")[1].text.replace("°C", ""))
    condition = entry.find_all("td")[2].text
    weather_data.append({"day": day, "temperature": temperature, "condition": condition})

print("Weather Forecast:")
for data in weather_data:
    print(f"Day: {data['day']}, Temperature: {data['temperature']}°C, Condition: {data['condition']}")

high = max(weather_data, key=lambda x:x["temperature"])
print(f"\nDay with the highest temperature: {high['day']} ({high['temperature']}°C)")

sunny = [data["day"] for data in weather_data if data["condition"].lower() == "sunny"]
print(f"\nDays with 'Sunny' condition: {', '.join(sunny)}")

avgTemp = sum(data["temperature"] for data in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {avgTemp:.2f}°C")