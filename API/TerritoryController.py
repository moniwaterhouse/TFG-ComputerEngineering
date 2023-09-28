from neo4j import GraphDatabase

def create_cells(driver, x, y, value):
    if value == '0':
        query = (
            "CREATE (c:Cell {visited: 'F', type: 0, pheromoneIntensity: 0, xPos: $x, yPos: $y})"
        )
    elif value == '1':
        query = (
            "CREATE (c:Cell {visited: null, type: 1, pheromoneIntensity: null, xPos: $x, yPos: $y})"
        )
    
    driver.run(query, x=x, y=y)

#Connect to Neo4j database
uri = "bolt://localhost:7687"  #Change this URI if necessary
username = "neo4j"
password = "territory"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Specify the path to your .txt file
territory_path = "../TerritoryFiles/territory.txt"

# Read and process the .txt file
with open(territory_path, "r") as file:
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

# Close the Neo4j driver
driver.close()