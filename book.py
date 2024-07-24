import datetime
import random

class AppointmentBookingChatbot:
    def __init__(self):
        self.available_slots = [
            "9:00 AM", "10:00 AM", "11:00 AM",
            "2:00 PM", "3:00 PM", "4:00 PM"
        ]
        self.booked_appointments = {}

    def greet(self):
        return "Hello! I'm your appointment booking assistant. How can I help you today?"

    def book_appointment(self, date, time):
        if date not in self.booked_appointments:
            self.booked_appointments[date] = []

        if time in self.available_slots and time not in self.booked_appointments[date]:
            self.booked_appointments[date].append(time)
            return f"Great! Your appointment is booked for {date} at {time}."
        else:
            return "I'm sorry, that time slot is not available. Would you like to try another time?"

    def suggest_time(self, date):
        if date not in self.booked_appointments:
            return random.choice(self.available_slots)
        
        available = [slot for slot in self.available_slots if slot not in self.booked_appointments[date]]
        return random.choice(available) if available else None

    def process_input(self, user_input):
        user_input = user_input.lower()

        if "book" in user_input and "appointment" in user_input:
            return "Sure, I can help you book an appointment. What date would you like?"

        elif "available" in user_input:
            today = datetime.date.today().strftime("%Y-%m-%d")
            suggested_time = self.suggest_time(today)
            if suggested_time:
                return f"For today ({today}), we have an opening at {suggested_time}. Would you like to book this slot?"
            else:
                return "I'm sorry, we don't have any available slots for today. Would you like to check another date?"

        elif "yes" in user_input:
            # This is a simplification. In a real scenario, you'd need to keep track of the conversation state.
            today = datetime.date.today().strftime("%Y-%m-%d")
            suggested_time = self.suggest_time(today)
            return self.book_appointment(today, suggested_time)

        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase or ask about booking an appointment?"

# Example usage
chatbot = AppointmentBookingChatbot()
print(chatbot.greet())

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Thank you for using our service. Goodbye!")
        break
    response = chatbot.process_input(user_input)
    print("Chatbot:", response)