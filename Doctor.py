class Doctor:
    def __init__(self, name="", specialty="", area="", rating=0.0):
        self.name = name
        self.specialty = specialty
        self.area = area
        self.rating = rating

def initializeDoctors():
    return [
        Doctor(name="Ricky Kuang", specialty="Neurology", area="Alhambra, CA", rating=5),
        Doctor(name="John Doe", specialty="Dermatology", area="Alhambra, CA", rating=3),
        Doctor(name="Bugs Bunny", specialty="Cardiology", area="San Francisco, CA", rating=2),
        Doctor(name="Mickey Mouse", specialty="Neurology", area="Burbank, CA", rating=4)
    ]