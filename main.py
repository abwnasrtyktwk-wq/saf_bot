# SAF AI Bot Main Application

class SafAiBot:
    def __init__(self):
        self.name = "SAF AI Bot"

    def greet(self):
        return f"Hello! I am {self.name}. How can I assist you today?"

if __name__ == "__main__":
    bot = SafAiBot()
    print(bot.greet())