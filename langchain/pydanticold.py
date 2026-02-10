# from pydantic import BaseModel, Field, ValidationError, validator, rootModel

# # class WeatherInput(BaseModel):
# #     """Input for weather queries."""
# #     location: str = Field(description="City name or coordinates")
# #     units: Literal["celsius", "fahrenheit"] = Field(
# #         default="celsius",
# #         description="Temperature unit preference"
# #     )
# #     include_forecast: bool = Field(
# #         default=False,
# #         description="Include 5-day forecast"
# #     )


# # input = WeatherInput(location="New York", units="fahrenheit", include_forecast=True)

# location = str(input("Enter your location (e.g., city name or coordinates): "))
# if not location:
#     raise ValueError("Location is required.")

# units = str(input("Preferred temperature units (celsius/fahrenheit, default: celsius): ") or "celsius")
# if units not in ["celsius", "fahrenheit"]:
#     raise ValueError("Units must be 'celsius' or 'fahrenheit'.")

# include_forecast_input = input("Include 5-day forecast? (yes/no, default: no): ") or "no"
# include_forecast = include_forecast_input.lower() in ["yes", "y"]
# if include_forecast_input.lower() not in ["yes", "y", "no", "n"]:
#     raise ValueError("Include forecast must be 'yes' or 'no'.")

# def get_weather(location, units, include_forecast) -> str:
#     temp = 22 if units == "celsius" else 72
#     result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
#     if include_forecast:
#         result += "\nNext 5 days: Sunny"
#     return result



