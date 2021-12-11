import sys
sys.path.append('C:/Users/Brian/Documents/New_folder') #had PATH problems using atom 
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)
