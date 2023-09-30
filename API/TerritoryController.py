from neo4j import GraphDatabase
from flask import Flask, request, jsonify

#Connect to Neo4j database
URI = "bolt://localhost:7687"  #Change this URI if necessary
USERNAME = "neo4j"
PASSWORD = "territory"
TERRITORY_FILE = "../TerritoryFiles/territory.txt"

def create_cells(driver, x, y, value):
    if value == '0':
        query = (
            "CREATE (c:Cell {visited: 'F', type: 0, pheromoneIntensity: 500, xPos: $x, yPos: $y})"
        )
    elif value == '1':
        query = (
            "CREATE (c:Cell {visited: null, type: 1, pheromoneIntensity: null, xPos: $x, yPos: $y})"
        )
    
    driver.run(query, x=x, y=y)

def create_relations(driver):
    relations_query = """
    MATCH (c:Cell)
    OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
    OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
    OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
    OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})

    FOREACH (north IN CASE WHEN northNeighbor IS NOT NULL THEN [northNeighbor] ELSE [] END |
        CREATE (c)-[:northNeighbor]->(north))
    FOREACH (west IN CASE WHEN westNeighbor IS NOT NULL THEN [westNeighbor] ELSE [] END |
        CREATE (c)-[:westNeighbor]->(west))
    FOREACH (east IN CASE WHEN eastNeighbor IS NOT NULL THEN [eastNeighbor] ELSE [] END |
        CREATE (c)-[:eastNeighbor]->(east))
    FOREACH (south IN CASE WHEN southNeighbor IS NOT NULL THEN [southNeighbor] ELSE [] END |
        CREATE (c)-[:southNeighbor]->(south))
    """

    # Execute the query
    driver.run(relations_query)

def deposit_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    SET  c.pheromoneIntensity = 500
    RETURN c;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()  # Assuming you expect a single result

def visit_cell(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    SET  c.visited = 'V'
    RETURN c;
    """
    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()  # Assuming you expect a single result

# Define a function to decrement pheromoneIntensity
def evaporate_pheromones(driver):
    query = """
    MATCH (c:Cell)
    WHERE c.pheromoneIntensity > 0
    SET c.pheromoneIntensity = c.pheromoneIntensity - 1
    RETURN c;
    """

    with driver.session() as session:
        result = session.run(query)
        return result

def delete_territory(driver):
    query = "MATCH (c) DETACH DELETE c"

    with driver.session() as session:
        session.run(query)

def initiate_territory(territory_txt_path, driver):
    # Read and process the .txt file
    with open(territory_txt_path, "r") as file:
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

    create_relations(driver)



driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
app = Flask(__name__)

@app.route('/api/initiate-territory', methods=['POST'])
def initiate_territory():
    try:
        # Read and process the .txt file
        with open(TERRITORY_FILE, "r") as file:
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

        return jsonify({"message": "Territory data uploaded successfully!"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

driver.close()