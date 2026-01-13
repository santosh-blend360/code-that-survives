class AppSettings:
    # This variable will store the ONE and ONLY instance
    _instance = None

    def __new__(cls):
        # __new__ runs BEFORE __init__
        # It controls object creation

        if cls._instance is None:
            print("Creating AppSettings instance")
            cls._instance = super().__new__(cls)
        else:
            print("Reusing existing AppSettings instance")

        return cls._instance

    def __init__(self):
        # __init__ may be called multiple times,
        # so avoid heavy logic here
        self.theme = "dark"
        self.language = "en"

settings1 = AppSettings()
settings2 = AppSettings()

print(settings1 is settings2)

settings1.theme = "light"

print(settings2.theme) 
