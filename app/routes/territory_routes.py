from flask import Blueprint, jsonify
from app import driver, territory_file_path
from app.models.territory import create_cells, create_relations, delete_territory

territory_bp = Blueprint('territory', __name__)

# Other territory-related routes
@territory_bp.route('/initiate', methods=['POST'])
def initiate_territory():
    try:
        # Read and process the .txt file
        with open(territory_file_path, "r") as file:
            lines = file.readlines()

        # Create the Neo4j driver session outside of the loop
        with driver.session() as session:
            # Loop through the lines
            for y, line in enumerate(lines):
                line = line.strip()
                # Loop through the characters in each line
                for x, value in enumerate(line):
                    # Use the session to create nodes here
                    session.execute_write(create_cells, x, y, value)

        # Create relationships
        with driver.session() as session:
            session.execute_write(create_relations)

        return "Territory successfully created!", 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@territory_bp.route('/reset', methods=['POST'])
def reset_territory():
    try:

        delete_territory(driver)
        result_initiation = initiate_territory()
        if result_initiation:
            return "Territory successfully reset!", 200
        else:
            return jsonify({"Error": "There has been an error resetting the territory."}), 404
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@territory_bp.route('/remove', methods=['POST'])
def remove_territory():
    try:
        # Call the function to run the Neo4j query
        delete_territory(driver)
        return "Territory successfully deleted!", 200
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500