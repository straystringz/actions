def check_parking_meter(time_parked, time_purchased):
    noCharges = "no charges yet"
    charged = "overtime charged"

    if time_parked >= time_purchased:
        return charged
    else:
        return noCharges
