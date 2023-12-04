import subprocess

def main():
    print("Running MaswaliYote Quiz Management System...")

    # Here you can replace 'python' with 'python3' if needed
    try:
        subprocess.run(['python', 'quiz_system.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
