
from ether import ETHER

def main():
    ether_frame = ETHER()
    src_address = "127.5.1.2"
    src_mac = "00:11:12:13:14:15:16:17"
    
    try:
        raw_frame = ether_frame.create_frame(src_address, src_mac, payload)
        print("Frame created successfully")
        print(f"Source address: {ether_frame.src_address}")
        print(f"Source MAC: {ether_frame.src_mac}")
        print(f"Payload: {ether_frame.payload}")
        print(f"Raw frame: {raw_frame}")
    except ValueError as ve:
        print(f"Error creating frame: {ve}")   

    
    raw_frame = b"\x00\x11\x22\x33\x44\x55\xC0\xA8\x01\x64Hello, Ethernet!"
    ether_parser=ETHER()

    try:
        src_address, src_mac, payload = ether_parser.parse_frame(raw_frame)
        print("\nFrame parsed successfully")
        print(f"Source address: {src_address}")
        print(f"Source MAC: {src_mac}")
        print(f"Payload: {payload}")
    except ValueError as ve:
        print(f"Error parsing frame: {ve}")

if __name__ == "__main__":
    main()