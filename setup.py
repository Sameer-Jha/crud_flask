#!/usr/bin/env python3
from app import db

def setupdb():
    db.create_all()

if __name__ == "__main__":
    setupdb()