def get_shipping_cost(weight, carrier): 
    if carrier == "fedex": 
        # FedEx: Flat $10 + $2 perkg 
        return 10 + (weight * 2) 
    elif carrier == "ups":
        # UPS: Flat $5 + $3 per kg + $1 fuel surcharge
        return 5 + (weight * 3) + 1 
    elif carrier =="postal_service": 
        # Postal: $1.5 per kg (No flat fee) 
        return weight * 1.5