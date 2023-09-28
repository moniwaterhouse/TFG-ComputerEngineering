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

    with driver.session() as session:
        session.run(relations_query)

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

create_relations(driver)

# Close the Neo4j driver
driver.close()