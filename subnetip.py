import ipaddress


def mask_to_cidr(mask_str):
    try:
        mask_octets = mask_str.strip().split('.')
        binary_str = ''.join(format(int(octet), '08b')
                             for octet in mask_octets)
        return str(binary_str.count('1'))
    except:
        raise ValueError("Invalid subnet mask format.")


def get_subnet_info(ip_str, mask_str):
    try:
        cidr = mask_to_cidr(mask_str)
        network_str = f"{ip_str}/{cidr}"
        network = ipaddress.ip_network(network_str, strict=False)

        subnet_id = network.network_address
        broadcast_ip = network.broadcast_address
        total_hosts = network.num_addresses
        usable_hosts = total_hosts - 2 if total_hosts > 2 else 0

        first_usable = None
        last_usable = None
        if usable_hosts > 0:
            first_usable = list(network.hosts())[0]
            last_usable = list(network.hosts())[-1]

        print("\n Subnet Information:")
        print(f"IP Address:        {ip_str}")
        print(f"Subnet Mask:       {mask_str}  (/ {cidr})")
        print(f"Subnet ID:         {subnet_id}")
        print(f"Broadcast IP:      {broadcast_ip}")
        print(f"Total Hosts:       {total_hosts}")
        print(f"Usable Hosts:      {usable_hosts}")
        if usable_hosts > 0:
            print(f"Usable IP Range:   {first_usable}  →  {last_usable}")
        else:
            print("Usable IP Range:   - (No usable IPs)")

        wasted_ips = total_hosts - usable_hosts - 2 if total_hosts > 2 else 0
        print(f"Wasted IPs:        {wasted_ips if wasted_ips > 0 else 0}")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    ip_input = input("Enter IP Address (e.g., 192.168.1.10): ")
    mask_input = input("Enter Subnet Mask (e.g., 255.255.255.0): ")
    get_subnet_info(ip_input, mask_input)
