from flask import Blueprint, jsonify
from app import driver, territory_file_path
from app.models.dpw import check_north_type, check_south_type, check_east_type, check_west_type, check_north_pheromone, check_east_pheromone, check_south_pheromone, check_west_pheromone, deposit_pheromone, evaporate_pheromones

dpw_bp = Blueprint('dpw', __name__)

# Define a route to query the north neighbor's type
@dpw_bp.route('/check-north-neighbor/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_north_type(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_north_type(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the south neighbor's type
@dpw_bp.route('/check-south-neighbor/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_south_type(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_south_type(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the east neighbor's type
@dpw_bp.route('/check-east-neighbor/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_east_type(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_east_type(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the west neighbor's type
@dpw_bp.route('/check-west-neighbor/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_west_type(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_west_type(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the north neighbor's pheromone
@dpw_bp.route('/north-pheromone/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_north_pheromone(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_north_pheromone(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the south neighbor's pheromone
@dpw_bp.route('/south-pheromone/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_south_pheromone(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_south_pheromone(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the east neighbor's pheromone
@dpw_bp.route('/east-pheromone/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_east_pheromone(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_east_pheromone(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to query the west neighbor's pheromone
@dpw_bp.route('/west-pheromone/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_west_pheromone(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_west_pheromone(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define an API endpoint to deposit pheromone in a cell
@dpw_bp.route('/deposit-pheromone/<int:x_pos>/<int:y_pos>', methods=['POST'])
def visit_cell(x_pos, y_pos):
    try:
        # Call the function to run the Neo4j query
        result = deposit_pheromone(driver, x_pos, y_pos)

        if result:
            return jsonify({"Success": "Pheromone deposited"}), 200
        else:
            return jsonify({"Error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Define an API endpoint to evaporate pheromone intensity
@dpw_bp.route('/evaporate-pheromones', methods=['POST'])
def evaporate_pheromones_intensities():
    try:
        # Call the function to run the Neo4j query
        result = evaporate_pheromones(driver)

        if result:
            return jsonify({"Success": "Pheromones evaporated"}), 200
        else:
            return jsonify({"Error": "An error has occurred"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
