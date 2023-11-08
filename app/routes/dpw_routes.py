from flask import Blueprint, jsonify
from app import driver
from app.models.dpw import is_current_visited, check_current_type, check_north_type, check_south_type, check_east_type, check_west_type, check_current_pheromone, check_north_pheromone, check_east_pheromone, check_south_pheromone, check_west_pheromone, deposit_pheromone, evaporate_pheromones, set_east_type,set_north_type, set_south_type, set_west_type

dpw_bp = Blueprint('dpw', __name__)

# Define a route to deposit pheromone in a cell
@dpw_bp.route('/deposit-pheromone/<int:x_pos>/<int:y_pos>/<int:pheromone_intensity>', methods=['POST'])
def visit_cell(x_pos, y_pos, pheromone_intensity):
    try:
        # Call the function to run the Neo4j query
        result = deposit_pheromone(driver, x_pos, y_pos, pheromone_intensity)

        if result:
            return "Pheromone successfully deposited!", 200
        else:
            return jsonify({"Error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Define an API route to evaporate all pheromones from the territory
@dpw_bp.route('/evaporate-pheromones', methods=['POST'])
def evaporate_pheromones_intensities():
    try:
        # Call the function to run the Neo4j query
        result = evaporate_pheromones(driver)

        if result:
            return "Pheromones evaporated!", 200
        else:
            return jsonify({"Error": "An error has occurred"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

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

# Define a route to query the type of a cell
@dpw_bp.route('/check-current-type/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_current_type(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_current_type(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to check if a cell is visited
@dpw_bp.route('/check-if-visited/<int:x_pos>/<int:y_pos>', methods=['GET'])
def check_if_visited(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = is_current_visited(driver, x_pos, y_pos)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Define a route to get the pheromone intensity from the current cell
@dpw_bp.route('/current-pheromone/<int:x_pos>/<int:y_pos>', methods=['GET'])
def get_current_pheromone(x_pos, y_pos):
    try:

        with driver.session() as session:
            result = check_current_pheromone(driver, x_pos, y_pos)

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

# Define a route to set the type of the north neighbor
@dpw_bp.route('/set-north-neighbor/<int:x_pos>/<int:y_pos>/<int:cell_type>', methods=['POST'])
def set_north_neighbor(x_pos, y_pos, cell_type):
    try:

        with driver.session() as session:
            result = set_north_type(driver, x_pos, y_pos, cell_type)

        if result:
            if cell_type == 0:
                return "North neighbor successfully set as free space!", 200
            else:
                return "North neighbor successfully set as obstacle!", 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to set the type of the south neighbor
@dpw_bp.route('/set-south-neighbor/<int:x_pos>/<int:y_pos>/<int:cell_type>', methods=['POST'])
def set_south_neighbor(x_pos, y_pos, cell_type):
    try:

        with driver.session() as session:
            result = set_south_type(driver, x_pos, y_pos, cell_type)

        if result:
            if cell_type == 0:
                return "South neighbor successfully set as free space!", 200
            else:
                return "South neighbor successfully set as obstacle!", 200

        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to set the type of the east neighbor
@dpw_bp.route('/set-east-neighbor/<int:x_pos>/<int:y_pos>/<int:cell_type>', methods=['POST'])
def set_east_neighbor(x_pos, y_pos, cell_type):
    try:

        with driver.session() as session:
            result = set_east_type(driver, x_pos, y_pos, cell_type)

        if result:
            if cell_type == 0:
                return "East neighbor successfully set as free space!", 200
            else:
                return "East neighbor successfully set as obstacle!", 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to set the type of the west neighbor
@dpw_bp.route('/set-west-neighbor/<int:x_pos>/<int:y_pos>/<int:cell_type>', methods=['POST'])
def set_west_neighbor(x_pos, y_pos, cell_type):
    try:

        with driver.session() as session:
            result = set_west_type(driver, x_pos, y_pos, cell_type)

        if result:
            if cell_type == 0:
                return "West neighbor successfully set as free space!", 200
            else:
                return "West neighbor successfully set as obstacle!", 200
        else:
            return jsonify({"error": "Node not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
