def process_order(item, type):
    if type == "digital":
        # logic for digital product
        print(f"Processing digital order for {item}")
        # send_download_link(item)

    elif type == "physical":
        # logic for physical product
        print(f"Processing physical order for {item}")
        # arrange_shipping(item)

    elif type == "subscription":
        # logic for subscription
        print(f"Processing subscription for {item}")
        # activate_subscription(item)

    elif type == "pre-order":
        # logic for pre-order
        print(f"Processing pre-order for {item}")
        # reserve_inventory(item)

    # Where does it end?
    else:
        raise ValueError("Unknown order type")
