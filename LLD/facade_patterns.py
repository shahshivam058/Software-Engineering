# The complex subsystem classes
class TV:
    def turn_on(self):
        print("TV: Turning On")
    def set_input(self, source):
        print(f"TV: Setting input to {source}")

class SoundSystem:
    def turn_on(self):
        print("Sound System: Turning On")
    def set_volume(self, level):
        print(f"Sound System: Setting volume to {level}")

class Lights:
    def dim(self, level):
        print(f"Lights: Dimming to {level}%")

# The Facade class
class HomeTheaterFacade:
    def __init__(self, tv, sound, lights):
        self.tv = tv
        self.sound = sound
        self.lights = lights

    def watch_movie(self, movie_title):
        print(f"\nHomeTheaterFacade: Get ready to watch {movie_title}...")
        self.lights.dim(20)
        self.tv.turn_on()
        self.tv.set_input("BluRay")
        self.sound.turn_on()
        self.sound.set_volume(15)
        print("Enjoy the movie!\n")

    def end_movie(self):
        print("HomeTheaterFacade: Shutting down...")
        self.sound.turn_off() # Assuming methods exist
        self.tv.turn_off()
        self.lights.turn_on()
        print("HomeTheaterFacade: Done.\n")

# The Client
if __name__ == "__main__":
    tv = TV()
    sound = SoundSystem()
    lights = Lights()

    # The client only interacts with the facade
    theater = HomeTheaterFacade(tv, sound, lights)
    theater.watch_movie("Inception")
    # theater.end_movie()