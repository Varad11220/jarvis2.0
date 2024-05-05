def weather_report():
    import subprocess
    # Execute the curl command and capture its output
    output = subprocess.check_output('curl wttr.in/?format="%l:+%C+%h+%t+%f+%w\\n"', shell=True)

    # Decode the output from bytes to string
    output = output.decode('utf-8')

    # Remove leading and trailing quotes
    output = output.strip('"')

    # Split the output into individual components and store them in variables
    components = output.strip().split()

    # Extracting location as two strings
    location = ' '.join(components[:2]).replace(":","")
    condition = components[2]
    humidity = components[3].split(' ')[0]
    temperature = components[4].split(' ')[0]
    feels_like = components[5].split(' ')[0]
    wind = components[6]

    # JUST FOR DEBUGGING
    # print("\nLocation:", location)
    # print("Condition:", condition)
    # print("Humidity:", humidity)
    # print("Temperature:", temperature)
    # print("Feels Like:", feels_like)
    # print("Wind:", wind)

    # TUZHYA VOICE COMMAND SATHI
    # AJUN KAHI ASTIL TAR ADD KARU
    if condition.lower() == "rain":
        sentence = f"In {location}, the sky is graced with {condition} as the temperature stands at {temperature} with a gentle breeze of {wind}, making it feel like {feels_like}."
    elif condition.lower() == "cloudy":
        sentence = f"In {location}, the clouds obscure the sky amidst {condition} conditions, with the temperature holding steady at {temperature}, and a gentle breeze of {wind} making it feel like {feels_like}."
    else:
        sentence = f"In {location}, the air carries a hint of {condition} as the temperature sits at {temperature} with a gentle breeze of {wind}, making it feel like {feels_like}."

    return sentence