#build
set FLASK_APP=app.py
flask freeze
cd build
cp * ..

#test
app run
