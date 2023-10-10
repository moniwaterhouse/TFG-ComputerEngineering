def check_north_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
    RETURN
       northNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_south_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
    RETURN
       southNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_east_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
    RETURN
       eastNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_west_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
    RETURN
       westNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def set_north_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
        SET  northNeighbor.type = 1, northNeighbor.pheromoneIntensity = null, northNeighbor.visited = null
        RETURN northNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
        SET  northNeighbor.type = 0, northNeighbor.pheromoneIntensity = 0, northNeighbor.visited = 'F'
        RETURN northNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def set_south_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
        SET  southNeighbor.type = 1, southNeighbor.pheromoneIntensity = null, southNeighbor.visited = null
        RETURN southNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
        SET  southNeighbor.type = 0, southNeighbor.pheromoneIntensity = 0, southNeighbor.visited = 'F'
        RETURN southNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def set_east_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
        SET  eastNeighbor.type = 1, eastNeighbor.pheromoneIntensity = null, eastNeighbor.visited = null
        RETURN eastNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
        SET  eastNeighbor.type = 0, eastNeighbor.pheromoneIntensity = 0, eastNeighbor.visited = 'F'
        RETURN eastNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def set_west_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
        SET  westNeighbor.type = 1, westNeighbor.pheromoneIntensity = null, westNeighbor.visited = null
        RETURN westNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
        SET  westNeighbor.type = 0, westNeighbor.pheromoneIntensity = 0, westNeighbor.visited = 'F'
        RETURN westNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()
    

def deposit_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    SET  c.pheromoneIntensity = 500, c.visited = 'V'
    RETURN c;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()  # Assuming you expect a single result

def check_north_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
    RETURN
       northNeighbor.pheromoneIntensity AS northPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_south_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
    RETURN
       southNeighbor.pheromoneIntensity AS southPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_east_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
    RETURN
       eastNeighbor.pheromoneIntensity AS eastPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

def check_west_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
    RETURN
       westNeighbor.pheromoneIntensity AS westPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

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