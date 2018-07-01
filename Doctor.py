class Doctor:
    def __init__(self, name="", specialty="", area="", rating=0.0):
        self.name = name
        self.specialty = specialty
        self.area = area
        self.rating = rating

def initializeDoctors():
    doctors = [
        Doctor(name="Ricky Kuang", specialty="Neurology", area="Alhambra, CA", rating=5),
        Doctor(name="John Doe", specialty="Dermatology", area="Alhambra, CA", rating=4),
        Doctor(name="Bugs Bunny", specialty="Cardiology", area="San Francisco, CA", rating=2),
        Doctor(name="Mickey Mouse", specialty="Neurology", area="Burbank, CA", rating=3),
        Doctor(name="Michael Jordan", specialty="Cardiology", area="Chicago, IL", rating=4),
        Doctor(name="Michael Scott", specialty="Dermatology", area="Scranton, PA", rating=3),
        Doctor(name="Usain Bolt", specialty="Cardiology", area="Miami, FL", rating=4),
        Doctor(name="Tom Langan", specialty="Neurology", area="San Francisco, CA", rating=5)
    ]
    doctors.sort(key=lambda x: x.rating, reverse=True)
    return doctors