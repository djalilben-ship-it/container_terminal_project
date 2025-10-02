import pulp

def optimize_equipment(
    annual_capacity,
    crane_productivity,
    crane_hours,
    ratio,
    daily_demand,
    truck_cycle_time,
    truck_hours_per_day,
    crane_cost=1_000_000,
    truck_cost=100_000,
    max_cranes=10,
    max_trucks=50
):
    """
    Linear optimization model to minimize investment cost while meeting throughput demand.

    Parameters
    ----------
    annual_capacity : int
        Required annual throughput in containers.
    crane_productivity : int
        Containers handled per hour per crane.
    crane_hours : int
        Total annual working hours per crane.
    ratio : float
        40’/20’ handling ratio.
    daily_demand : int
        Containers per day to be handled by trucks.
    truck_cycle_time : float
        Average cycle time per truck in minutes.
    truck_hours_per_day : int
        Total working hours per truck per day.
    crane_cost, truck_cost : float
        Unit cost of cranes and trucks.
    max_cranes, max_trucks : int
        Upper bounds for decision variables.

    Returns
    -------
    dict : solution with optimal number of cranes and trucks.
    """

    # Problem definition
    model = pulp.LpProblem("Port_Equipment_Optimization", pulp.LpMinimize)

    # Decision variables
    cranes = pulp.LpVariable("Cranes", lowBound=0, upBound=max_cranes, cat='Integer')
    trucks = pulp.LpVariable("Trucks", lowBound=0, upBound=max_trucks, cat='Integer')

    # Constraints
    # Crane capacity per year
    crane_capacity = cranes * crane_productivity * crane_hours * ratio
    model += crane_capacity >= annual_capacity, "Crane_Capacity_Constraint"

    # Truck capacity per day
    deliveries_per_hour = 60 / truck_cycle_time
    deliveries_per_day = deliveries_per_hour * truck_hours_per_day
    truck_capacity = trucks * deliveries_per_day
    model += truck_capacity >= daily_demand, "Truck_Capacity_Constraint"

    # Objective: Minimize cost
    model += cranes * crane_cost + trucks * truck_cost

    # Solve
    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return {
        "Optimal_Cranes": int(pulp.value(cranes)),
        "Optimal_Trucks": int(pulp.value(trucks)),
        "Total_Cost": pulp.value(model.objective)
    }
