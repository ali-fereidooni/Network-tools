import ipaddress

def mask_to_cidr(mask_str):
    try:
        mask_octets = mask_str.strip().split('.')
        binary_str = ''.join(format(int(octet), '08b') for octet in mask_octets)
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

        print(f"IP Address:       {ip_str}")
        print(f"Subnet Mask:      {mask_str}  (/{cidr})")
        print(f"Subnet ID:        {subnet_id}")
        print(f"Broadcast IP:     {broadcast_ip}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_input = input("Enter IP Address (e.g., 192.168.1.10): ")
    mask_input = input("Enter Subnet Mask (e.g., 255.255.255.0): ")
    get_subnet_info(ip_input, mask_input)
