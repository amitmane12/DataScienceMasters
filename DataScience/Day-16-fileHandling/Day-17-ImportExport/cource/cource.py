import sys
import os
from os.path import dirname, join, abspath

# Add the parent directory of 'cource' to the Python path
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# Now try importing serviceDetails
from service import serviceDetails

def courseDetails():
    print("These are my course details")

serviceDetails()
