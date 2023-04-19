import sys
from config1 import DB_DETAILS

def main():
    """Progran takes at least one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

if __name__ == '__main__':
    main()
