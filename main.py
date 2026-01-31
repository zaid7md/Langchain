from dotenv import load_dotenv 
import os 

load_dotenv(override='True')

def main():
    print("Hello from langchain-course!")
    print(os.getenv("api_key"))

if __name__ == "__main__":
    main()
