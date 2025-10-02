def calculate_cranes(capacity, productivity, hours, ratio):
    return capacity / (productivity * hours * ratio)

def calculate_trucks(daily_demand, loading, unloading, distance, speed, availability, shifts, shift_hours):
    cycle_time = (loading/60) + (distance/(speed*1000/3600)) + (unloading/60) + (distance/(speed*1000/3600))  # in minutes
    available_time = 60 * availability * 1 * 0.7  # simplified traffic factor included
    deliveries_per_hour = available_time / cycle_time
    deliveries_per_day = deliveries_per_hour * (shifts * shift_hours)
    return daily_demand / deliveries_per_day
