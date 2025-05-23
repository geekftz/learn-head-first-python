fav_movies = ["The Holy Grail", "The Life of Brian"]

for each_flick in fav_movies:
    print(f"One of my favorite movies is {each_flick}")


count = 0
while count < len(fav_movies):
  print(fav_movies[count])
  count += 1

def greet(name: str) -> str:
  # return f"Hello, {name}!"
  return f"Hello, {name}"  # :ml-citation{ref="1,3" data="citationList"}


greetName = greet("John")
print(greetName)