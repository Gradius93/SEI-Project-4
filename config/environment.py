import os

secret = os.getenv('SECRET', 'malthopsyeastwater')
db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/craftbeer-db')
