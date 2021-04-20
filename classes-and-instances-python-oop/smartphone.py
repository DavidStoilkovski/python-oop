class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False
        self.occupied_memory = 0

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.occupied_memory + app_memory > self.memory:
            return f"Not enough memory to install {app}"

        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.occupied_memory += app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        memory_left = self.memory - self.occupied_memory
        return f"Total apps: {len(self.apps)}. Memory left: {memory_left}"

# Test code
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
