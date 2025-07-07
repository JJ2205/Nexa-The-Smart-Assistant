from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query = "Ernakulam"
    url =f'https://in.search.yahoo.com/search?type=E211IN714G0&p=weather+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})


    # Find the temperature div
    temp_element = r.html.find('div.imperial-metric.fz-50.lh-40.pr-2', first=True)

    # Find the unit button
    unit_element = r.html.find('button.degree-unit-button', first=True)

    if temp_element:
        temp = temp_element.text.strip()  # Extracts the displayed temperature (e.g., 30)
        
        # Extract the temperature from data attributes if needed
        temp_celsius = temp_element.attrs.get('data-metric', 'N/A')  # Celsius value
        temp_fahrenheit = temp_element.attrs.get('data-imperial', 'N/A')  # Fahrenheit value

        if unit_element:
            unit = "°C" if "°C" in unit_element.text else "°F"
            print(f"Temperature: {temp}{unit}")
        else:
            print(f"Temperature: {temp} (Unit unknown)")

        print(f"Data Attribute Values - Celsius: {temp_celsius}°C, Fahrenheit: {temp_fahrenheit}°F")

    else:
        print("Error: Unable to find temperature data.")
