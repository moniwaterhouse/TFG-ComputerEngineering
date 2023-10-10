
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

    # Execute the query
    driver.run(relations_query)

def delete_territory(driver):
    query = "MATCH (c) DETACH DELETE c"

    with driver.session() as session:
        session.run(query)

