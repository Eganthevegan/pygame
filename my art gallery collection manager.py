class ArtGallery:
    # 1. Constructor: Sets up the name and location
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []  # Starts with an empty list

    # 2. Method to add an artwork
    def add_artwork(self, name):
        self.artworks.append(name)
        print(f"'{name}' has been added.")

    # 3. Method to remove an artwork
    def remove_artwork(self, name):
        if name in self.artworks:
            self.artworks.remove(name)
            print(f"'{name}' has been removed.")
        else:
            print(f"'{name}' was not found.")

    # 4. Method to display the collection
    def display_artworks(self):
        print(f"\n--- {self.gallery_name} Collection ---")
        if not self.artworks:
            print("The gallery is empty.")
        else:
            for art in self.artworks:
                print(f"- {art}")

    # 5. Destructor: Shows a closing message when deleted
    def __del__(self):
        print(f"\nClosing {self.gallery_name}. Goodbye!")


# --- Menu Program ---
# Create the gallery object
name = input("Enter gallery name: ")
loc = input("Enter gallery location: ")
my_gallery = ArtGallery(name, loc)

# Menu loop
while True:
    print("\n1. Add Artwork | 2. Remove Artwork | 3. Display Gallery | 4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        art = input("Enter artwork name: ")
        my_gallery.add_artwork(art)
    elif choice == "2":
        art = input("Enter artwork to remove: ")
        my_gallery.remove_artwork(art)
    elif choice == "3":
        my_gallery.display_artworks()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

# Triggers the destructor at the very end
del my_gallery