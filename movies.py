from flask import Flask, jsonify, request
app = Flask(__name__)
movies = [
    {"name": "The Shawsshank Redemption",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]},
    {"name": "The Godfather",
    "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
    "genres": ["Crime","Drama"]}]

@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200

if __name__ == '__main__':
    app.run() #run our Flask app