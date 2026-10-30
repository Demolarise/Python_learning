favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King"] 
print("My favorite movies are:")
number = 1
    
for movie in favorite_movies:
    print(f"{number}. {movie}")
    number += 1

choice = input("\nDo you want to add or remove a movie from your list? (Option 1: Add, Option 2: Remove): ")

if choice == "1":
    new_movie = input("Enter the name of the movie you want to add: ")
    favorite_movies.append(new_movie)
    print("Movie added successfully! Updated list:")
    number = 1
    for movie in favorite_movies:
            print(f"{number}. {movie}")
            number += 1
elif choice == "2":
    remove_movie = input("Enter the name of the movie you want to remove: ")
    number = 1
    if remove_movie in favorite_movies:
        favorite_movies.remove(remove_movie)
        print("Movie removed successfully! Updated list:")
        for movie in favorite_movies:
            print(f"{number}. {movie}")
            number += 1
else:
    print("Movie not found in the list.")
    