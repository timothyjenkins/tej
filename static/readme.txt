#build
set FLASK_APP=app.py
flask freeze
cd build
cp * ..
cd ..

#test
app run
