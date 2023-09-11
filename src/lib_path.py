import sys
import os

if hasattr(sys, "implementation") and sys.implementation.name != "micropython":
    sys.path.append(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib/')
    )
