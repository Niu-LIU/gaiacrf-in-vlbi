def parse_arc(arcfile):
    """Extract session identifier and network from arc file.

    This maybe only works for the src file of Sebastien.
    """
    sessids = []
    networks = []

    with open(arcfile, "r") as farc:
        for line in farc.readlines():

            line = line.strip().strip("\n")

            # The commented character is "*"
            if line.startswith("*"):
                continue

            line1, line2 = line.split("!")
            sessid = line1.split()[0]
            network = line2.split()[-1]

            sessids.append(sessid)
            networks.append(network)

    return sessids, networks


arcfile = "../data/icrf3.arc"

sessids, networks = parse_arc(arcfile)
